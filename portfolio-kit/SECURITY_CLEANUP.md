# Security Cleanup Checklist — Word Segmentation Portfolio

## Purpose
This checklist helps ensure that the project is safe to publish on GitHub, Streamlit, or a portfolio website.

## Files to Review Before Upload
Check all files before publishing:

```txt
source code
notebooks
sample images
screenshots
README files
case study files
requirements.txt
```

## Do Not Upload
Avoid uploading:

- `.env` files.
- API keys.
- Credentials.
- Private images.
- Images with GPS/EXIF metadata.
- Personal documents.
- Screenshots containing names, addresses, emails, phone numbers, or locations.
- Notebook checkpoint folders.
- System files such as `.DS_Store`.
- Large unused raw files.

## Sensitive Image Cleanup
Before using a sample image:

- Remove EXIF metadata.
- Remove GPS metadata.
- Ensure no private information is visible.
- Ensure no face, address, phone number, ID number, signature, or confidential document is shown.
- Use a clean test image if possible.

## Recommended `.gitignore`

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual environments
.venv/
venv/
env/

# Environment files
.env
.env.*

# Jupyter
.ipynb_checkpoints/

# OS files
.DS_Store
Thumbs.db

# Local outputs
outputs/
crops/
temp/

# Large/private media
private/
raw-images/
```

## Safe Files to Publish
Generally safe to publish after review:

```txt
app.py
requirements.txt
README.md
README_DEPLOY.md
screenshots/*.png
CASE_STUDY_ID.md
CASE_STUDY_EN.md
CV_BULLETS.md
```

## Claims Safety
Use accurate project descriptions:

Safe:

```txt
Computer Vision
OpenCV
Image Processing
Word Segmentation
Contour Detection
Bounding Box Visualization
Segmented Crops
```

Avoid unless implemented:

```txt
OCR
Text Recognition
AI Handwriting Recognition
Machine Learning Model
Deep Learning Model
Production OCR System
```

## Final Security Acceptance Criteria
The project is ready for public upload if:

- No private files are included.
- No `.env` file is included.
- No credentials are visible.
- Sample images are non-sensitive.
- Image metadata is removed.
- Screenshots do not expose private data.
- Claims are technically accurate.
- README clearly states that the project is not OCR.
