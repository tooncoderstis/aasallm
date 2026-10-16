# STATUS — aasallm

> **Sumber kebenaran status & progres.** Baca file ini dulu sebelum melanjutkan pekerjaan.
> Riwayat rilis: [`CHANGELOG.md`](CHANGELOG.md) · Keputusan: [`docs/adr/`](docs/adr/) · Kebutuhan: [`PRD.md`](PRD.md).
> **Jangan simpan kredensial di file ini.**

- **Terakhir diperbarui**: 2026-10-11
- **Versi produksi aktif**: —
- **Platform**: Python 3.11 (NumPy → PyTorch); deploy EasyPanel (Docker image via GHCR publik)

## TL;DR (konteks 30 detik)
Proyek belajar + membangun LLM dari nol mengikuti buku *"Memahami Matematika di Balik LLM"* (22 bab): catatan belajar bahasa Indonesia + implementasi kode (NumPy murni lalu PyTorch). Puncak: melatih mini-LLM 188 parameter dari nol dan memverifikasi titik pemeriksaan buku, lalu demo web (FastAPI + chat) di EasyPanel. **Fase 0 (Setup & Fondasi) selesai**; berikutnya **Fase 1 (Fondasi Matematika, Bab 2–7)**. Kesimpulan & keputusan kunci ada di bagian **Keputusan & kesimpulan penting** di bawah.

## Checklist Tahap
| Fase | Judul | Status |
|---|---|---|
| 0 | Setup & Fondasi | ✅ |
| 1 | Fondasi Matematika (Bab 2–7) | ⬜ |
| 2 | Tokenisasi & Embedding (Bab 8) | ⬜ |
| 3 | Neuron & Aktivasi (Bab 9) | ⬜ |
| 4 | Softmax & Loss (Bab 10) | ⬜ |
| 5 | Backpropagation (Bab 11) | ⬜ |
| 6 | Optimizer (Bab 12) | ⬜ |
| 7 | Attention (Bab 13–14) | ⬜ |
| 8 | Informasi Posisi (Bab 15) | ⬜ |
| 9 | Blok Transformer Lengkap (Bab 16–17) | ⬜ |
| 10 | Latih Mini-LLM dari Nol (Bab 18–19, 21) | ⬜ |
| 11 | Port PyTorch + Model Kecil (Bab 18–20) | ⬜ |
| 12 | Layanan Inference & Demo Deploy | ⬜ |

> Fase dikerjakan: tandai 🔄 saat mulai dan ✅ saat selesai, lalu jalankan `npm run hub:report` di tiap perubahan — hub portofolio mengirim notifikasi (inbox + Web Push).

## Kondisi saat ini
- **Fase 0 selesai** ✅: scaffold dokumen + struktur paket `src/aasallm`.
- Verifikasi lokal hijau: `ruff check .`, `ruff format --check .`, `pytest` (2 passed).
- `git init` sudah; 37 file ter-stage; **belum ada commit**.
- Hub portofolio tersinkron (`aasallm`, 13 fase terbaca, 1 selesai).
- Deploy: belum (Fase 12).

## Yang belum selesai / menunggu
| Item | Catatan |
|---|---|
| Commit awal | Belum ada (menunggu izin); 37 file ter-stage |
| Repo GitHub | Belum dibuat/push (rencana publik `aasallm`) |
| Secret hub | ✅ terisi di `.env` (dari repo portofolio); tidak di-commit |
| Secret EasyPanel | `EASYPANEL_API_KEY` belum diisi; MCP perlu di-restart bila baru ditambah |
| Isi 22 bab | Catatan + kode per bab menyusul fase 1–11 |

## Keputusan & kesimpulan penting (sesi 2026-10-11)
- **Mini-LLM Bab 21 = alat verifikasi, bukan model pakai.** Dilatih hanya dari **4 kalimat** (korpus "kucing duduk di atas meja/tikar", 7 token/kalimat → 24 pasangan input–target), vocab 8 token, 188 parameter, batch penuh, 400 langkah. Ia hanya meniru proporsi data (`P(meja)≈0,75`, `P(tikar)≈0,25`); tidak bisa generalisasi/mengobrol.
- **Demo (Fase 12) menyajikan model Fase 11** (char-level, korpus nyata), **bukan** mini-LLM — lihat [ADR-0006](docs/adr/0006-model-demo-dan-data.md).
- **PDF buku tidak di-commit** (`LLM.pdf`, `per bab/` ada di `.gitignore`) — alasan hak cipta, repo publik; tetap tersedia lokal sebagai rujukan.
- **Hub**: `HUB_INGEST_SECRET` terisi di `.env` (nilai dari repo portofolio), tidak di-commit.
- **EasyPanel**: project `aasallm`, service `web` (direncanakan, Fase 12).

## Cara menjalankan & menguji
```sh
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[dev]"
.venv\Scripts\ruff check .
.venv\Scripts\pytest
npm run hub:report
```

## Rilis
`deploy/easypanel-docker/build-push.ps1` → image GHCR → deploy via MCP EasyPanel. Detail: [`docs/runbooks/`](docs/runbooks/).

## Referensi cepat
- PRD: `PRD.md` · Changelog: `CHANGELOG.md` · ADR: `docs/adr/README.md` · Runbook: `docs/runbooks/` · Catatan: `docs/belajar/`
