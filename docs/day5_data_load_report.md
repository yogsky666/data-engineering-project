# Hari 5 - Data Load Report

## Proses

- Data dibaca dari: `../data/cleaned/cleaned_retail_data.csv`
- Dimuat ke tabel: `retail_sales` di `../database/retail.db`
- Metode: `pandas.to_sql()`
- Mode: `if_exists='replace'`

## Hasil

- Jumlah baris berhasil dimuat: 392.692
- Semua kolom sesuai skema

## Catatan

- Script bersifat idempotent (bisa dijalankan ulang tanpa duplikat)
- Cocok untuk otomatisasi harian
