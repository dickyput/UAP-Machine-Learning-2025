# Klasifikasi Tingkat Kejernihan Air Menggunakan CNN

Proyek UAP Pembelajaran Mesin Universitas Muhammadiyah Malang 2025.
Sistem ini mengklasifikasikan citra air menjadi tiga kategori: **Gelap, Jernih, dan Keruh**.

## 1. Dataset

Dataset yang digunakan dalam penelitian ini bersumber dari repositori publik Kaggle yang telah disesuaikan untuk studi kasus klasifikasi air.

- **Nama Dataset:** Sea Animals Image Dataset (diadaptasi untuk Visualisasi Air)
- **Sumber Download:** [Kaggle - Vencerlanz09](https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste)
- **Struktur Data:**
  - **Training:** 18,296 gambar
  - **Validasi:** 4,574 gambar
- **Kelas (Label):**
  1. `Gelap`
  2. `Jernih`
  3. `Keruh`
- **Sumber Data:** EUVP Dataset (Enhancement of Underwater Visual Perception).
- **Preprocessing:** Resize 224x224, Normalisasi (1./255), Augmentasi (Rotation, Flip).

## 2. Arsitektur Model
Kami menggunakan 3 pendekatan model sesuai ketentuan UAP:
1.  **Custom CNN (Scratch):** Model CNN sederhana dengan 3 layer konvolusi yang dibangun dari awal.
2.  **MobileNetV2 (Transfer Learning):** Model pretrained yang ringan dan efisien. Layer dasar dibekukan (freeze).
3.  **ResNet50V2 (Transfer Learning):** Model pretrained yang lebih dalam (deep) untuk komparasi performa.

## 3. Hasil Analisis Perbandingan

| Nama Model | Akurasi | Loss | F1-Score | Waktu Training | Analisis Singkat |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Custom CNN** | 82% | 0.45 | 0.81 | Cepat | Cukup baik namun learning curve fluktuatif. |
| **MobileNetV2** | 96% | 0.12 | 0.96 | Sedang | **Model Terbaik**. Sangat stabil dan akurat. |
| **ResNet50V2** | 94% | 0.18 | 0.94 | Lama | Akurasi tinggi namun ukuran model lebih besar. |

## 4. Cara Menjalankan Website (Lokal)
1. Install library: `pip install -r requirements.txt`
2. Jalankan Streamlit: `streamlit run app.py`
