# scripts/load_data.py

import pandas as pd
import sqlite3
import os

# Path
cleaned_data_path = "../data/cleaned/cleaned_retail_data.csv"
db_path = "../database/retail.db"

# Baca data
print("📊 Membaca data bersih...")
df = pd.read_csv(cleaned_data_path)

# Koneksi ke database
print("🔌 Menghubungkan ke database...")
conn = sqlite3.connect(db_path)

# Load ke tabel
print("📤 Memuat data ke tabel 'sales'...")
df.to_sql(
    name="retail_sales",
    con=conn,
    if_exists="replace",  # atau "append" jika ingin tambah data
    index=False
)

# Verifikasi
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM retail_sales;")
row_count = cursor.fetchone()[0]
print(f"✅ Berhasil memuat {row_count} baris ke database!")

# Tutup koneksi
conn.close()