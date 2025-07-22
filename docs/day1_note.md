# Hari 1 - Pengamatan Dataset Online Retail

## Informasi Dasar

- Nama Dataset : Online Retail
- Format : Excel (.xlsx)
- Sumber : UCI Machine Learning Repository
- Jumlah Baris : ~500k

## Informasi Kolom

1. InvoiceNo : Nomor Faktur
2. StockCode : Kode Barang
3. Description : Deskripsi Barang
4. Quantity : Jumlah Barang
5. InvoiceDate : Tanggal Transaksi
6. UnitPrice : Harga Satuan
7. CostumerID : ID Pelanggan
8. Country : Negara Pelanggan

## Tipe Data Kolom

1. InvoiceNo : Char (Object)
2. StockCode : Char (Object)
3. Description : Varchar
4. Quantity : Int
5. InvoiceDate : Date
6. UnitPrice : Float
7. CostumerID : Char (Object)
8. Country : Char (Object)

## Nilai Kolom Hilang

1. InvoiceNo : 0
2. StockCode : 0
3. Description : 1454
4. Quantity : 0
5. InvoiceDate :
6. UnitPrice : 0
7. CostumerID : 135080
8. Country : 0

## Observari Awal

- Kolom 'Quantity' dan 'UnitPrice' dapat dikalikan untuk dapat Total Penjualan
- Kolom 'InvoiceDate' dapat diubah menjadi format tanggal yang lebih mudah dibaca
- Kolom 'InvoiceNo', 'StockCode', 'Description', 'CostumerID', &'Country' dapat diubah menjadi format string yang lebih mudah dibaca
- Kolom 'Country' dapat menjadi acuan untuk menganalisis penjualan berdasarkan negara
- Kolom 'Quantity' dan 'UnitPrice' dapat digunakan untuk menganalisis penjualan berdasarkan jumlah dan harga satuan
- Kolom 'StockCode' dapat digunakan untuk menganalisa penjualan berdasarkan kode barang
- Kolom 'InvoiceDate' dapat digunakan untuk menganalisis penjualan berdasarkan tanggal transaksi terbaik
