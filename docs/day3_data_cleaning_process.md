# Hari 3 - Proses Pembersihan Data

## 1. Modifikasi Nama Kolom menjadi 'lower()'

- Menggunakan fungsi `lower()` untuk mengubah semua huruf pada nama kolom menjadi huruf kecil.
- Ini membantu menghindari kesalahan penulisan nama kolom dan memudahkan proses pembersihan data.

## 2. Missing Value

- kolom'costumerid' memiliki 135.080 nilai kosong.
- Untuk menganalisa pelanggan terdaftar

## 3. Tipe Data

- 'invoicedate' perlu diubah dari object ke datetime untuk memudah analisis

## 4. Filter Nilai Negatif

- 'quantity' negatif, kemungkinan retur pelanggan.
- 'unitprice' negatif, kemungkinan ada kesalahan dalam proses penjualan.

## 5. Kolom Baru

- 'totalprice' = 'quantity' \* 'unitprice'
- untuk analisa pendapatan dari pelanggan

## 6. Kolom yang dipertahankan

- Karena data ini sudah cukup lengkap, seluruh field dapat digunakan dalam analisis
