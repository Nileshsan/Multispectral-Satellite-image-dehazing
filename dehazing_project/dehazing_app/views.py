from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm  # Import your custom form
import numpy as np
from PIL import Image
from django.http import JsonResponse
from django.core.files.storage import default_storage
from .model_loader import get_model  # Import the model loader



def home(request):
    return HttpResponse("Welcome to Multispectral Image Dehazing!")

def about_view(request):
    return render(request, 'about.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('users:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with desired URL name
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, "Login failed. Please check your credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def upload_image(request):
    return render(request, 'upload_image.html')  # Create a corresponding template if necessary

def processing_history(request):
    return render(request, 'processing_history.html')  # Create a corresponding template if necessary

def advanced_options(request):
    return render(request, 'advanced_options.html')  # Create a corresponding template if necessary


def dehazing_page(request):
    return render(request, 'dehazing.html')  # change template name to match your file



# Get the preloaded model
model = get_model()

def dehaze_image(request):
    if request.method == "POST" and request.FILES["image"]:
        uploaded_file = request.FILES["image"]
        
        # Save the uploaded file temporarily 
        file_path = default_storage.save("temp/hazy_image.jpg", uploaded_file)
        
        # Open and preprocess the image
        image = Image.open(file_path).resize((256, 256))  # Resize to match model input size
        image = np.array(image) / 255.0  # Normalize to [0,1]
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        
        # Run the model
        dehazed_image = model.predict(image)[0]  # Get the first (and only) output
        
        # Convert the output back to an image
        dehazed_image = (dehazed_image * 255).astype(np.uint8)  # Convert to [0,255] range
        dehazed_image = Image.fromarray(dehazed_image)

        # Save the processed image
        output_path = "media/dehazed_image.jpg"
        dehazed_image.save(output_path)

        # Return the output image URL
        return JsonResponse({"image_url": "/media/dehazed_image.jpg"})
    
    return render(request, "upload.html")  # Load the upload page


import os
import numpy as np
from PIL import Image
import uuid
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
from .model_loader import get_model  # Your model loader that loads the dehazing model

def dehaze_api(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]

        # Save the uploaded file.
        input_filename = f"input_{uuid.uuid4().hex}.jpg"
        input_path = default_storage.save(input_filename, uploaded_file)
        input_full_path = default_storage.path(input_path)

        # Open and preprocess the image
        image = Image.open(input_full_path).convert("RGB")
        image = image.resize((256, 256))
        im_array = np.array(image) / 255.0
        im_array = np.expand_dims(im_array, axis=0)

        # Process using your dehazing model
        model = get_model()
        dehazed_tensor = model(im_array)
        if isinstance(dehazed_tensor, dict):
            first_output = list(dehazed_tensor.values())[0]
        else:
            first_output = dehazed_tensor[0]

        # Convert the tensor to a NumPy array
        output_array = first_output.numpy()  # expect shape (1,1,256,3)
        
        # Remove the extra singleton dimensions.
        # In this example, we assume the extra axis (the second one) is accidental.
        # First remove batch dimension:
        output_array = output_array[0]  # shape becomes (1,256,3)
        # If the height dimension is 1 instead of 256, we can repeat it:
        if output_array.shape[0] == 1:
            output_array = np.repeat(output_array, 256, axis=0)  # now shape (256,256,3)

        dehazed_array = (output_array * 255).astype(np.uint8)
        try:
            dehazed_image = Image.fromarray(dehazed_array)
        except TypeError as e:
            return JsonResponse({"error": f"Image conversion failed: {e}"}, status=500)

        # Save processed image using MEDIA_ROOT
        output_filename = f"output_{uuid.uuid4().hex}.jpg"
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
        dehazed_image.save(output_path)

        # Construct URLs using MEDIA_URL
        input_url = default_storage.url(input_path)
        output_url = settings.MEDIA_URL + output_filename

        return JsonResponse({
            "input_image_url": input_url,
            "output_image_url": output_url
        })
    return JsonResponse({"error": "Invalid Request"}, status=400)

from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def dehazing_page(request):
    return render(request, "dehazing_page.html")


