import os
import tensorflow as tf
from keras.layers import TFSMLayer

# Define the path to your saved model folder
MODEL_PATH = os.path.join("C:/Users/Admin/multispectral_image_dehazing", "Nilesh_cycleGAN_dehaze_saved_model")

# Load the CycleGAN SavedModel as a Keras layer
model = TFSMLayer(
    MODEL_PATH,
    call_endpoint="serving_default"  # Ensure this matches your model's signature
)

def get_model():
    """Returns the loaded CycleGAN model as a layer."""
    return model

# Verify the loaded model's signatures (for debugging)
loaded = tf.saved_model.load(MODEL_PATH)
print("Available Signatures:", list(loaded.signatures.keys()))