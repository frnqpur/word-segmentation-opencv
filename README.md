# Word Segmentation using OpenCV

## Overview
Word Segmentation using OpenCV is a computer vision project that demonstrates a classical image processing pipeline for detecting handwritten text regions and extracting segmented word/component crops from an input image.

The project uses OpenCV-based preprocessing, thresholding, morphological dilation, contour detection, bounding-box visualization, and a Streamlit demo interface.

> Note: This project is not an OCR system. It does not recognize or convert handwriting into digital text.

## Features

- Upload handwritten text image.
- Display original image.
- Show grayscale preprocessing result.
- Show binary threshold result.
- Apply morphological dilation.
- Detect contours using OpenCV.
- Draw bounding boxes around detected text regions.
- Extract segmented word/component crops.
- Display results in a Streamlit web demo.
- Handle invalid image input gracefully.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Image preprocessing and contour detection |
| NumPy | Image array manipulation |
| Pillow | Image upload handling |
| Streamlit | Interactive web demo |
| Matplotlib | Optional visualization support |

## Image Processing Pipeline

```txt
Input Image
→ RGB Conversion
→ Grayscale Conversion
→ Binary Inverse Thresholding
→ Morphological Dilation
→ Contour Detection
→ Bounding Box Sorting
→ Segmented Crop Extraction
→ Streamlit Visualization
```

## Demo Screenshots

| Step | Screenshot |
|---|---|
| Upload Screen | `screenshots/01-upload-screen.png` |
| Original Image | `screenshots/02-original-image.png` |
| Preprocessing Result | `screenshots/03-threshold-preprocessing-result.png` |
| Bounding Box Output | `screenshots/04-bounding-box-output.png` |
| Segmented Word Crops | `screenshots/05-segmented-words-output.png` |

## Local Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Streamlit App

```bash
streamlit run app.py
```

## requirements.txt

```txt
opencv-python-headless>=4.8,<5
numpy>=1.24,<3
pillow>=10,<12
streamlit>=1.30,<2
matplotlib>=3.7,<4
```

## Recommended Sample Image
Use a clean handwritten image with:

- Clear contrast between text and background.
- Bright background.
- No private or sensitive information.
- No GPS/EXIF metadata.
- No faces, addresses, phone numbers, signatures, or official documents.

## Limitations

- This project does not perform OCR.
- It does not recognize characters or words.
- It does not use machine learning or deep learning.
- Results depend on lighting, contrast, threshold value, and dilation kernel size.
- It is designed for portfolio and educational demonstration purposes.

## Portfolio Value
This project demonstrates practical skills in computer vision, OpenCV image preprocessing, contour detection, visual segmentation, and simple interactive application deployment using Streamlit.
