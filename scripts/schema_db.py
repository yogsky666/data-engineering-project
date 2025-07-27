import sqlite3
import pandas as pd

# 1. Koneksi ke database SQLite
conn = sqlite3.connect('../database/retail.db')
cursor = conn.cursor()

# 2. Baca dan eksekusi script SQL
with open('../scripts/db_setup.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

# 3. Baca data .csv ke DataFrame
df = pd.read_csv('../data/cleaned/cleaned_retail_data.csv')

# 4. Simpan ke tabel SQLite
df.to_sql('retail_sales', conn, if_exists='replace', index=False)

# 5. Tutup koneksi
conn.commit()

print('Database schema and data successfully created and populated.')