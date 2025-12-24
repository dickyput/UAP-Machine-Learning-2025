# 🌊 Klasifikasi Kualitas Air Sungai Menggunakan CNN

**Sistem Deteksi Visual Kualitas Air Berbasis Deep Learning**

---

## TABLE OF CONTENT

- [Deskripsi Project](#-deskripsi-project-)
- [Latar Belakang](#latar-belakang)
- [Tujuan Pengembangan](#tujuan-pengembangan)
- [Sumber Dataset](#-sumber-dataset-)
- [Preprocessing dan Pemodelan](#-preprocessing-dan-pemodelan-)
  - [Preprocessing Data](#preprocessing-data)
  - [Pemodelan](#pemodelan)
- [Langkah Instalasi](#-langkah-instalasi-)
  - [Software Utama](#software-utama)
  - [Dependensi](#dependensi)
- [Menjalankan Sistem Prediksi (Streamlit)](#menjalankan-sistem-prediksi-streamlit)
- [Pelatihan Model](#pelatihan-model)
- [Hasil dan Analisis](#-hasil-dan-analisis-)
  - [Tabel Perbandingan Model (WAJIB)](#tabel-perbandingan-model-wajib)
  - [Detail Evaluasi (Classification Report)](#detail-evaluasi-classification-report)
- [Sistem Sederhana Streamlit](#-sistem-sederhana-streamlit-)
  - [Link Live Demo](#link-live-demo)
- [Biodata](#-biodata-)

---

## 📚 Deskripsi Project 📚

Proyek ini bertujuan untuk mengembangkan sistem **klasifikasi kualitas air sungai** berbasis citra digital. Sistem ini menggunakan teknologi *Deep Learning*, khususnya **Convolutional Neural Networks (CNN)**, untuk menganalisis karakteristik visual air dan mengkategorikannya ke dalam tiga tingkat kualitas: **Gelap**, **Jernih**, dan **Keruh**.

Proyek ini membandingkan performa antara model yang dibangun dari awal (*Custom CNN*) dengan teknik *Transfer Learning* menggunakan arsitektur yang sudah dilatih sebelumnya (*pre-trained models*) seperti **MobileNetV2** dan **ResNet50V2**.

## Latar Belakang

Pemantauan kualitas air sungai sangat penting untuk kelestarian lingkungan dan kesehatan masyarakat. Metode konvensional seringkali memerlukan pengambilan sampel fisik dan uji laboratorium yang memakan waktu.

Klasifikasi berbasis visi komputer ini didasarkan pada asumsi bahwa kualitas air yang berbeda memiliki fitur visual yang dapat dibedakan, seperti:
* 🌊 **Warna Air** (Tingkat kegelapan/kejernihan)
* 🌫️ **Kekeruhan** (Turbiditas atau partikel terlarut)

Sistem ini dirancang untuk mengotomatisasi proses identifikasi awal kualitas air berdasarkan input visual.

## Tujuan Pengembangan

1.  **Membangun Model Klasifikasi Citra:** Mengembangkan model CNN yang mampu mengenali tiga kategori kualitas air (Gelap, Jernih, Keruh) dengan akurasi yang tinggi.
2.  **Evaluasi Perbandingan Model:** Menganalisis perbandingan performa antara model *Custom CNN (Scratch)*, *MobileNetV2*, dan *ResNet50V2* untuk menentukan arsitektur terbaik untuk dataset ini.
3.  **Membangun Antarmuka Pengguna (Streamlit):** Menciptakan aplikasi web sederhana yang memungkinkan pengguna mengunggah gambar air dan mendapatkan prediksi kualitasnya secara *real-time*.

## 📊 Sumber Dataset 📊

Dataset yang digunakan dalam proyek ini bersumber dari repositori publik Kaggle, yang telah dikurasi dan diadaptasi untuk kebutuhan klasifikasi visual kualitas air.

* **Judul Dataset Asli:** Sea Animals Image Dataset (Diadaptasi untuk Kualitas Air)
* **Link Sumber:** [Kaggle - Vencerlanz09](https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste)
* **Deskripsi:** Dataset berisi ribuan citra yang terbagi ke dalam kelas-kelas berdasarkan karakteristik visualnya.

**Pembagian Data (Data Splitting):**
Data dibagi menjadi *training set* untuk melatih model dan *validation set* untuk mengevaluasi performa model saat pelatihan.
* **Data Training:** 18,296 gambar
* **Data Validasi:** 4,574 gambar

**Label Kelas:**
1.  `Gelap`
2.  `Jernih`
3.  `Keruh`

## 🧑‍💻 Preprocessing dan Pemodelan 🧑‍💻

### Preprocessing Data
Sebelum dimasukkan ke dalam model, citra mengalami beberapa tahapan pra-pemrosesan:
1.  **Resizing:** Mengubah ukuran semua citra input menjadi dimensi yang seragam (misalnya 224x224 piksel) agar sesuai dengan input layer model.
2.  **Normalisasi:** Mengubah nilai piksel dari rentang 0-255 menjadi rentang 0-1 untuk mempercepat konvergensi selama pelatihan.
3.  **Data Augmentation (Opsional pada Training):** Menerapkan transformasi acak (seperti rotasi, *flip*) pada data latih untuk meningkatkan generalisasi model dan mencegah *overfitting*.

### Pemodelan
Tiga pendekatan arsitektur model diuji dalam proyek ini:

1.  **Custom CNN (Scratch):**
    * Membangun arsitektur CNN dari nol menggunakan tumpukan layer Konvolusi (Conv2D), Pooling (MaxPooling2D), dan Fully Connected (Dense).
    * Dirancang khusus untuk dataset ini.

2.  **MobileNetV2 (Transfer Learning):**
    * Menggunakan arsitektur yang ringan dan efisien, dirancang untuk perangkat mobile.
    * Menggunakan bobot awal (*weights*) dari ImageNet, kemudian melakukan *fine-tuning* pada layer akhir untuk klasifikasi 3 kelas air.

3.  **ResNet50V2 (Transfer Learning):**
    * Menggunakan arsitektur jaringan saraf residual yang dalam (*deep residual network*).
    * Sama seperti MobileNetV2, menggunakan teknik *transfer learning* dari ImageNet.

## 🔧 Langkah Instalasi 🔧

### Software Utama
Proyek ini dikembangkan menggunakan bahasa pemrograman **Python** (disarankan versi 3.8 ke atas). Anda dapat menjalankannya di lingkungan lokal menggunakan VSCode, Jupyter Notebook, atau Google Colab.

### Dependensi
Perpustakaan (libraries) utama yang diperlukan untuk menjalankan proyek ini:
* **TensorFlow / Keras** (Framework Deep Learning utama)
* **NumPy & Pandas** (Manipulasi data numerik)
* **Matplotlib & Seaborn** (Visualisasi data dan grafik)
* **Streamlit** (Untuk membuat antarmuka web)
* **Pillow (PIL)** (Pengolahan citra)

Instalasi dependensi dapat dilakukan melalui pip:
```bash
pip install tensorflow numpy pandas matplotlib seaborn streamlit pillow
Menjalankan Sistem Prediksi (Streamlit)Untuk menjalankan aplikasi antarmuka web di komputer lokal Anda:Pastikan Anda berada di direktori proyek di terminal/command prompt.Jalankan perintah berikut (asumsi nama file utama adalah app.py):Bashstreamlit run app.py
Aplikasi akan terbuka secara otomatis di browser default Anda.Pelatihan ModelProses pelatihan dilakukan untuk ketiga model menggunakan framework Keras. Log pelatihan menunjukkan bahwa model dilatih selama beberapa epoch dengan memantau accuracy dan loss pada data training dan validasi.Optimizer: Adam (umumnya digunakan)Loss Function: Categorical Crossentropy (karena ini klasifikasi multi-kelas).Callbacks: Digunakan untuk menyimpan model terbaik (ModelCheckpoint) berdasarkan val_accuracy tertinggi selama pelatihan, seperti terlihat pada log WARNING:absl:You are saving your model as an HDF5 file....🔍 Hasil dan Analisis 🔍Bagian ini menyajikan hasil evaluasi kuantitatif dari ketiga model pada data validasi (4,574 gambar).Tabel Perbandingan Model (WAJIB)Berikut adalah ringkasan performa dan analisis komparatif dari model yang diuji:Nama ModelAkurasi (Validation)Hasil AnalisisCustom CNN (Scratch)95%Model ini menunjukkan performa terbaik (State-of-the-Art) pada dataset ini. Konvergensi loss sangat stabil selama pelatihan. Model memiliki keseimbangan nilai Precision dan Recall yang sangat tinggi di semua kelas (rata-rata F1-Score 0.95), mengindikasikan kemampuan generalisasi yang sangat baik tanpa bias signifikan ke kelas tertentu.MobileNetV288%Performa tergolong baik, namun mengalami kesulitan spesifik dalam membedakan kelas Keruh (nilai Recall hanya 0.71). Model ini cenderung "bingung" dan sering salah mengklasifikasikan citra keruh sebagai kelas lain. Kelebihannya adalah waktu pelatihan per epoch yang lebih cepat dibanding ResNet.ResNet50V285%Performa terendah di antara ketiga model. Model ini mengalami kesulitan signifikan dalam mengenali fitur visual kelas Keruh (nilai Recall sangat rendah: 0.58). Selain akurasi yang kurang optimal, model ini juga membutuhkan waktu komputasi pelatihan paling lama (sekitar 2200 detik/epoch).Kesimpulan: Berdasarkan tabel di atas, Custom CNN (Scratch) dipilih sebagai model terbaik untuk diimplementasikan karena memiliki akurasi tertinggi dan konsistensi prediksi yang paling andal di seluruh kategori.Detail Evaluasi (Classification Report)Berikut adalah data mentah laporan klasifikasi untuk transparansi hasil pengujian pada 4,574 data validasi.1. Custom CNN (Scratch) - Best ModelPlaintext              precision    recall  f1-score   support

       Gelap       0.96      1.00      0.98      1110
      Jernih       0.99      0.92      0.95      2287
       Keruh       0.87      0.96      0.91      1177

    accuracy                           0.95      4574
   macro avg       0.94      0.96      0.95      4574
weighted avg       0.95      0.95      0.95      4574
2. MobileNetV2 (Transfer Learning)Plaintext              precision    recall  f1-score   support

       Gelap       0.90      0.97      0.93      1110
      Jernih       0.88      0.93      0.90      2287
       Keruh       0.87      0.71      0.78      1177

    accuracy                           0.88      4574
   macro avg       0.88      0.87      0.87      4574
weighted avg       0.88      0.88      0.88      4574
3. ResNet50V2 (Transfer Learning)Plaintext              precision    recall  f1-score   support

       Gelap       0.87      0.88      0.87      1110
      Jernih       0.82      0.97      0.89      2287
       Keruh       0.91      0.58      0.71      1177

    accuracy                           0.85      4574
   macro avg       0.87      0.81      0.82      4574
weighted avg       0.85      0.85      0.84      4574
🎓 Sistem Sederhana Streamlit 🎓Aplikasi berbasis Streamlit ini dikembangkan untuk memudahkan pengguna melakukan prediksi kualitas air secara interaktif. Pengguna cukup mengunggah file gambar, dan sistem akan menampilkan prediksi kategori air beserta tingkat kepercayaan (confidence score) model.Link Live DemoBerikut adalah akses untuk mencoba demo aplikasi yang berjalan di lingkungan lokal (Localhost).Catatan: Tautan
di bawah ini hanya dapat diakses jika aplikasi Streamlit sedang berjalan di mesin lokal Anda atau jika Anda berada dalam jaringan lokal yang sama dengan mesin host.Local URL: http://localhost:8501Network URL: http://10.243.83.41:8501(Jika Anda men-deploy aplikasi ini ke layanan cloud seperti Streamlit Share atau Heroku di masa depan, gantilah tautan ini dengan URL publik yang aktif).👤 Biodata 👤Nama: Mas Dicky Putra SanjayaNIM: 202210370311167Program Studi: Teknik InformatikaUniversitas: Universitas Muhammadiyah Malang
