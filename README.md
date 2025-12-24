#  Klasifikasi Kualitas Air Sungai Menggunakan CNN
## 1. Dataset
- **Sumber Data:** EUVP Dataset (Enhancement of Underwater Visual Perception).
- **Jumlah Data:** 7.000+ Citra.
- **Preprocessing:** Resize 224x224, Normalisasi (1./255), Augmentasi (Rotation, Flip).

## 2. Arsitektur Model
Kami menggunakan 3 pendekatan model sesuai ketentuan UAP:
1.  **Custom CNN (Scratch):** Model CNN sederhana dengan 3 layer konvolusi yang dibangun dari awal.
2.  **MobileNetV2 (Transfer Learning):** Model pretrained yang ringan dan efisien. Layer dasar dibekukan (freeze).
3.  **ResNet50V2 (Transfer Learning):** Model pretrained yang lebih dalam (deep) untuk komparasi performa.
Proyek ini bertujuan untuk mengklasifikasikan tingkat risiko potabilitas atau kualitas air sungai berdasarkan citra visual menggunakan teknik *Deep Learning*. Sistem ini membagi kualitas air menjadi tiga kategori utama: **Gelap**, **Jernih**, dan **Keruh**.

Penelitian ini membandingkan performa antara arsitektur **Custom CNN (Scratch)** dengan teknik *Transfer Learning* menggunakan model **MobileNetV2** dan **ResNet50V2**.

##  Dataset

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


---

##  Hasil Analisis Perbandingan Model

Berikut adalah tabel ringkasan performa dan hasil analisis dari ketiga model yang telah diuji (Wajib):

| Nama Model | Akurasi | Hasil Analisis |
| :--- | :---: | :--- |
| **Custom CNN (Scratch)** | **95%** | Model ini menunjukkan performa terbaik (State-of-the-Art) dalam penelitian ini. Konvergensi loss sangat stabil dan memiliki keseimbangan nilai *Precision* dan *Recall* tertinggi (rata-rata 0.95), yang berarti model mampu membedakan ketiga kelas dengan sangat baik tanpa bias yang signifikan. |
| **MobileNetV2** | 88% | Performa tergolong baik (Good Fit) namun mengalami kesulitan pada kelas `Keruh` (Recall 0.71). Model cenderung bias memprediksi air keruh sebagai kelas lain. Keunggulan model ini ada pada kecepatan training yang lebih cepat dibandingkan ResNet. |
| **ResNet50V2** | 85% | Performa terendah (Underperforming) untuk dataset ini. Model mengalami kesulitan signifikan dalam mengidentifikasi ciri visual kelas `Keruh` (Recall sangat rendah: 0.58). Selain itu, waktu komputasi paling lambat (sekitar 2200 detik/epoch). |

> **Kesimpulan:** Berdasarkan tabel di atas, model **Custom CNN (Scratch)** dipilih sebagai model terbaik karena memiliki akurasi tertinggi (95%) dan konsistensi deteksi yang paling andal di seluruh kelas.

---

##  Detail Evaluasi (Classification Report)

Berikut adalah data teknis hasil pengujian pada data validasi (4,574 gambar) untuk transparansi hasil eksperimen.

### 1. Custom CNN (Scratch) - *Best Model*
Model dibangun dari awal (*from scratch*) dengan arsitektur Conv2D yang disesuaikan.
```text
              precision    recall  f1-score   support

       Gelap       0.96      1.00      0.98      1110
      Jernih       0.99      0.92      0.95      2287
       Keruh       0.87      0.96      0.91      1177
### 2. MobileNetV2 (Transfer Learning)
Model menggunakan bobot pre-trained dari ImageNet dengan fine-tuning.
              precision    recall  f1-score   support

       Gelap       0.90      0.97      0.93      1110
      Jernih       0.88      0.93      0.90      2287
       Keruh       0.87      0.71      0.78      1177

    accuracy                           0.88      4574
   macro avg       0.88      0.87      0.87      4574
weighted avg       0.88      0.88      0.88      4574
### 3. ResNet50V2 (Transfer Learning)
Arsitektur deep residual network yang lebih kompleks.
              precision    recall  f1-score   support

       Gelap       0.87      0.88      0.87      1110
      Jernih       0.82      0.97      0.89      2287
       Keruh       0.91      0.58      0.71      1177

    accuracy                           0.85      4574
   macro avg       0.87      0.81      0.82      4574
weighted avg       0.85      0.85      0.84      4574
    accuracy                           0.95      4574
   macro avg       0.94      0.96      0.95      4574
weighted avg       0.95      0.95      0.95      4574
## Catatan Penilaian
File model (`.h5`) dan dataset disimpan secara lokal (Local Storage) karena ukurannya melebihi batas upload GitHub (100MB).
Demo aplikasi dan model akan dijalankan langsung dari laptop saat sesi presentasi.
