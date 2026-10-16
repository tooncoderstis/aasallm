# aasallm

Belajar **sekaligus** membangun Large Language Model dari nol, dipandu buku *"Memahami Matematika di Balik LLM"* (22 bab). Proyek ini menggabungkan catatan belajar berbahasa Indonesia dengan implementasi kode yang bisa dijalankan — mulai dari NumPy murni (transparan) lalu di-port ke PyTorch.

## Fitur
- Catatan belajar per bab (`docs/belajar/`) dengan contoh angka yang bisa dihitung ulang.
- Implementasi NumPy murni setiap rumus: vektor, matriks, softmax, cross-entropy, LayerNorm, attention, hingga blok Transformer.
- Port PyTorch dengan uji paritas terhadap versi NumPy.
- Mini-LLM (188 parameter) dilatih dari nol, diverifikasi terhadap titik pemeriksaan buku.
- Demo web: API inference + halaman chat (FastAPI), di-deploy ke EasyPanel.

## Stack
- Python 3.11 · NumPy (inti) · PyTorch (opsional) · FastAPI/uvicorn (demo)
- pytest + ruff · GitHub Actions · EasyPanel (Docker image via GHCR)

## Menjalankan
```sh
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[dev]"
```

## Testing
```sh
.venv\Scripts\pytest
.venv\Scripts\ruff check .
```

## Dokumentasi
- Kebutuhan: [`PRD.md`](PRD.md)
- Status: [`STATUS.md`](STATUS.md)
- Riwayat rilis: [`CHANGELOG.md`](CHANGELOG.md)
- Keputusan: [`docs/adr/`](docs/adr/)
- Catatan belajar: [`docs/belajar/`](docs/belajar/)
- Runbook: [`docs/runbooks/`](docs/runbooks/)

## Kontribusi
Lihat [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Sumber acuan
Buku *"Memahami Matematika di Balik LLM"* (`LLM.pdf`, `per bab/`) dipertahankan sebagai rujukan. Catatan di repo ini **bukan** salinan — ditulis ulang dengan bahasa sendiri.
