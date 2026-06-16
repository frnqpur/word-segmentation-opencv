"""
Streamlit Demo: Word Segmentation using OpenCV

Purpose:
- Upload an image
- Show original image
- Show preprocessing results
- Show bounding boxes
- Show segmented word/component crops

Important:
This demo performs image segmentation only. It does not perform OCR or handwriting recognition.
"""

from __future__ import annotations

import io
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple

import cv2
import numpy as np
from PIL import Image, UnidentifiedImageError
import streamlit as st


@dataclass
class SegmentationResult:
    original_rgb: np.ndarray
    resized_rgb: np.ndarray
    grayscale: np.ndarray
    threshold: np.ndarray
    line_dilation: np.ndarray
    word_dilation: np.ndarray
    line_boxes_image: np.ndarray
    word_boxes_image: np.ndarray
    crops: List[np.ndarray]
    line_boxes: List[Tuple[int, int, int, int]]
    word_boxes: List[Tuple[int, int, int, int]]


st.set_page_config(
    page_title="Word Segmentation Demo",
    page_icon="📝",
    layout="wide",
)


# -----------------------------
# Utility functions
# -----------------------------

def pil_to_rgb_array(image: Image.Image) -> np.ndarray:
    """Convert PIL image to RGB NumPy array."""
    return np.array(image.convert("RGB"))


def resize_if_needed(image_rgb: np.ndarray, max_width: int = 1000) -> np.ndarray:
    """Resize image proportionally when it is wider than max_width."""
    height, width = image_rgb.shape[:2]
    if width <= max_width:
        return image_rgb.copy()

    scale = max_width / float(width)
    new_height = int(height * scale)
    return cv2.resize(image_rgb, (max_width, new_height), interpolation=cv2.INTER_AREA)


def find_external_contours(binary_image: np.ndarray) -> List[np.ndarray]:
    """OpenCV version-safe contour detection."""
    contours_result = cv2.findContours(
        binary_image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    if len(contours_result) == 2:
        contours, _ = contours_result
    else:
        _, contours, _ = contours_result
    return list(contours)


def draw_boxes(
    image_rgb: np.ndarray,
    boxes: List[Tuple[int, int, int, int]],
    thickness: int = 2,
) -> np.ndarray:
    """Draw bounding boxes on a copy of the RGB image."""
    output = image_rgb.copy()
    for x, y, w, h in boxes:
        # OpenCV draws in BGR-style tuple order, but green is the same positionally.
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), thickness)
    return output


def safe_crop(image_rgb: np.ndarray, box: Tuple[int, int, int, int], padding: int = 2) -> np.ndarray:
    """Crop a region safely with optional padding."""
    x, y, w, h = box
    height, width = image_rgb.shape[:2]

    x1 = max(x - padding, 0)
    y1 = max(y - padding, 0)
    x2 = min(x + w + padding, width)
    y2 = min(y + h + padding, height)

    return image_rgb[y1:y2, x1:x2]


def process_image(
    image_rgb: np.ndarray,
    max_width: int,
    threshold_value: int,
    line_kernel_width: int,
    word_kernel_width: int,
    min_line_width: int,
    min_line_height: int,
    min_word_width: int,
    min_word_height: int,
    max_crops: int,
) -> SegmentationResult:
    """Run OpenCV preprocessing and contour-based segmentation."""
    if image_rgb.ndim != 3 or image_rgb.shape[2] != 3:
        raise ValueError("Image must be a valid RGB image.")

    resized_rgb = resize_if_needed(image_rgb, max_width=max_width)

    # 1. Grayscale
    grayscale = cv2.cvtColor(resized_rgb, cv2.COLOR_RGB2GRAY)

    # 2. Binary inverse thresholding
    _, threshold = cv2.threshold(
        grayscale,
        threshold_value,
        255,
        cv2.THRESH_BINARY_INV,
    )

    # 3. Dilation for line grouping
    line_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (line_kernel_width, 3))
    line_dilation = cv2.dilate(threshold, line_kernel, iterations=1)

    line_contours = find_external_contours(line_dilation)
    line_boxes = [cv2.boundingRect(contour) for contour in line_contours]
    line_boxes = [
        box for box in line_boxes
        if box[2] >= min_line_width and box[3] >= min_line_height
    ]
    line_boxes = sorted(line_boxes, key=lambda box: (box[1], box[0]))

    # 4. Dilation for word/component candidates
    word_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (word_kernel_width, 3))
    word_dilation = cv2.dilate(threshold, word_kernel, iterations=1)

    # Detect word/component boxes inside each detected line region.
    word_boxes: List[Tuple[int, int, int, int]] = []
    for line_x, line_y, line_w, line_h in line_boxes:
        roi = word_dilation[line_y:line_y + line_h, line_x:line_x + line_w]
        roi_contours = find_external_contours(roi)

        local_boxes = [cv2.boundingRect(contour) for contour in roi_contours]
        local_boxes = [
            (line_x + x, line_y + y, w, h)
            for x, y, w, h in local_boxes
            if w >= min_word_width and h >= min_word_height
        ]
        local_boxes = sorted(local_boxes, key=lambda box: box[0])
        word_boxes.extend(local_boxes)

    # Fallback: if no line boxes are detected, attempt global word/component detection.
    if not line_boxes:
        global_contours = find_external_contours(word_dilation)
        word_boxes = [cv2.boundingRect(contour) for contour in global_contours]
        word_boxes = [
            box for box in word_boxes
            if box[2] >= min_word_width and box[3] >= min_word_height
        ]
        word_boxes = sorted(word_boxes, key=lambda box: (box[1], box[0]))

    line_boxes_image = draw_boxes(resized_rgb, line_boxes, thickness=2)
    word_boxes_image = draw_boxes(resized_rgb, word_boxes, thickness=2)

    crops = [safe_crop(resized_rgb, box) for box in word_boxes[:max_crops]]

    return SegmentationResult(
        original_rgb=image_rgb,
        resized_rgb=resized_rgb,
        grayscale=grayscale,
        threshold=threshold,
        line_dilation=line_dilation,
        word_dilation=word_dilation,
        line_boxes_image=line_boxes_image,
        word_boxes_image=word_boxes_image,
        crops=crops,
        line_boxes=line_boxes,
        word_boxes=word_boxes,
    )


def read_uploaded_image(uploaded_file) -> Image.Image:
    """Read uploaded image with clear error handling."""
    try:
        return Image.open(uploaded_file)
    except UnidentifiedImageError as exc:
        raise ValueError("Uploaded file is not a valid image. Please upload PNG, JPG, or JPEG.") from exc
    except Exception as exc:
        raise ValueError(f"Unable to read image file: {exc}") from exc


def image_to_download_bytes(image_rgb: np.ndarray) -> bytes:
    """Convert RGB image array to PNG bytes for download."""
    image = Image.fromarray(image_rgb)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("📝 Word Segmentation Demo using OpenCV")
st.caption(
    "Upload an image and visualize grayscale preprocessing, thresholding, dilation, "
    "bounding boxes, and segmented word/component crops. This demo is for segmentation only, not OCR."
)

with st.sidebar:
    st.header("⚙️ Segmentation Settings")

    max_width = st.slider("Max image width", min_value=500, max_value=1600, value=1000, step=100)
    threshold_value = st.slider("Threshold value", min_value=0, max_value=255, value=80, step=1)

    st.subheader("Dilation Kernels")
    line_kernel_width = st.slider("Line grouping kernel width", min_value=5, max_value=151, value=85, step=2)
    word_kernel_width = st.slider("Word/component kernel width", min_value=1, max_value=75, value=15, step=2)

    st.subheader("Filtering")
    min_line_width = st.slider("Minimum line width", min_value=1, max_value=500, value=30, step=1)
    min_line_height = st.slider("Minimum line height", min_value=1, max_value=100, value=8, step=1)
    min_word_width = st.slider("Minimum word/component width", min_value=1, max_value=150, value=5, step=1)
    min_word_height = st.slider("Minimum word/component height", min_value=1, max_value=80, value=5, step=1)

    max_crops = st.slider("Maximum crops to display", min_value=5, max_value=100, value=40, step=5)

    st.info(
        "Tip: If too many boxes appear, increase minimum width/height or adjust threshold. "
        "If boxes are merged, reduce kernel width."
    )

uploaded_file = st.file_uploader(
    "Upload image",
    type=["png", "jpg", "jpeg"],
    help="Use a clear handwritten or text image for best results.",
)

st.markdown("### Optional Sample Image")
st.write(
    "A sample image can be provided at `assets/sample-image.jpg`. "
    "The app also supports legacy `sample.jpg` in the project root. "
    "The app will still work without a sample image."
)

sample_image = None
sample_image_label = None
for sample_path in [Path("assets/sample-image.jpg"), Path("sample.jpg")]:
    try:
        if sample_path.exists():
            sample_image = Image.open(sample_path)
            sample_image_label = str(sample_path).replace("\\", "/")
            break
    except Exception:
        sample_image = None
        sample_image_label = None

use_sample = False
if sample_image is not None:
    use_sample = st.button(f"Use {sample_image_label}")

if uploaded_file is None and not use_sample:
    st.warning("Please upload an image to start the segmentation demo.")
    st.stop()

try:
    pil_image = sample_image if use_sample else read_uploaded_image(uploaded_file)
    image_rgb = pil_to_rgb_array(pil_image)

    result = process_image(
        image_rgb=image_rgb,
        max_width=max_width,
        threshold_value=threshold_value,
        line_kernel_width=line_kernel_width,
        word_kernel_width=word_kernel_width,
        min_line_width=min_line_width,
        min_line_height=min_line_height,
        min_word_width=min_word_width,
        min_word_height=min_word_height,
        max_crops=max_crops,
    )

except ValueError as exc:
    st.error(str(exc))
    st.stop()
except cv2.error as exc:
    st.error("OpenCV failed to process this image. Try another image or adjust the settings.")
    st.code(str(exc))
    st.stop()
except Exception as exc:
    st.error("Unexpected error occurred while processing the image.")
    st.code(str(exc))
    st.stop()

# Summary metrics
metric_col1, metric_col2, metric_col3 = st.columns(3)
metric_col1.metric("Detected Lines", len(result.line_boxes))
metric_col2.metric("Detected Word/Component Boxes", len(result.word_boxes))
metric_col3.metric("Displayed Crops", len(result.crops))

# Original image
st.markdown("## 1. Original Image")
st.image(result.resized_rgb, caption="Original / resized image", use_container_width=True)

# Preprocessing result
st.markdown("## 2. Preprocessing Result")
pre_col1, pre_col2, pre_col3 = st.columns(3)
with pre_col1:
    st.image(result.grayscale, caption="Grayscale", use_container_width=True, clamp=True)
with pre_col2:
    st.image(result.threshold, caption="Binary Inverse Threshold", use_container_width=True, clamp=True)
with pre_col3:
    st.image(result.line_dilation, caption="Line Dilation", use_container_width=True, clamp=True)

st.image(result.word_dilation, caption="Word / Component Dilation", use_container_width=True, clamp=True)

# Bounding boxes
st.markdown("## 3. Bounding Boxes")
box_col1, box_col2 = st.columns(2)
with box_col1:
    st.image(result.line_boxes_image, caption="Detected Text Line Boxes", use_container_width=True)
with box_col2:
    st.image(result.word_boxes_image, caption="Detected Word / Component Boxes", use_container_width=True)

st.download_button(
    label="Download bounding-box result as PNG",
    data=image_to_download_bytes(result.word_boxes_image),
    file_name="word_segmentation_bounding_boxes.png",
    mime="image/png",
)

# Crops
st.markdown("## 4. Segmented Word / Component Crops")
if not result.crops:
    st.warning(
        "No crops were detected. Try changing the threshold, reducing kernel width, "
        "or lowering minimum width/height filters."
    )
else:
    crop_columns = st.columns(4)
    for index, crop in enumerate(result.crops, start=1):
        with crop_columns[(index - 1) % 4]:
            st.image(crop, caption=f"Crop {index}", use_container_width=True)

# Technical notes
with st.expander("Technical Notes"):
    st.markdown(
        """
        **Processing pipeline:**
        1. Convert uploaded image to RGB.
        2. Resize image if it exceeds the selected maximum width.
        3. Convert image to grayscale.
        4. Apply binary inverse thresholding.
        5. Apply morphological dilation for text-line grouping.
        6. Detect contours and sort bounding boxes.
        7. Apply second dilation for word/component candidates.
        8. Crop detected word/component regions.

        **Limitation:** This app performs image segmentation only. It does not recognize, classify, or read the text.
        """
    )
