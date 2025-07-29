import pandas as pd
import logging
import sqlite3
import os
from datetime import datetime

def main():
    logging.info(f"🚀 Mulai ETL Pipeline - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Path
    raw_file = "data/raw/online_retail.xlsx"
    db_file = "database/retail.db"

    # Cek file ada
    if not os.path.exists(raw_file):
        logging.info(f"❌ File mentah tidak ditemukan: {raw_file}")
        return
    
    try:
        # ==  EXTRACT ==
        logging.info("📥 EXTRACT: Membaca data dari Excel..")
        df = pd.read_excel(raw_file, sheet_name="Online Retail", dtype={'InvoiceNo': str, 'CustomerID': str}) # untuk menghindari tipe data float/real
        
        # == TRANSFORM ==
        logging.info("🧹 TRANSFORM: Membersihkan data..")
        df.dropna(subset=['CustomerID'], inplace=True)
        
        # Hapus Duplikat
        df.drop_duplicates(inplace=True)
        
        # Ubah InvoiceDate ke datetime
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
        df.dropna(subset=['Quantity'], inplace=True) # Hapus jika gagal parse
        
        # Filter kuantitas dan harga positif
        df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

        # Buat kolom TotalPrice
        df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

        # Pilih Kolom
        cleaned_df = df[[
            'InvoiceNo', 'StockCode', 'Description', 'Quantity',
            'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country', 'TotalPrice'
        ]]

        # == LOAD ==
        logging.info("💾 LOAD: Memuat ke database SQLite..")
        conn = sqlite3.connect(db_file)

        # Ganti tabel jika sudah ada
        cleaned_df.to_sql(
            name="sales",
            con=conn,
            if_exists="replace",
            index=False
        )
        conn.close()

        logging.info(f"✅ ETL BERHASIL!! {len(cleaned_df)} baris dimuat ke database.\n")

    except Exception as e:
        logging.info(f"❌ ETL Gagal: {str(e)}")

if __name__ == "__main__":
    main()


# Setup logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = f"{log_dir}/etl_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler() # Tampilkan juga di terminal
    ]
)