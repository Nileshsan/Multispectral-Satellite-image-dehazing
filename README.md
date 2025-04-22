# 🛰️ X-Dehazed: Hybrid GAN-Based Multispectral Satellite Image Dehazing

A novel deep learning framework for dehazing multispectral satellite images by sequentially combining **CycleGAN** and **Pix2Pix GAN**, with intelligent post-analysis using a **local LLM (LLaMA)**. This approach enhances visibility and structural clarity of satellite images affected by atmospheric haze, making it suitable for real-world applications like environmental monitoring, urban planning, and disaster response.

---

## 📌 Key Features

- 🌫️ **Hybrid GAN Pipeline**: CycleGAN for unpaired image translation + Pix2Pix for paired refinement.
- 🧠 **LLM Integration**: Utilizes LLaMA to provide automated alerts and descriptive analysis.
- 🖼️ **High-Resolution Outputs**: Incorporates perceptual loss & Laplacian pyramid for enhanced clarity.
- 🌐 **Web Interface**: User-friendly Django web app for image upload, processing, and PDF report generation.

---

## 🚀 Technologies Used

| Category       | Tools & Frameworks                          |
|----------------|---------------------------------------------|
| Frontend       | HTML, CSS, Bootstrap, JavaScript            |
| Backend        | Python, Django                              |
| DL Frameworks  | TensorFlow, Keras                           |
| Models         | Pix2Pix, CycleGAN, U-Net                    |
| LLM Integration| LLaMA (local deployment)                    |
| Image Handling | OpenCV, Keras Image Preprocessing           |
| UI/UX          | Django Templates + JS Interactivity         |

---

## 🧠 System Architecture

1. **Input**: Hazy JPG/RGB satellite image
2. **Preprocessing**: Resize to 256x256, normalize, spectral alignment
3. **Dehazing Flow**:
    - `CycleGAN` for unpaired translation
    - `Pix2Pix` for paired refinement
4. **Postprocessing**:
    - Denormalize, upscale using Laplacian Pyramid
    - Analyze using **LLaMA** to generate insights
5. **Output**: Dehazed image + PDF report (alerts, analysis)

---

## 📂 Dataset

- **Custom Dataset**: Hazy and clear multispectral satellite images
- **Additional Datasets**: 
  - [I-HAZE](http://cs-chan.com/downloads/ihaze_dataset.zip)
  - [O-HAZE](http://cs-chan.com/downloads/ohaze_dataset.zip)
- Supports both **paired** and **unpaired** image formats

---

## 📈 Results

| Metric   | Value (Hybrid Pipeline) |
|----------|-------------------------|
| PSNR     | ↑ Improved significantly over baselines |
| SSIM     | ↑ Better structural consistency |
| FID      | ↓ Lower than single-model approaches |
| Loss     | Final: ~0.29 after 200 epochs |

### 🔍 Visual Results
- Clearer textures
- Sharper edges
- Realistic color balance
- Side-by-side comparisons with original hazy images

---

## 🖥️ Web Application

### Features:
- Upload satellite image (JPG/RGB)
- Select model (CycleGAN, Pix2Pix)
- View real-time results
- Download dehazed image + report

### Screens:
- Home/Login
- Upload & Result Preview
- Dehazed Image Display
- PDF Report with LLM Summary

---

## 📜 How to Run Locally

```bash
git clone https://github.com/Nileshsan/Multispectral-Satellite-image-dehazing.git
cd Multispectral-Satellite-image-dehazing
pip install -r requirements.txt

# Run Django server
python manage.py runserver
