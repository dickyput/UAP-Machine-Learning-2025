import os
import shutil

# --- KONFIGURASI LOKASI FOLDER ---
# Sesuaikan ini dengan lokasi folder 'DatasetAIR' di laptop Anda
# Berdasarkan gambar, pathnya ada di dalam folder 'dataset'
BASE_DIR = os.path.join("dataset", "DatasetAIR") 
OUTPUT_DIR = "Dataset_Final"

# --- MAPPING: Folder Asal -> Masuk ke Kelas Apa ---
MAPPING_RULES = [
    # 1. KELAS JERNIH (Ambil semua 'trainB' karena itu referensi air bersih)
    {"root": "underwater_dark",     "sub": "trainB", "target": "Jernih"},
    {"root": "underwater_imagenet", "sub": "trainB", "target": "Jernih"},
    {"root": "underwater_scenes",   "sub": "trainB", "target": "Jernih"},

    # 2. KELAS KERUH (Ambil 'trainA' dari scenes & imagenet)
    {"root": "underwater_imagenet", "sub": "trainA", "target": "Keruh"},
    {"root": "underwater_scenes",   "sub": "trainA", "target": "Keruh"},

    # 3. KELAS GELAP (Ambil 'trainA' dari dark)
    {"root": "underwater_dark",     "sub": "trainA", "target": "Gelap"},
]

# --- EKSEKUSI ---
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print(f"Mencari data di: {BASE_DIR} ...")
total_copied = 0

for rule in MAPPING_RULES:
    # Rakit path lengkap: dataset/DatasetAIR/underwater_xxx/trainX
    source_folder = os.path.join(BASE_DIR, rule["root"], rule["sub"])
    target_folder = os.path.join(OUTPUT_DIR, rule["target"])
    
    # Buat folder target (Jernih/Keruh/Gelap) jika belum ada
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        
    if os.path.exists(source_folder):
        files = os.listdir(source_folder)
        print(f"-> Memproses {rule['root']}/{rule['sub']} ke folder '{rule['target']}'...")
        
        for f in files:
            # Ambil hanya file gambar
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                src_path = os.path.join(source_folder, f)
                
                # Ubah nama file biar tidak bentrok (tambah prefix folder asal)
                new_name = f"{rule['root']}_{f}"
                dest_path = os.path.join(target_folder, new_name)
                
                shutil.copy2(src_path, dest_path)
                total_copied += 1
    else:
        print(f"⚠️ Folder tidak ditemukan: {source_folder}")

print("="*40)
print(f"SELESAI! Total {total_copied} gambar berhasil disusun.")
print(f"Cek folder baru bernama '{OUTPUT_DIR}' untuk dipakai training.")