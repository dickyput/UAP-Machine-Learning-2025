[Link Dataset](https://drive.google.com/drive/folders/1Au4Pvsjrn--V2T55MiFk_yC2AXcqCQl1?usp=sharing)
# 🌊 Water Quality Classification System
**Sistem Deteksi Kualitas Air Sungai Berbasis Deep Learning (CNN)**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy)

<p align="center">
  <a href="#-deskripsi-project">Deskripsi</a> •
  <a href="#-sumber-dataset">Dataset</a> •
  <a href="#-instalasi--penggunaan">Instalasi</a> •
  <a href="#-hasil-analisis--performa">Hasil Analisis</a> •
  <a href="#-live-demo">Live Demo</a>
</p>

</div>

---

## 📚 Deskripsi Project

Proyek ini bertujuan untuk mengotomatisasi pemantauan lingkungan dengan mengembangkan sistem **klasifikasi kualitas air sungai** berbasis citra digital. Menggunakan kekuatan **Convolutional Neural Networks (CNN)**, sistem ini mampu menganalisis karakteristik visual air dan mengkategorikannya ke dalam tiga tingkat kualitas:

1.  ⚫ **Gelap** (Tercemar berat/berwarna pekat)
2.  ⚪ **Jernih** (Bersih/layak)
3.  🟤 **Keruh** (Berlumpur/sedimen tinggi)

Proyek ini melakukan **Studi Komparasi** mendalam antara model *Custom CNN (Scratch)* melawan teknik *Transfer Learning* menggunakan **MobileNetV2** dan **ResNet50V2**.

---

## 📊 Sumber Dataset

Dataset bersumber dari repositori publik Kaggle yang telah dikurasi khusus untuk kebutuhan klasifikasi visual kualitas air.

* **Nama Dataset:** Sea Animals Image Dataset (Adapted for Water Quality)
* **Sumber:** [Kaggle - Vencerlanz09](https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste)
* **Total Data Training:** `18,296` gambar
* **Total Data Validasi:** `4,574` gambar

---

## ⚙️ Arsitektur & Metodologi

### 1. Preprocessing
Setiap citra yang masuk melalui proses:
* **Resizing:** Penyeragaman dimensi citra (224x224 px).
* **Normalization:** Rescaling nilai piksel (0-255 $\rightarrow$ 0-1).
* **Augmentation:** Rotasi dan *flip* acak untuk memperkaya variasi data latih.

### 2. Model yang Diuji
| Model | Tipe | Deskripsi Singkat |
| :--- | :--- | :--- |
| **Custom CNN** | *Scratch* | Dibangun dari nol dengan layer Conv2D, MaxPooling, dan Dense. |
| **MobileNetV2** | *Transfer Learning* | Model ringan (*lightweight*) yang efisien, menggunakan bobot ImageNet. |
| **ResNet50V2** | *Transfer Learning* | *Deep Residual Network* dengan arsitektur yang sangat dalam. |

---

## 💻 Instalasi & Penggunaan

Pastikan Python 3.8+ sudah terinstall.

**1. Install Dependensi**
pip install tensorflow numpy pandas matplotlib seaborn streamlit pillow
** 2. Jalankan Aplikasi (Streamlit)Gunakan perintah berikut di terminal proyek Anda:Bashstreamlit run app.py
🏆 Hasil Analisis & PerformaBagian ini merangkum evaluasi model pada 4,574 data validasi.🥇 Tabel Perbandingan Model (Final Result)Nama ModelAkurasiPredikatAnalisis SingkatCustom CNN95%🌟 BESTSangat Stabil. Menghasilkan keseimbangan Precision & Recall tertinggi tanpa bias. Tidak mengalami overfitting signifikan.MobileNetV288%GOODCukup Baik. Namun kesulitan membedakan kelas Keruh (banyak salah prediksi). Keunggulannya ada pada kecepatan training.ResNet50V285%POORKurang Optimal. Sangat kesulitan mengenali kelas Keruh (Recall hanya 0.58). Waktu training paling lama (berat).Kesimpulan: Model Custom CNN (Scratch) dipilih sebagai model utama karena memiliki akurasi tertinggi dan konsistensi terbaik

### 1. Custom CNN (Scratch) - 🌟 Best Model
| Kelas | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Gelap** | 0.96 | 1.00 | 0.98 | 1110 |
| **Jernih** | 0.99 | 0.92 | 0.95 | 2287 |
| **Keruh** | 0.87 | 0.96 | 0.91 | 1177 |
| **Accuracy** | | | **0.95** | 4574 |
| **Macro Avg** | 0.94 | 0.96 | 0.95 | 4574 |
| **Weighted Avg** | 0.95 | 0.95 | 0.95 | 4574 |

<br>

### 2. MobileNetV2
| Kelas | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Gelap** | 0.90 | 0.97 | 0.93 | 1110 |
| **Jernih** | 0.88 | 0.93 | 0.90 | 2287 |
| **Keruh** | 0.87 | 0.71 | 0.78 | 1177 |
| **Accuracy** | | | **0.88** | 4574 |
| **Macro Avg** | 0.88 | 0.87 | 0.87 | 4574 |
| **Weighted Avg** | 0.88 | 0.88 | 0.88 | 4574 |

<br>

### 3. ResNet50V2
| Kelas | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Gelap** | 0.87 | 0.88 | 0.87 | 1110 |
| **Jernih** | 0.82 | 0.97 | 0.89 | 2287 |
| **Keruh** | 0.91 | 0.58 | 0.71 | 1177 |
| **Accuracy** | | | **0.85** | 4574 |
| **Macro Avg** | 0.87 | 0.81 | 0.82 | 4574 |
| **Weighted Avg** | 0.85 | 0.85 | 0.84 | 4574 |

</details>
</details>
</details>
<div align="center">

Mas Dicky Putra Sanjaya


202210370311167


Teknik Informatika - Universitas Muhammadiyah Malang


Link live demo [DISINI](http://localhost:8501)


