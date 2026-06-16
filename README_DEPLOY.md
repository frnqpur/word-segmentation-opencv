# Word Segmentation Streamlit Demo

**Live Demo:** https://word-segmentation-opencv-vwxn5bwzguagidn8qdsqcq.streamlit.app/  
**GitHub Repository:** https://github.com/frnqpur/word-segmentation-opencv

Demo ini menampilkan pipeline **Word Segmentation menggunakan OpenCV**. Aplikasi menerima upload image, menampilkan original image, preprocessing result, bounding boxes, dan segmented word/component crops.

> Catatan penting: demo ini bukan OCR dan tidak membaca tulisan menjadi teks digital. Fokusnya adalah segmentasi visual berbasis classical image processing.

---

## 1. Fitur Demo

- Upload image format PNG, JPG, atau JPEG.
- Tampilkan original/resized image.
- Tampilkan preprocessing result:
  - Grayscale
  - Binary inverse threshold
  - Line dilation
  - Word/component dilation
- Tampilkan bounding boxes:
  - Detected text line boxes
  - Detected word/component boxes
- Tampilkan segmented word/component crops.
- Download hasil bounding box sebagai PNG.
- Graceful error handling untuk file rusak, format tidak valid, dan error OpenCV.
- Sample image optional melalui file `assets/sample-image.jpg`.
- Tidak membutuhkan cPanel.

---

## 2. Struktur File

```txt
word-segmentation-demo/
├── app.py
├── requirements.txt
├── README_DEPLOY.md
└── assets/sample-image.jpg              # optional, tidak wajib
```

---

## 3. Dependency

Project menggunakan dependency berikut:

```txt
opencv-python-headless
numpy
pillow
streamlit
matplotlib
```

`opencv-python-headless` digunakan agar lebih ringan dan lebih cocok untuk deployment server/cloud dibanding `opencv-python` biasa.

---

## 4. Local Setup

### 4.1 Buat virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4.2 Install dependency

```bash
pip install -r requirements.txt
```

### 4.3 Jalankan Streamlit app

```bash
streamlit run app.py
```

Setelah itu buka URL lokal yang muncul di terminal, biasanya:

```txt
http://localhost:8501
```

---

## 5. Optional Sample Image

Jika ingin menampilkan tombol sample image, tambahkan gambar bernama:

```txt
assets/sample-image.jpg
```

Letakkan di folder `assets/` dengan nama `sample-image.jpg`.

Jika `assets/sample-image.jpg` tidak tersedia, aplikasi tetap berjalan normal menggunakan fitur upload image.

Sebelum menggunakan sample image publik, pastikan metadata sensitif sudah dihapus, terutama metadata lokasi/GPS.

---

## 6. Deployment ke Streamlit Community Cloud

### 6.1 Siapkan repository GitHub

Upload file berikut ke repository:

```txt
app.py
requirements.txt
README_DEPLOY.md
assets/sample-image.jpg          # optional
```

### 6.2 Buka Streamlit Community Cloud

1. Login ke Streamlit Community Cloud.
2. Pilih **New app**.
3. Hubungkan repository GitHub.
4. Pilih branch yang digunakan, misalnya `main`.
5. Isi main file path:

```txt
app.py
```

6. Klik **Deploy**.

---

## 7. Deployment ke Hugging Face Spaces

Alternatif lain adalah menggunakan Hugging Face Spaces.

1. Buat Space baru.
2. Pilih SDK: **Streamlit**.
3. Upload file:

```txt
app.py
requirements.txt
README_DEPLOY.md
```

4. Commit file.
5. Space akan otomatis menjalankan aplikasi.

---

## 8. Parameter yang Bisa Diatur di Sidebar

| Parameter | Fungsi |
|---|---|
| Max image width | Resize image agar proses lebih ringan |
| Threshold value | Mengontrol binary inverse thresholding |
| Line grouping kernel width | Mengatur penggabungan area menjadi baris teks |
| Word/component kernel width | Mengatur deteksi kandidat kata/komponen |
| Minimum line width/height | Filter noise untuk line detection |
| Minimum word width/height | Filter noise untuk word/component detection |
| Maximum crops to display | Membatasi jumlah crop agar UI tetap ringan |

---

## 9. Pipeline Image Processing

```txt
Upload image
→ Convert to RGB
→ Resize if needed
→ Convert to grayscale
→ Binary inverse thresholding
→ Morphological dilation for line grouping
→ Contour detection for text lines
→ Bounding box sorting by Y position
→ Morphological dilation for word/component candidates
→ Contour detection inside each line region
→ Bounding box sorting by X position
→ Crop segmented word/component regions
→ Display result in Streamlit
```

---

## 10. Error Handling

Aplikasi menangani beberapa kondisi error:

- File upload bukan image valid.
- File image rusak atau tidak bisa dibaca.
- Error dari OpenCV saat preprocessing.
- Tidak ada contour/crop yang berhasil terdeteksi.
- Sample image tidak tersedia.

Jika hasil bounding box terlalu banyak atau tidak akurat, ubah parameter di sidebar.

---

## 11. Limitation

- Demo ini tidak melakukan OCR.
- Demo ini tidak membaca tulisan menjadi teks.
- Hasil segmentasi sangat bergantung pada kualitas gambar, pencahayaan, noise, threshold value, dan ukuran dilation kernel.
- Project ini menggunakan classical image processing, bukan machine learning atau deep learning.

---

## 12. Acceptance Criteria

Demo dianggap siap digunakan untuk portfolio jika:

- App bisa dijalankan dengan `streamlit run app.py`.
- User bisa upload image PNG/JPG/JPEG.
- Original image tampil dengan benar.
- Grayscale, threshold, dan dilation result tampil.
- Bounding boxes tampil pada image.
- Segmented word/component crops tampil.
- App tidak crash saat file tidak valid.
- README menjelaskan bahwa demo bukan OCR.
- Tidak ada file sensitif atau metadata lokasi yang dipublikasikan.

---

## 13. Recommended Portfolio Positioning

Gunakan deskripsi berikut untuk recruiter:

**Indonesia:**

> Demo interaktif berbasis Streamlit untuk menampilkan pipeline segmentasi tulisan tangan menggunakan Python dan OpenCV. Pipeline mencakup grayscale conversion, binary inverse thresholding, morphological dilation, contour detection, bounding-box visualization, dan crop kandidat kata/komponen.

**English:**

> An interactive Streamlit demo that visualizes a handwritten word segmentation pipeline using Python and OpenCV. The pipeline includes grayscale conversion, binary inverse thresholding, morphological dilation, contour detection, bounding-box visualization, and segmented word/component crops.
