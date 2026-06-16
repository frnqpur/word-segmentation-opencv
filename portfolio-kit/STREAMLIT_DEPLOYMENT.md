# Streamlit Deployment Guide

## Recommended Deployment Option
Use **Streamlit Community Cloud** for this portfolio demo.

This project does not need cPanel because Streamlit apps are better deployed through platforms that support Python web apps directly.

## Required Files
At minimum, the repository should include:

```txt
app.py
requirements.txt
README.md
screenshots/
```

## requirements.txt
Use:

```txt
opencv-python-headless>=4.8,<5
numpy>=1.24,<3
pillow>=10,<12
streamlit>=1.30,<2
matplotlib>=3.7,<4
```

## Deployment Steps — Streamlit Community Cloud

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select the branch.
5. Set the main file path:

```txt
app.py
```

6. Deploy the app.
7. Test image upload and segmentation output.

## Repository Structure for Deployment

```txt
word-segmentation-streamlit/
├── app.py
├── requirements.txt
├── README.md
├── README_DEPLOY.md
└── screenshots/
```

## Deployment Notes

- Use `opencv-python-headless`, not `opencv-python`, for cloud deployment.
- Do not upload private images.
- Do not upload images with EXIF/GPS metadata.
- Do not include `.env` files.
- Do not include notebook checkpoint files.
- Keep demo sample images clean and non-sensitive.

## Post-Deployment Testing Checklist

| Test Item | Expected Result |
|---|---|
| App loads | Streamlit page opens successfully |
| Upload works | Image can be uploaded |
| Original image appears | Uploaded image is displayed |
| Preprocessing appears | Grayscale and threshold outputs are shown |
| Bounding boxes appear | Detected boxes are drawn on image |
| Crops appear | Segmented word/component crops are displayed |
| Error handling works | Invalid input shows friendly message |

## Recommended Portfolio Link Label
Use:

```txt
Live Demo — Word Segmentation using OpenCV
```

## Deployment Limitation Statement
This demo is designed for portfolio demonstration and educational purposes. It is not a production OCR system and does not convert handwriting into digital text.
