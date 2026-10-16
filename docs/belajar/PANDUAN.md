# Panduan — Cara Memahami Proyek Ini

> Panduan membaca & memahami proyek `aasallm`. Bukan ringkasan materi, melainkan **cara menavigasi** catatan, kode, dan uji agar Anda benar-benar paham alurnya.
> Terkait: [`README.md`](README.md) (indeks bab) · [`STATUS.md`](../../STATUS.md) (progres) · [`PRD.md`](../../PRD.md) (tujuan).

## 1. Gambaran besar

Proyek ini punya tiga lapis yang saling menopang. Setiap bab buku menghasilkan ketiganya sekaligus:

```
Catatan belajar (kenapa & bagaimana)   →  docs/belajar/bab-*.md
Kode NumPy    (rumus yang bisa jalan)  →  src/aasallm/np/*.py
Uji           (bukti angkanya benar)   →  tests/test_*.py
```

Aturannya: **satu bab = satu catatan + satu modul + satu file uji**. Jadi Anda bisa masuk lewat mana saja — baca catatan, lihat kodenya, lalu jalankan ujinya untuk mengonfirmasi.

## 2. Peta repo

```
aasallm/
├─ docs/
│  ├─ belajar/            ← catatan belajar (bahasa Indonesia)
│  │  ├─ bab-01..bab-08.md
│  │  ├─ cheatsheet.md    ← ringkasan rumus per bab
│  │  ├─ glosarium.md     ← arti istilah kunci
│  │  └─ PANDUAN.md       ← file ini
│  ├─ adr/                ← keputusan desain (kenapa dibuat begini)
│  ├─ referensi/          ← makalah yang dirujuk buku
│  └─ runbooks/           ← cara operasional (deploy dll)
├─ src/aasallm/
│  ├─ np/                 ← implementasi NumPy murni (rujukan kebenaran)
│  ├─ torch/              ← port PyTorch (Fase 11; masih kosong)
│  └─ serve/              ← layanan demo (Fase 12; masih kosong)
├─ tests/                 ← uji pytest (verifikasi angka buku)
├─ PRD.md · STATUS.md · CHANGELOG.md
└─ pyproject.toml
```

Status terkini ada di `STATUS.md`; riwayat perubahan di `CHANGELOG.md`; **kenapa** sebuah keputusan diambil ada di `docs/adr/`.

## 3. Apa yang sudah dibuat (Fase 1–2, Bab 1–8)

**Catatan** (`docs/belajar/`) — 8 bab berformat **Masalah → Gagasan → Inti bab**, tiap rumus disertai contoh angka yang bisa dihitung ulang, ditutup "Cek pemahaman".

**Kode** (`src/aasallm/np/`) — 7 modul, masing-masing menyalin rumus buku apa adanya:

| Bab | Modul | Fungsi inti |
|---|---|---|
| 3 | `vectors.py` | `dot`, `norm_l2`, `cosine_similarity`, `add`, `scale`, `hadamard` |
| 4 | `matrices.py` | `matmul`, `matvec`, `transpose`, `matadd`, `identity`, `flops_matmul` |
| 5 | `probability.py` | `validate_distribution`, `conditional_probability`, `expected_value`, `variance`, `sample_categorical`, `normal_pdf` |
| 6 | `information.py` | `entropy`, `cross_entropy`, `kl_divergence`, `perplexity`, `mean_negative_log_likelihood` |
| 7 | `calculus.py` | `numerical_gradient`, `gradient_descent_step`, `sigmoid`/`relu` + turunan, `linear_backward` |
| 8 | `bpe.py` | `split_symbols`, `train_bpe`, `encode` (tokenizer BPE) |
| 8 | `embedding.py` | `one_hot`, `embedding_lookup`, `embed_one_hot`, `tied_logits`, `embedding_parameters` |

**Uji** (`tests/`) — 8 file, **101 uji lolos**, memverifikasi angka-angka dari buku (toleransi desimal ke-3).

Belum diisi (memang kosong): `src/aasallm/torch/` dan `src/aasallm/serve/` — dipakai mulai Fase 11–12.

## 4. Cara memahami tiap lapis

### a. Membaca catatan
Baca berurutan Bab 1 → 8. Tiap bab menjawab satu pertanyaan dan menutup dengan **Inti bab** + **Cek pemahaman**. Kalau macet pada simbol, buka `bab-02-notasi.md` atau `cheatsheet.md`.

### b. Membaca kode
Setiap fungsi = satu rumus. Docstring menyebut bab asalnya, jadi kode dibaca sebagai "rumus yang bisa dijalankan", bukan kotak hitam.

```python
def dot(a, b):
    """Dot product: a · b = sum_i a_i * b_i — dua vektor jadi satu skalar (Bab 3.4)."""
    ...
```

### c. Membaca uji sebagai kunci jawaban
Uji memuat angka persis dari buku. Kalau ragu memahami sebuah rumus, baca ujinya — di situlah angkanya diverifikasi.

```python
def test_dot_first_example():
    assert dot([2.0, 3.0], [4.0, -1.0]) == pytest.approx(5.0, abs=TOL)  # 2·4 + 3·(−1) = 5
```

### d. Rujukan cepat
Butuh rumus → `cheatsheet.md`. Lupa istilah → `glosarium.md`. Ingin tahu *kenapa* diputuskan begitu → `docs/adr/`.

## 5. Benang merah konsep (Bab 1–8 → menuju LLM)

Bab-bab yang sudah dikerjakan membentuk satu alur logis:

1. **Bab 1** — LLM = fungsi yang memetakan deret token → distribusi probabilitas token berikutnya.
2. **Bab 2** — cara membaca rumus (`∑`, `∏`, `eˣ`, `ln`) agar sisanya bisa dibaca.
3. **Bab 3** — isi LLM berbentuk **vektor**; **dot product** = ukuran kecocokan (dasar attention).
4. **Bab 4** — **matriks** = banyak dot product sekaligus; dua lapisan linear = satu lapisan → fungsi **non-linear wajib**.
5. **Bab 5** — keluaran = **distribusi probabilitas**; **aturan rantai** membenarkan "menebak satu token" = memodelkan bahasa.
6. **Bab 6** — mengubah distribusi menjadi satu angka: **loss = −log p(token benar)**; **perplexity = e^loss**.
7. **Bab 7** — **turunan/gradien** menunjukkan ke arah mana tiap parameter digeser agar loss turun; **aturan rantai** = dasar backpropagation.
8. **Bab 8** — gerbang masuk: **tokenisasi** memecah teks jadi sub-kata, **embedding** menukarnya menjadi vektor yang **dipelajari** (bukan ditulis manusia).

Ringkasnya: Bab 1 memotret tujuan; Bab 2–4 menyiapkan perkakas angka; Bab 5–6 memberi ukuran benar/salah; Bab 7 memberi cara memperbaikinya; Bab 8 mengubah teks menjadi angka agar semuanya bisa dimulai. Modul Bab 3–8 dipakai ulang di fase berikutnya (mis. `dot` di attention Bab 13, `cross_entropy` di loss Bab 10, `embedding_lookup` di seluruh model).

## 6. Peta baca rinci

Urutan yang disarankan. Kolom kanan = perintah untuk melihat sendiri.

| # | Baca catatan | Lihat kode | Buktikan | Estimasi |
|---|---|---|---|---|
| 1 | `bab-01-apa-yang-dihitung-llm.md` | — | — | 20 mnt |
| 2 | `bab-02-notasi.md` | — | — | 20 mnt |
| 3 | `bab-03-vektor.md` | `np/vectors.py` | `pytest tests/test_vectors.py` | 30 mnt |
| 4 | `bab-04-matriks.md` | `np/matrices.py` | `pytest tests/test_matrices.py` | 40 mnt |
| 5 | `bab-05-probabilitas.md` | `np/probability.py` | `pytest tests/test_probability.py` | 40 mnt |
| 6 | `bab-06-informasi.md` | `np/information.py` | `pytest tests/test_information.py` | 40 mnt |
| 7 | `bab-07-turunan.md` | `np/calculus.py` | `pytest tests/test_calculus.py` | 50 mnt |
| 8 | `bab-08-tokenisasi-embedding.md` | `np/bpe.py`, `np/embedding.py` | `pytest tests/test_bpe.py tests/test_embedding.py` | 50 mnt |

Cara pakai tiap baris: baca catatannya, buka modulnya untuk melihat rumus dalam kode, lalu jalankan ujinya. Jika ingin mencoba sendiri:

```sh
.venv\Scripts\python -c "from aasallm.np import dot, cosine_similarity; print(dot([2,3],[4,-1]))"
```

> Bab 2 hampir tanpa kode (kamus notasi); Bab 1 murni konsep. Bab 3–8 punya kode + uji.

### Bab berikutnya (belum ditulis)

- **Fase 3 (Bab 9)** — Neuron, lapisan, dan fungsi aktivasi. Melanjutkan Bab 4 (non-linear wajib) dan Bab 7 (`relu`/`sigmoid`).

Saat menulis bab baru, teks PDF-nya diekstrak dulu (lihat `scripts/extract_bab.py` dan bagian "Menjalankan" di bawah).

## 7. Menjalankan & menguji

```sh
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[dev]"
.venv\Scripts\ruff check .
.venv\Scripts\pytest
```

`pytest` hijau berarti semua angka buku cocok (toleransi desimal ke-3, lihat [ADR-0002](../adr/0002-strategi-verifikasi.md)).

**Membaca teks bab dari PDF** (untuk menulis catatan bab baru). PDF buku tidak di-commit (hak cipta) dan `pypdf` ada di extra `dev`:

```sh
.venv\Scripts\python scripts\extract_bab.py "per bab\bab 09.pdf"
```

## 8. Status & berikutnya

- **Fase 0 (Setup & Fondasi): selesai** ✅
- **Fase 1 (Fondasi Matematika, Bab 1–7): selesai** ✅
- **Fase 2 (Tokenisasi & Embedding, Bab 8): selesai** ✅
- **Berikutnya: Fase 3 (Neuron & Aktivasi, Bab 9)** — neuron, lapisan, dan fungsi aktivasi (`ReLU`, `GELU`, `SiLU`, `SwiGLU`).

Detail dan daftar centang ada di [`STATUS.md`](../../STATUS.md) dan [`README.md`](README.md).

## 9. Dokumen lain yang berguna

- Tujuan & lingkup proyek → [`PRD.md`](../../PRD.md)
- Progres terkini → [`STATUS.md`](../../STATUS.md)
- Riwayat rilis → [`CHANGELOG.md`](../../CHANGELOG.md)
- Keputusan teknis → [`docs/adr/`](../adr/)
- Makalah rujukan → [`docs/referensi/`](../referensi/)
