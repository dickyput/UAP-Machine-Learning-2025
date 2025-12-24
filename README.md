# Klasifikasi Tingkat Kejernihan Air Menggunakan CNN

Proyek UAP Pembelajaran Mesin Universitas Muhammadiyah Malang 2025.
Sistem ini mengklasifikasikan citra air menjadi tiga kategori: **Gelap, Jernih, dan Keruh**.

## 1. Dataset
- **Sumber Data:** EUVP Dataset (Enhancement of Underwater Visual Perception).
- **Jumlah Data:** 7.000+ Citra.
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
