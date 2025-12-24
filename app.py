import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# --- KONFIGURASI ---
st.set_page_config(page_title="UAP Water Quality", page_icon="💧")
st.title("Klasifikasi Kejernihan Air 💧")
st.write("Sistem Deteksi Kualitas Air Menggunakan Citra (Deep Learning)")

# --- SIDEBAR: PILIH MODEL ---
st.sidebar.header("Panel Kontrol")
pilihan_model = st.sidebar.selectbox(
    "Pilih Model:",
    ("MobileNetV2 (Recommended)", "ResNet50V2", "Custom CNN")
)

# --- LOAD MODEL (Cached) ---
@st.cache_resource
def load_my_model(model_name):
    if model_name == "MobileNetV2 (Recommended)":
        return tf.keras.models.load_model('models/model_mobilenet.h5')
    elif model_name == "ResNet50V2":
        return tf.keras.models.load_model('models/model_resnet.h5')
    else:
        return tf.keras.models.load_model('models/model_scratch.h5')

# Coba Load Model
try:
    model = load_my_model(pilihan_model)
    st.sidebar.success(f"Model {pilihan_model} Aktif!")
except:
    st.error("Model belum ditemukan! Jalankan training.ipynb dulu.")

# --- AREA UTAMA ---
uploaded_file = st.file_uploader("Upload Foto Air (JPG/PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar diupload', use_column_width=True)
    
    if st.button("🔍 Analisis Kualitas Air"):
        with st.spinner('Sedang memproses...'):
            # Preprocessing (Harus sama dengan Training!)
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
            img_array = np.asarray(image)
            img_array = img_array / 255.0 # Normalisasi
            img_reshape = np.expand_dims(img_array, axis=0)
            
            # Prediksi
            prediction = model.predict(img_reshape)
            
            # LABEL (Sesuaikan Abjad: Gelap, Jernih, Keruh)
            class_names = ['Gelap', 'Jernih', 'Keruh'] 
            
            idx = np.argmax(prediction)
            hasil_label = class_names[idx]
            confidence = prediction[0][idx] * 100
            
            # Tampilan Hasil
            st.markdown("---")
            st.subheader("Hasil Analisis:")
            
            if hasil_label == 'Jernih':
                st.success(f"✅ **{hasil_label}**")
            elif hasil_label == 'Keruh':
                st.warning(f"⚠️ **{hasil_label}**")
            else:
                st.info(f"🌑 **{hasil_label}**")
                
            st.write(f"Tingkat Keyakinan Model: **{confidence:.2f}%**")