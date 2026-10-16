# PRD: aasallm

**Status**: dikembangkan — fondasi (Fase 0) sedang dikerjakan; inti pembelajaran & kode menyusul.
**Versi dokumen**: 0.1
**Terkait**: `STATUS.md`, `CHANGELOG.md`, `docs/adr/`

> Dokumen ini menjawab **apa & kenapa**. Progres ada di `STATUS.md`, riwayat rilis di `CHANGELOG.md`, keputusan teknis di `docs/adr/`.

## 1. Ringkasan Produk
`aasallm` adalah proyek belajar sekaligus membangun Large Language Model **dari nol**, dipandu buku *"Memahami Matematika di Balik LLM"* (22 bab). Proyek memadukan dua hal: **catatan belajar berbahasa Indonesia** yang merangkum konsep & rumus tiap bab, dan **implementasi kode yang bisa dijalankan** — dimulai dari NumPy murni agar setiap rumus transparan, lalu di-port ke PyTorch untuk pelatihan sungguhan.

Target pembelajar: pemula yang bisa aritmetika dasar tetapi belum menguasai aljabar linear, kalkulus, atau notasi matematika formal. Setiap konsep dijelaskan lewat definisi tegas + contoh angka nyata, bukan perumpamaan.

Puncak perjalanan: melatih **mini-LLM dari nol** dan memverifikasi bahwa hasilnya cocok dengan titik pemeriksaan buku (loss `2,4480 → 0,0955`), lalu naik ke model kecil (char-level) yang benar-benar bisa dijalankan, dan **menyajikannya lewat demo web** (API inference + halaman chat) di EasyPanel untuk menunjukkan *apa gunanya LLM dan bagaimana cara kerjanya*.

## 2. Prinsip Desain Utama
- **Transparansi matematis dulu.** Implementasi NumPy murni menjadi rujukan kebenaran; PyTorch menyusul dan harus setara (paritas).
- **Terverifikasi, bukan diklaim.** Setiap angka penting diuji terhadap titik pemeriksaan buku pada `tests/`.
- **Satu contoh dilacak terus.** Mengikuti buku: satu mini-LLM (V=8, d=4, L=1, 188 parameter) dari bab ke bab.
- **Catatan = hasil proses.** Ringkasan per bab ditulis dengan bahasa sendiri, bahasa Indonesia.
- **Hemat & terstruktur.** Dokumen proyek mengikuti standar Aasa (aasaprojectkit).

## 3. Peran Pengguna (Roles)
| Role | Deskripsi | Akses |
|---|---|---|
| Pembelajar/penulis | Menulis catatan, menjalankan kode, bereksperimen | Tulisan penuh di repo |
| Pengguna demo | Mengakses halaman chat & API inference | Baca/pakai API publik (rate-limited) |
| Operator | Men-deploy & memantau layanan | MCP/CLI EasyPanel, `.env` lokal |

## 4. Fase / Modul Pengembangan
```
FASE 0  → Setup & Fondasi (scaffold, CI, hub)
FASE 1  → Fondasi Matematika (Bab 2–7)
FASE 2  → Tokenisasi & Embedding (Bab 8)
FASE 3  → Neuron & Aktivasi (Bab 9)
FASE 4  → Softmax & Loss (Bab 10)
FASE 5  → Backpropagation (Bab 11)
FASE 6  → Optimizer (Bab 12)
FASE 7  → Attention (Bab 13–14)
FASE 8  → Informasi Posisi (Bab 15)
FASE 9  → Blok Transformer Lengkap (Bab 16–17)
FASE 10 → Latih Mini-LLM dari Nol (Bab 18–19, 21) — MILESTONE
FASE 11 → Port PyTorch + Model Kecil (Bab 18–20)
FASE 12 → Layanan Inference & Demo Deploy
BACKLOG → Fine-tuning lanjutan (SFT/RLHF/DPO/LoRA), kuantisasi, MoE, dll.
```

### 4.10 Mini-LLM dilatih dari nol (MILESTONE)
- **Deskripsi**: Replikasi persis eksperimen Bab 21 + Lampiran: `V=8, d=4, L=1, d_ff=8`, seed 42, inisialisasi N(0, 0,5), Adam lr 0,05 tetap, 400 langkah, gradien beda-hingga terpusat, float64.
- **Acceptance criteria**:
  - Loss `2,4480 → 0,0955` (batas bawah teoretis 0,0937), toleransi ±0,001.
  - `P(meja) ≈ 0,7492`, `P(tikar) ≈ 0,2494`.
  - Perplexity `11,57 → 1,10`; `cos(meja, tikar) 0,7557 → 0,9960`.
  - Routing attention akhir ≈ one-hot.
  - Jumlah parameter = 188 (184 dilatih).
- **Non-goals**: kualitas teks produksi; ini toy model untuk verifikasi matematika.

### 4.12 Layanan inference & demo deploy
- **Deskripsi**: FastAPI menyajikan checkpoint hasil latihan sendiri. Endpoint `/generate`, `/health`, `/explain` (mengembalikan logit/probabilitas & langkah sampling). Halaman chat web sederhana menampilkan top-k probabilitas tiap langkah.
- **Acceptance criteria**: `GET /health = 200` di domain EasyPanel `aasallm-web.<wildcard>`; chat page menghasilkan token dari model; `/explain` mengembalikan distribusi per langkah.
- **Non-goals**: fine-tuning di server; GPU inference; model besar.

## 5. Model Data (ERD)
Bukan aplikasi ber-basis data. Artefak utama: **checkpoint model** (file bobot) dan **hasil eksperimen** (loss, plot). Tidak ada entitas persisten selain berkas.

## 6. Non-Functional Requirements
- **Reproduksibilitas**: seed tetap; hasil dapat direplikasi (toleransi desimal ke-3).
- **Kinerja**: mini-LLM & model kecil char-level dapat dilatih di CPU dalam waktu wajar.
- **Keamanan**: tidak ada rahasia di repo; `.env` di-ignore; demo tanpa data pengguna.
- **Portabilitas**: NumPy murni sebagai baseline; PyTorch opsional.
- **Ketergantungan minimal**: hindari framework berat sebelum waktunya.

## 7. KPI & Metrik Keberhasilan
| Area | Metrik | Target |
|---|---|---|
| Pembelajaran | Bab dengan catatan + kode | 22/22 |
| Verifikasi | Titik pemeriksaan buku lolos test | Semua |
| Kode | Paritas NumPy ↔ PyTorch | max abs diff < 1e-6 |
| Demo | Layanan hidup & sehat | `/health` = 200 |

## 8. Kepatuhan & Keamanan
- Repo publik; **tanpa** data pribadi, rahasia, atau kredensial.
- `.env` (hub & EasyPanel) tidak di-commit; secret hanya di `.env` lokal & env panel.
- Sumber PDF (`LLM.pdf`, `per bab/`) dipertahankan sebagai rujukan; konten PDF **tidak** didaur ulang mentah (ditulis ulang dengan bahasa sendiri).
- Secret scan (gitleaks) di CI.

## 9. Risiko & Mitigasi
| # | Risiko | Dampak | Mitigasi |
|---|---|---|---|
| 1 | Replikasi angka buku tidak persis (seed/urutan isi bobot/float64) | Tinggi | Ikuti resep Lampiran; toleransi desimal ke-3; uji terfokus |
| 2 | Ekspektasi "bisa ngobrol" atas model latihan sendiri | Sedang | Batas kemampuan dicantumkan jujur di runbook & README demo |
| 3 | `torch` berukuran besar / CPU lambat | Sedang | NumPy-first; torch sebagai extra opt-in; model kecil char-level |
| 4 | Detail figur PDF hilang saat ekstraksi | Rendah | Ekstrak per bab saat dikerjakan; verifikasi dengan teks |
| 5 | Secret EasyPanel/hub bocor | Tinggi | `.env` di-ignore, secret scan, rotasi kredensial |

## 10. Out of Scope
- Melatih model skala produksi (butuh GPU + data besar).
- Infrastruktur GPU terdistribusi (tensor/pipeline/sequence parallel).
- Isu etika/keamanan AI lanjutan, multimodal, MoE, kuantisasi (Backlog).

## 11. Ringkasan Keputusan
| # | Pertanyaan | Keputusan |
|---|---|---|
| 1 | Bahasa/model | Python 3.11, paket `aasallm`; catatan bahasa Indonesia |
| 2 | Stack kode | NumPy dulu (transparan) → PyTorch (performa) |
| 3 | Strategi verifikasi | Replikasi eksperimen Bab 21 sebagai acceptance gate |
| 4 | Bentuk demo | FastAPI (API + halaman chat) |
| 5 | Deploy | EasyPanel source Docker image via GHCR publik, programatik MCP |
| 6 | Repo | GitHub publik `aasallm` |
| 7 | Model demo | Checkpoint hasil latihan sendiri (edukatif) |
