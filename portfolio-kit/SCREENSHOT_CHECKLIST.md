# Screenshot Checklist — Word Segmentation Demo

## Purpose
This checklist defines the required screenshots for presenting the Streamlit Word Segmentation demo in a GitHub README, portfolio website, or recruiter-facing case study.

## Required Screenshots

| No | File Name | Caption ID | Caption EN | Alt Text | Sample Image Standard |
|---:|---|---|---|---|---|
| 1 | `01-upload-screen.png` | Tampilan awal demo Streamlit untuk mengunggah gambar tulisan tangan. | Initial Streamlit demo screen for uploading a handwritten text image. | Upload screen of the Streamlit word segmentation demo with image upload control. | Menampilkan judul aplikasi, deskripsi singkat, dan upload widget. Jangan tampilkan path lokal atau data pribadi. |
| 2 | `02-original-image-1.png` / `02-original-image-2.png` | Gambar asli yang diunggah sebelum proses segmentasi dilakukan. | Original uploaded image before the segmentation process. | Original handwritten text image displayed in the Streamlit demo. | Gunakan gambar sample bersih, jelas, dan tanpa metadata EXIF/GPS. |
| 3 | `03-threshold-preprocessing-result-1.png` / `03-threshold-preprocessing-result-2.png` | Hasil preprocessing berupa grayscale dan binary threshold untuk memisahkan area teks dari background. | Preprocessing result showing grayscale and binary threshold output to separate text regions from the background. | Grayscale and threshold preprocessing result for handwritten text segmentation. | Hasil harus memiliki kontras jelas antara tulisan dan background. |
| 4 | `04-bounding-box-output.png` | Hasil deteksi bounding box pada area tulisan menggunakan contour detection OpenCV. | Bounding box detection result on handwritten text regions using OpenCV contour detection. | Handwritten text image with detected bounding boxes around text components. | Bounding boxes harus terlihat jelas dan cukup rapi untuk ditampilkan ke recruiter. |
| 5 | `05-segmented-words-output-1.png` / `05-segmented-words-output-2.png` / `05-segmented-words-output-3.png` | Hasil crop kandidat kata atau komponen tulisan yang terdeteksi dari proses segmentasi. | Segmented word or text-component crop outputs detected from the segmentation process. | Grid of segmented handwritten word or component crops from the uploaded image. | Tampilkan crop representatif. Hindari crop kosong, noise, atau terlalu kecil. |

## Recommended Folder Structure

```txt
screenshots/
├── 01-upload-screen.png
├── 02-original-image-1.png
├── 02-original-image-2.png
├── 03-threshold-preprocessing-result-1.png
├── 03-threshold-preprocessing-result-2.png
├── 04-bounding-box-output.png
├── 05-segmented-words-output-1.png
├── 05-segmented-words-output-2.png
└── 05-segmented-words-output-3.png
```

## General Screenshot Standards

- Use `.png` format.
- Minimum width: 1280 px.
- Use consistent browser zoom.
- Avoid showing browser bookmarks, email, local file paths, or notifications.
- Use the same sample image throughout the screenshot sequence.
- Remove EXIF/GPS metadata from sample images.
- Do not include sensitive personal data.
- Do not label the output as OCR.

## Recommended README Caption — Indonesia

```md
## Demo Screenshots

1. **Upload Screen** — Tampilan awal aplikasi Streamlit untuk mengunggah gambar tulisan tangan.
2. **Original Image** — Gambar asli sebelum proses image processing dilakukan.
3. **Preprocessing Result** — Hasil grayscale dan binary threshold sebagai tahap awal segmentasi.
4. **Bounding Box Output** — Visualisasi area tulisan yang terdeteksi menggunakan contour detection.
5. **Segmented Word Crops** — Crop kandidat kata atau komponen tulisan hasil segmentasi.
```

## Recommended README Caption — English

```md
## Demo Screenshots

1. **Upload Screen** — Initial Streamlit application screen for uploading a handwritten text image.
2. **Original Image** — Original image before the image processing pipeline is applied.
3. **Preprocessing Result** — Grayscale and binary threshold outputs used as the initial segmentation stage.
4. **Bounding Box Output** — Visualization of detected handwritten text regions using contour detection.
5. **Segmented Word Crops** — Cropped word or text-component candidates generated from the segmentation process.
```
