# Cara menjalankan agent

Langkah singkat untuk mencoba agent lokal:

1. Jalankan agent dari terminal:

```bash
python3 cli.py --task "Cek tugas"
```

2. Opsi lainnya:
- Ganti nama agent: `--name "NamaSaya"`
- Tidak memberikan `--task` hanya akan menampilkan status siap.

Perluasan:
- Tambahkan logika nyata pada `agent/agent.py`.
- Integrasikan API eksternal jika diperlukan.
