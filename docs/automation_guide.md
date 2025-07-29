# Panduan Otomatisasi Pipeline

## Tujuan

Menjalankan ETL pipeline setiap hari tanpa intervensi manual.

## Platform: Windows

- Tool: Task Scheduler
- Waktu: 17:00 setiap hari
- Command: `python scripts/etl_pipeline.py`
- Lokasi proyek: `C:\laragon\www\data-engineering-project`

## Platform: Linux/Mac

- Tool: Cron
- Jadwal: `1 7 * * *`
- Command:
  ```bash
  /usr/bin/python3 C:\laragon\www\data-engineering-project\scripts/etl_pipeline.py
  ```
