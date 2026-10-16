# STATUS — aasallm

> **Sumber kebenaran status & progres.** Baca file ini dulu sebelum melanjutkan pekerjaan.
> Riwayat rilis: [`CHANGELOG.md`](CHANGELOG.md) · Keputusan: [`docs/adr/`](docs/adr/) · Kebutuhan: [`PRD.md`](PRD.md).
> **Jangan simpan kredensial di file ini.**

- **Terakhir diperbarui**: 2026-10-17
- **Versi produksi aktif**: demo `aasatech/aasallm-web:latest` → https://aasallm-web.hgteop.easypanel.host
- **Platform**: Python 3.11 (NumPy → PyTorch); deploy EasyPanel (Docker image via GHCR publik)

## TL;DR (konteks 30 detik)
Proyek belajar + membangun LLM dari nol mengikuti buku *"Memahami Matematika di Balik LLM"* (22 bab): catatan belajar bahasa Indonesia + implementasi kode (NumPy murni lalu PyTorch). Puncak: melatih mini-LLM 188 parameter dari nol dan memverifikasi titik pemeriksaan buku, lalu demo web (FastAPI + chat) di EasyPanel. **Fase 0 (Setup & Fondasi) selesai** ✅; **Fase 1 (Fondasi Matematika, Bab 1–7) selesai** ✅; **Fase 2 (Tokenisasi & Embedding, Bab 8) selesai** ✅; **Fase 3 (Neuron & Aktivasi, Bab 9) selesai** ✅; **Fase 4 (Softmax & Loss, Bab 10) selesai** ✅; **Fase 5 (Backpropagation, Bab 11) selesai** ✅; **Fase 6 (Optimizer, Bab 12) selesai** ✅; **Fase 7 (Attention, Bab 13–14) selesai** ✅; **Fase 8 (Informasi Posisi, Bab 15) selesai** ✅; **Fase 9 (Blok Transformer Lengkap, Bab 16–17) selesai** ✅; **Fase 10 (Latih Mini-LLM dari Nol, Bab 18–19, 21) selesai** ✅ — **MILESTONE** (loss `2,4480 → 0,0955`, `P(meja)=0,7492`, cos(meja,tikar) `0,9960`); **Fase 11 (Port PyTorch + Model Kecil, Bab 18–20) selesai** ✅; **Fase 12 (Layanan Inference & Demo Deploy) selesai** ✅ — **seluruh 22 bab + Lampiran tuntas**. Kesimpulan & keputusan kunci ada di bagian **Keputusan & kesimpulan penting** di bawah.

## Checklist Tahap
| Fase | Judul | Status |
|---|---|---|
| 0 | Setup & Fondasi | ✅ |
| 1 | Fondasi Matematika (Bab 1–7) | ✅ |
| 2 | Tokenisasi & Embedding (Bab 8) | ✅ |
| 3 | Neuron & Aktivasi (Bab 9) | ✅ |
| 4 | Softmax & Loss (Bab 10) | ✅ |
| 5 | Backpropagation (Bab 11) | ✅ |
| 6 | Optimizer (Bab 12) | ✅ |
| 7 | Attention (Bab 13–14) | ✅ |
| 8 | Informasi Posisi (Bab 15) | ✅ |
| 9 | Blok Transformer Lengkap (Bab 16–17) | ✅ |
| 10 | Latih Mini-LLM dari Nol (Bab 18–19, 21) | ✅ |
| 11 | Port PyTorch + Model Kecil (Bab 18–20) | ✅ |
| 12 | Layanan Inference & Demo Deploy | ✅ |

> Fase dikerjakan: tandai 🔄 saat mulai dan ✅ saat selesai, lalu jalankan `npm run hub:report` di tiap perubahan — hub portofolio mengirim notifikasi (inbox + Web Push).

## Cara melanjutkan (resume) — baca ini saat membuka proyek lagi
1. **Baca `STATUS.md` ini** — kondisi & langkah berikutnya ada di sini (satu-satunya sumber kebenaran progres).
2. **Pasang lingkungan** (sekali saja per mesin):
   `python -m venv .venv` lalu `.venv\Scripts\python -m pip install -e ".[dev]"` (extra `dev` termasuk `pypdf` untuk membaca PDF bab).
3. **Verifikasi cepat**: `.venv\Scripts\ruff check .` dan `.venv\Scripts\pytest` → harap **314 passed** (± 1,5 mnt; uji mini-LLM melatih 400 langkah sekali + uji PyTorch/FastAPI; butuh `torch` CPU + `fastapi`).
4. **Semua fase selesai.** Lanjutan opsional: deploy provisi EasyPanel (butuh `EASYPANEL_API_KEY`, lihat `docs/runbooks/deploy.md`) dan **BACKLOG** (fine-tuning lanjutan/kuantisasi/MoE, lihat `PRD.md`).
5. **Panduan membaca** proyek (urutan catatan↔kode↔uji): `docs/belajar/PANDUAN.md`.

Kondisi ringkas: **Fase 0–12 ✅** (seluruh 22 bab + Lampiran tuntas). Fase 0–2 ter-commit; Fase 3–12 masih di working tree menunggu instruksi commit.

## Kondisi saat ini
- **Fase 0 selesai** ✅: scaffold dokumen + struktur paket `src/aasallm`.
- **Fase 1 selesai** ✅: fondasi matematika (Bab 1–7) — 7 catatan bab + 5 modul NumPy (`vectors`, `matrices`, `probability`, `information`, `calculus`) + `cheatsheet.md` & `glosarium.md`.
- **Fase 2 selesai** ✅: tokenisasi & embedding (Bab 8) — catatan + modul NumPy (`bpe`, `embedding`) + uji.
- **Fase 3 selesai** ✅: neuron, lapisan & fungsi aktivasi (Bab 9) — catatan + modul NumPy (`activation`, `neuron`) + uji.
- **Fase 4 selesai** ✅: softmax & loss (Bab 10) — catatan + modul NumPy (`softmax`, `loss`) + uji.
- **Fase 5 selesai** ✅: backpropagation (Bab 11) — catatan + modul NumPy (`backprop`) + uji.
- **Fase 6 selesai** ✅: optimizer (Bab 12) — catatan + modul NumPy (`optimizer`) + uji. Bagian II tuntas.
- **Fase 7 selesai** ✅: attention & multi-head (Bab 13–14) — catatan + modul NumPy (`attention`, `multihead`) + uji.
- **Fase 8 selesai** ✅: informasi posisi (Bab 15) — catatan + modul NumPy (`position`) + uji.
- **Fase 9 selesai** ✅: blok Transformer & lapisan keluaran (Bab 16–17) — catatan + modul NumPy (`layernorm`, `block`, `transformer`) + uji. Bagian III tuntas.
- **Fase 10 selesai** ✅ — **MILESTONE**: latih mini-LLM dari nol (Bab 18–19, 21) — catatan + modul NumPy (`training`, `inference`, `mini_llm`) + uji + skrip `scripts/train_mini_llm.py`.
- **Fase 11 selesai** ✅: port PyTorch + model char-level + penyelarasan (Bab 18–20) — `torch/functional.py`, `torch/model.py`, `np/alignment.py` + uji (termasuk paritas NumPy↔PyTorch) + `data/corpus.txt` + skrip `scripts/train_char_model.py`.
- **Fase 12 selesai** ✅: layanan FastAPI + demo deploy (Bab 22 & Lampiran) — `serve/engine.py`, `serve/app.py` + uji + `deploy/easypanel-docker/` + runbook + catatan Bab 22 & Lampiran.
- Verifikasi lokal hijau: `ruff check .`, `ruff format --check .`, `pytest` (314 passed).
- Commit Fase 0–2 sudah ada; perubahan Fase 3–12 masih di working tree (belum di-commit — menunggu instruksi).
- Hub portofolio tersinkron (`aasallm`, 13 fase terbaca, 13 selesai).
- Deploy EasyPanel: **tayang** — image Docker Hub `aasatech/aasallm-web:latest`; project `m`, service `aasallmweb`, domain `aasallm-web.hgteop.easypanel.host`; `/health = 200` (lihat [ADR-0007](docs/adr/0007-target-deploy-aktual.md)).

## Yang belum selesai / menunggu
| Item | Catatan |
|---|---|
| Repo GitHub | Belum dibuat/push (rencana publik `aasallm`) |
| Secret hub | ✅ terisi di `.env` (dari repo portofolio); tidak di-commit |
| Secret EasyPanel | ✅ MCP `easypanel` aktif (dikelola server MCP); project baru ditolak (batas paket) → deploy di project `m` |
| Isi 22 bab | ✅ Bab 1–22 + Lampiran selesai |
| PyTorch | Terpasang CPU (`torch 2.14.1+cpu`); uji paritas dilewati otomatis bila `torch` tidak ada |
| FastAPI | `fastapi`/`uvicorn`/`httpx` terpasang (extra `serve`); uji layanan dilewati otomatis bila tidak ada |
| BACKLOG | Fine-tuning lanjutan (SFT/RLHF/DPO/LoRA), kuantisasi, MoE — lihat `PRD.md` |

## Keputusan & kesimpulan penting (sesi 2026-10-11)
- **Mini-LLM Bab 21 = alat verifikasi, bukan model pakai.** Dilatih hanya dari **4 kalimat** (korpus "kucing duduk di atas meja/tikar", 7 token/kalimat → 24 pasangan input–target), vocab 8 token, 188 parameter, batch penuh, 400 langkah. Ia hanya meniru proporsi data (`P(meja)≈0,75`, `P(tikar)≈0,25`); tidak bisa generalisasi/mengobrol.
- **Reproduksi Bab 21 tercapai persis** (Fase 10 ✅): inisialisasi `N(0,0,5²)` seed 42 via `numpy.default_rng` (E digambar pertama) + gradien beda-hingga terpusat `h=1e-6` + Adam `lr=0,05` → loss `2,4480 → 0,0955`, `P(meja)=0,7492`, `P(tikar)=0,2494`, perplexity `11,57 → 1,10`, cos(meja,tikar) `0,9960`, 188 param (184 dilatih). Uji menjalankan latih sekali (~25 dtk).
- **Demo (Fase 12) menyajikan model Fase 11** (char-level, korpus nyata), **bukan** mini-LLM — lihat [ADR-0006](docs/adr/0006-model-demo-dan-data.md).
- **Port PyTorch (Fase 11)** menyalin operasi inti di `src/aasallm/torch/functional.py` dan model char-level di `torch/model.py`; **paritas NumPy↔PyTorch** diuji `tests/test_torch_parity.py` (float64, tol `1e-6`), sesuai [ADR-0001](docs/adr/0001-bahasa-dan-stack.md).
- **Layanan serve (Fase 12)** = FastAPI (`serve/app.py`) di atas `serve/engine.py` (model char-level); endpoint `/health`, `/generate`, `/explain`, halaman chat, + rate-limit per IP; uji `tests/test_serve.py` (injeksi engine kecil).
- **PDF buku tidak di-commit** (`LLM.pdf`, `per bab/` ada di `.gitignore`) — alasan hak cipta, repo publik; tetap tersedia lokal sebagai rujukan.
- **Hub**: `HUB_INGEST_SECRET` terisi di `.env` (nilai dari repo portofolio), tidak di-commit.
- **EasyPanel**: tayang di project `m`, service `aasallmweb` (project `aasallm` ditolak batas paket — [ADR-0007](docs/adr/0007-target-deploy-aktual.md)); image Docker Hub `aasatech/aasallm-web:latest`.

## Cara menjalankan & menguji
```sh
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[dev]"
.venv\Scripts\ruff check .
.venv\Scripts\ruff format --check .
.venv\Scripts\pytest
npm run hub:report
```

Membaca teks bab dari PDF (untuk menulis catatan bab baru): `.venv\Scripts\python scripts\extract_bab.py "per bab\bab 22.pdf"`. (Seluruh bab sudah ditulis; perintah ini untuk rujukan bila menambah catatan.)

Menjalankan demo lokal: `.venv\Scripts\python -m uvicorn aasallm.serve.app:app --port 8000` lalu buka `http://127.0.0.1:8000/`.

## Rilis
`deploy/easypanel-docker/build-push.ps1` → image GHCR → deploy via MCP EasyPanel. Detail: [`docs/runbooks/`](docs/runbooks/).

## Referensi cepat
- PRD: `PRD.md` · Changelog: `CHANGELOG.md` · ADR: `docs/adr/README.md` · Runbook: `docs/runbooks/` · Catatan: `docs/belajar/` · Panduan membaca: `docs/belajar/PANDUAN.md`
