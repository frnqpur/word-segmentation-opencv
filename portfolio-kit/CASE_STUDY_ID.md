# Studi Kasus — Word Segmentation menggunakan OpenCV

## Ringkasan Project
Project ini adalah implementasi computer vision berbasis OpenCV untuk melakukan segmentasi area tulisan tangan dari sebuah gambar. Sistem memproses gambar melalui tahapan preprocessing, thresholding, morphological dilation, contour detection, bounding-box visualization, dan crop kandidat kata atau komponen tulisan.

Project ini dibuat sebagai demonstrasi image processing, bukan sebagai sistem OCR atau handwriting recognition.

## Latar Belakang
Dalam pengolahan citra dokumen atau tulisan tangan, salah satu tahap penting sebelum analisis lanjutan adalah memisahkan area teks dari background. Segmentasi ini membantu mengidentifikasi bagian gambar yang mengandung tulisan sehingga dapat divisualisasikan atau diproses lebih lanjut.

## Tujuan
Tujuan project ini adalah membangun pipeline sederhana yang mampu:

- Menerima input gambar tulisan tangan.
- Menampilkan gambar asli.
- Melakukan preprocessing gambar.
- Menghasilkan threshold image.
- Mengelompokkan area teks menggunakan dilation.
- Mendeteksi kontur teks menggunakan OpenCV.
- Menampilkan bounding boxes.
- Mengekstrak crop kandidat kata atau komponen tulisan.

## Tech Stack

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| OpenCV | Image processing dan contour detection |
| NumPy | Manipulasi array gambar |
| Pillow | Membaca file gambar upload |
| Streamlit | Demo web interaktif |
| Matplotlib | Visualisasi opsional |

## Pipeline Image Processing

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
Output utama project ini meliputi:

- Original image preview.
- Grayscale image.
- Threshold image.
- Bounding-box visualization.
- Segmented word/component crops.

## Tantangan Teknis
Beberapa tantangan dalam project ini:

- Kualitas hasil dipengaruhi oleh pencahayaan gambar.
- Nilai threshold tidak selalu cocok untuk semua gambar.
- Ukuran kernel dilation perlu disesuaikan dengan jarak antar huruf dan kata.
- Noise pada background dapat menghasilkan kontur tambahan.
- Project belum melakukan OCR, sehingga tidak membaca tulisan menjadi teks digital.

## Solusi
Untuk membuat demo lebih fleksibel, parameter seperti threshold value, dilation kernel, dan minimum contour area dapat dibuat adjustable melalui sidebar Streamlit. Hal ini membantu pengguna menyesuaikan proses segmentasi berdasarkan kualitas gambar.

## Hasil
Project berhasil menunjukkan pipeline computer vision dasar untuk mendeteksi area tulisan tangan dan menampilkan hasil segmentasi secara visual melalui bounding boxes dan crop kandidat kata/komponen.

## Limitasi
Project ini memiliki limitasi berikut:

- Tidak melakukan OCR.
- Tidak mengenali karakter atau kata.
- Tidak menggunakan machine learning atau deep learning.
- Hasil segmentasi bergantung pada kualitas gambar input.
- Belum dirancang untuk dokumen kompleks atau produksi skala besar.

## Nilai Portfolio
Project ini menunjukkan kemampuan dalam:

- Computer vision fundamental.
- OpenCV image processing.
- Preprocessing pipeline.
- Contour-based segmentation.
- Visual debugging.
- Streamlit demo development.
- Dokumentasi project yang jelas dan recruiter-friendly.
