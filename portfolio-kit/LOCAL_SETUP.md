# Local Setup Guide — Word Segmentation Streamlit Demo

## Purpose
This guide explains how to run the Word Segmentation Streamlit demo locally.

## Requirements
Install the following before running the project:

- Python 3.10 or 3.11 recommended.
- pip.
- Git, optional but recommended.
- A terminal or command prompt.

## Recommended Folder Structure

```txt
word-segmentation-demo/
├── app.py
├── requirements.txt
├── README_DEPLOY.md
└── screenshots/
```

## Step 1 — Create Virtual Environment

```bash
python -m venv .venv
```

## Step 2 — Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4 — Run Streamlit App

```bash
streamlit run app.py
```

## Step 5 — Open Browser
Streamlit usually opens automatically. If not, open the local URL shown in the terminal, usually:

```txt
http://localhost:8501
```

## Step 6 — Test the Demo
Use a clean handwritten text image and verify that the app displays:

- Original image.
- Grayscale result.
- Threshold result.
- Bounding-box output.
- Segmented word/component crops.

## Troubleshooting

### Issue: OpenCV installation problem
Use `opencv-python-headless` instead of `opencv-python` for Streamlit/cloud environments.

### Issue: Image cannot be processed
Check that the uploaded file is a valid image format such as:

```txt
PNG
JPG
JPEG
WEBP
```

### Issue: No word crops detected
Try adjusting:

- Threshold value.
- Line dilation kernel.
- Word dilation kernel.
- Minimum contour area.

Also ensure the sample image has clear handwriting and good contrast.

## Local Acceptance Criteria
The local setup is successful if:

- Streamlit app runs without error.
- Image upload works.
- Preprocessing output appears.
- Bounding boxes are generated.
- Segmented crops are displayed.
