# Hari 4 - Skema Database: retail.db

Database ini akan menyimpan data penjualan ritel dari dataset bersih.

# Tabel: "retail_sales"

| Column Name | Data Type | Description           |
| ----------- | --------- | --------------------- |
| id          | INTEGER   | Primary key otomatis  |
| invoiceno   | TEXT      | Nomor invoice         |
| stockcode   | TEXT      | Kode Produksi         |
| description | TEXT      | Deskripsi Produk      |
| quantity    | INTEGER   | Jumlah barang dibeli  |
| invoicedate | DATETIME  | Format ISO8601        |
| unitprice   | REAL      | Harga satuan produk   |
| costumerid  | TEXT      | ID Pelanggan          |
| country     | TEXT      | Negara Asal Pelanggan |
| totalprice  | REAL      | Total harga pembelian |
