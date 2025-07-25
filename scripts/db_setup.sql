-- Membuat tabel retail_sales
CREATE TABLE IF NOT EXISTS retail_sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoiceno TEXT NOT NULL,
    stockcode TEXT,
    description TEXT,
    quantity INTEGER,
    invoicedate DATETIME,
    unitprice REAL,
    customerid INTEGER,
    country TEXT,
    totalprice REAL
);