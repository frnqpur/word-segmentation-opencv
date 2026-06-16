# Case Study — Word Segmentation using OpenCV

## Project Summary
This project implements an OpenCV-based computer vision pipeline for segmenting handwritten text regions from an image. The system processes the image through preprocessing, thresholding, morphological dilation, contour detection, bounding-box visualization, and segmented word/component crop extraction.

This project is designed as an image processing demonstration, not as an OCR or handwriting recognition system.

## Background
In document image processing and handwritten text analysis, text-region segmentation is an important early-stage process. Before text can be analyzed further, the system needs to separate potential text regions from the image background.

## Objective
The objective of this project is to build a simple pipeline that can:

- Accept a handwritten image input.
- Display the original image.
- Apply image preprocessing.
- Generate a threshold image.
- Group text regions using dilation.
- Detect contours using OpenCV.
- Display bounding boxes.
- Extract segmented word or text-component crops.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Image processing and contour detection |
| NumPy | Image array manipulation |
| Pillow | Uploaded image handling |
| Streamlit | Interactive web demo |
| Matplotlib | Optional visualization support |

## Image Processing Pipeline

```txt
Upload image
→ Convert image to RGB
→ Convert RGB to grayscale
→ Apply binary inverse thresholding
→ Apply morphological dilation
→ Detect contours
→ Sort bounding boxes
→ Draw bounding boxes
→ Crop segmented word/component regions
→ Display result in Streamlit
```

## Output
The main outputs include:

- Original image preview.
- Grayscale image.
- Threshold image.
- Bounding-box visualization.
- Segmented word/component crops.

## Technical Challenges
Key technical challenges include:

- Segmentation quality depends on image lighting.
- A fixed threshold value may not work for every image.
- Dilation kernel size must be adjusted based on letter and word spacing.
- Background noise may create additional contours.
- The project does not perform OCR or convert handwriting into digital text.

## Solution
To make the demo more flexible, parameters such as threshold value, dilation kernel size, and minimum contour area can be adjusted through the Streamlit sidebar. This allows users to tune the segmentation process based on the uploaded image quality.

## Result
The project successfully demonstrates a classical computer vision workflow for detecting handwritten text regions and visualizing segmentation results through bounding boxes and segmented word/component crops.

## Limitation
This project has the following limitations:

- It does not perform OCR.
- It does not recognize characters or words.
- It does not use machine learning or deep learning.
- Segmentation results depend on input image quality.
- It is not designed for complex document processing or production-scale usage.

## Portfolio Value
This project demonstrates practical skills in:

- Computer vision fundamentals.
- OpenCV image processing.
- Image preprocessing pipeline design.
- Contour-based segmentation.
- Visual debugging.
- Streamlit demo development.
- Clear recruiter-friendly technical documentation.
