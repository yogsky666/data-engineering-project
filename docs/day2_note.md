# Hari 2 - Analis Dataset Awal Dengan Python

## Hasil Observasi

- Dataset memiliki **541.909 baris** dan **8 Kolom**
- Kolom 'CostumerID' memiliki **135080 Nilai Kosong (NaN)** -> Cukup Besar untuk sebuah dataset
- Kolom 'Description' memiliki **1454 Nilai Kosong (NaN)**
- Kolom 'InvoiceDate' bertipe datetime

## Masalah Potensial

- Transaksi tanpa 'CustomerID'-> memungkinkan pengguna melakukan transaksi secara anaonim
- 'UnitPrice' bernilai nol, apakah barang tersebut merupakan promosi?
- 'Quantity' negatif, apakah ada kesalahan dalam pengiriman?

## Langkah Selanjutnya

- Membersihkan missing value pada kolom 'CostumerID'
- Ubah nama kolom keseluruhan menjadi 'lower'
- Filtering data yang berinilai negatif pada 'Quantity' dan 'UnitPrice'
- Buat kolom baru untuk 'TotalPrice'
- Simpan file bersih menjadi file .csv
