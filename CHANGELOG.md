# Changelog

Semua perubahan penting didokumentasikan di file ini.

Format mengikuti [Keep a Changelog](https://keepachangelog.com) dan proyek ini menganut [Semantic Versioning](https://semver.org).

Status terkini: [`STATUS.md`](STATUS.md).

## [Unreleased]
### Added
- Fase 0: scaffold dokumen proyek (PRD, STATUS, CHANGELOG, ADR, runbook, catatan index).
- Struktur paket `src/aasallm` (np, torch, serve), `pyproject.toml`, smoke test.
- CI GitHub Actions (ruff + pytest), health files, secret scan.
- Pelaporan hub portofolio (`scripts/hub-report.mjs`, `npm run hub:report`).
- Fase 1: catatan Bab 1 (`docs/belajar/bab-01-apa-yang-dihitung-llm.md`) + seed `cheatsheet.md` & `glosarium.md`.
- Fase 1: catatan Bab 2 (`docs/belajar/bab-02-notasi.md`); `cheatsheet.md` & `glosarium.md` diperluas (notasi, eksponensial, logaritma).
- Fase 1: modul vektor NumPy (`src/aasallm/np/vectors.py`) + uji (`tests/test_vectors.py`) + catatan Bab 3 (`docs/belajar/bab-03-vektor.md`).
- Fase 1: modul matriks NumPy (`src/aasallm/np/matrices.py`) + uji (`tests/test_matrices.py`) + catatan Bab 4 (`docs/belajar/bab-04-matriks.md`).
- Fase 1: modul probabilitas NumPy (`src/aasallm/np/probability.py`) + uji (`tests/test_probability.py`) + catatan Bab 5 (`docs/belajar/bab-05-probabilitas.md`).
- Fase 1: modul teori informasi NumPy (`src/aasallm/np/information.py`) + uji (`tests/test_information.py`) + catatan Bab 6 (`docs/belajar/bab-06-informasi.md`).
- Fase 1: modul turunan/gradien NumPy (`src/aasallm/np/calculus.py`) + uji (`tests/test_calculus.py`) + catatan Bab 7 (`docs/belajar/bab-07-turunan.md`).
- Fase 1: catatan Bab 1–7, `cheatsheet.md`, dan `glosarium.md` lengkap untuk fondasi.
- Panduan membaca proyek (`docs/belajar/PANDUAN.md`): cara menavigasi catatan/kode/uji + peta baca rinci.
- Fase 2: catatan Bab 8 (`docs/belajar/bab-08-tokenisasi-embedding.md`) + modul NumPy (`src/aasallm/np/bpe.py`, `src/aasallm/np/embedding.py`) + uji (`tests/test_bpe.py`, `tests/test_embedding.py`).
- Utilitas `scripts/extract_bab.py` (ekstrak teks bab PDF ke stdout) + `pypdf` di extra `dev`.
- Panduan `docs/belajar/PANDUAN.md` diperbarui ke Fase 2 (Bab 8) + `STATUS.md` punya bagian "Cara melanjutkan (resume)".
- Fase 3: catatan Bab 9 (`docs/belajar/bab-09-neuron-lapisan-aktivasi.md`) + modul NumPy (`src/aasallm/np/activation.py`, `src/aasallm/np/neuron.py`) + uji (`tests/test_activation.py`, `tests/test_neuron.py`).
- Fase 4: catatan Bab 10 (`docs/belajar/bab-10-softmax-loss.md`) + modul NumPy (`src/aasallm/np/softmax.py`, `src/aasallm/np/loss.py`) + uji (`tests/test_softmax.py`, `tests/test_loss.py`).
- Fase 5: catatan Bab 11 (`docs/belajar/bab-11-backpropagation.md`) + modul NumPy (`src/aasallm/np/backprop.py`) + uji (`tests/test_backprop.py`).
- Fase 6: catatan Bab 12 (`docs/belajar/bab-12-optimizer.md`) + modul NumPy (`src/aasallm/np/optimizer.py`) + uji (`tests/test_optimizer.py`).
- Fase 7: catatan Bab 13 (`docs/belajar/bab-13-attention.md`) & Bab 14 (`docs/belajar/bab-14-multi-head-attention.md`) + modul NumPy (`src/aasallm/np/attention.py`, `src/aasallm/np/multihead.py`) + uji (`tests/test_attention.py`, `tests/test_multihead.py`).
- Fase 8: catatan Bab 15 (`docs/belajar/bab-15-informasi-posisi.md`) + modul NumPy (`src/aasallm/np/position.py`) + uji (`tests/test_position.py`).
- Fase 9: catatan Bab 16 (`docs/belajar/bab-16-blok-transformer.md`) & Bab 17 (`docs/belajar/bab-17-lapisan-keluaran.md`) + modul NumPy (`src/aasallm/np/layernorm.py`, `src/aasallm/np/block.py`, `src/aasallm/np/transformer.py`) + uji (`tests/test_layernorm.py`, `tests/test_block.py`, `tests/test_transformer.py`).
- Fase 10 (MILESTONE): catatan Bab 18 (`docs/belajar/bab-18-pretraining.md`), Bab 19 (`docs/belajar/bab-19-inference.md`), Bab 21 (`docs/belajar/bab-21-mini-llm-dari-nol.md`) + modul NumPy (`src/aasallm/np/training.py`, `src/aasallm/np/inference.py`, `src/aasallm/np/mini_llm.py`) + uji (`tests/test_training.py`, `tests/test_inference.py`, `tests/test_mini_llm.py`) + skrip `scripts/train_mini_llm.py`. Reproduksi eksperimen Bab 21 (loss `2,4480 → 0,0955`, `P(meja)=0,7492`, `P(tikar)=0,2494`, cos(meja,tikar) `0,9960`, 188 parameter).
- Fase 11: catatan Bab 20 (`docs/belajar/bab-20-sft-rlhf-dpo-lora.md`) + modul NumPy `src/aasallm/np/alignment.py` (SFT/reward/RLHF/DPO/LoRA) + uji `tests/test_alignment.py`.
- Fase 11: port PyTorch (`src/aasallm/torch/functional.py`) + model GPT char-level (`src/aasallm/torch/model.py`) + paritas NumPy↔PyTorch (`tests/test_torch_parity.py`) + uji model (`tests/test_torch_model.py`) + korpus `data/corpus.txt` + skrip `scripts/train_char_model.py`.
- Fase 12: layanan FastAPI demo (`src/aasallm/serve/engine.py`, `src/aasallm/serve/app.py`) + uji (`tests/test_serve.py`) + artefak deploy (`deploy/easypanel-docker/`) + runbook (`docs/runbooks/deploy.md`, `docs/runbooks/kegunaan-llm.md`) + catatan Bab 22 (`docs/belajar/bab-22-peta-besar.md`) & Lampiran (`docs/belajar/lampiran-eksperimen-bab-21.md`).
- Deploy produksi: image Docker Hub `aasatech/aasallm-web:latest` → EasyPanel service `aasallmweb` (project `m`) → https://aasallm-web.hgteop.easypanel.host (`/health = 200`). Target project menyimpang dari ADR-0004 (batas paket) → [ADR-0007](docs/adr/0007-target-deploy-aktual.md).

### Changed
- Fase 0 (Setup & Fondasi) dituntaskan ✅; hub portofolio tersinkron (`aasallm`, 13 fase terbaca).
- Keputusan model demo dicatat: mini-LLM Bab 21 = verifikasi, demo = model char-level Fase 11 (ADR-0006).
- Fase 1 (Fondasi Matematika, Bab 1–7) dimulai 🔄 lalu dituntaskan ✅: 5 modul NumPy (`vectors`, `matrices`, `probability`, `information`, `calculus`) + 7 catatan bab, seluruh uji hijau.
- Fase 2 (Tokenisasi & Embedding, Bab 8) dimulai 🔄.
- Fase 3 (Neuron & Aktivasi, Bab 9) dimulai 🔄 lalu dituntaskan ✅: katalog aktivasi (GELU/SiLU) + neuron/lapisan/FFN/SwiGLU, catatan Bab 9, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui.
- Fase 4 (Softmax & Loss, Bab 10) dimulai 🔄 lalu dituntaskan ✅: softmax stabil + loss `LSE(z) − z_c` + gradien `p − y`, pembanding MSE, label smoothing; catatan Bab 10, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui.
- Fase 5 (Backpropagation, Bab 11) dimulai 🔄 lalu dituntaskan ✅: aturan mundur tiap operasi, contoh jaringan mungil 11.3, residual connection, backprop batch, rumus biaya `6ND` & memori aktivasi; catatan Bab 11, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui.
- Fase 6 (Optimizer, Bab 12) dimulai 🔄 lalu dituntaskan ✅: SGD, momentum, Adam/AdamW (koreksi bias), jadwal LR warmup+cosine, gradient clipping, memori `16N`; catatan Bab 12, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui. **Bagian II (komponen neural) tuntas.**
- Fase 7 (Attention, Bab 13–14) dimulai 🔄 lalu dituntaskan ✅: scaled dot-product attention + causal mask + softmax per baris, dan multi-head (split/concat + `W_O`) + KV cache (MQA/GQA); catatan Bab 13–14, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui. **Bagian III (Transformer) dimulai.**
- Fase 8 (Informasi Posisi, Bab 15) dimulai 🔄 lalu dituntaskan ✅: learned PE (`X+P`), sinusoidal encoding, RoPE (rotasi Q/K), ALiBi, position interpolation; catatan Bab 15, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui.
- Fase 9 (Blok Transformer Lengkap, Bab 16–17) dimulai 🔄 lalu dituntaskan ✅: LayerNorm/RMSNorm, blok Pre-LN/Post-LN, penumpukan, rumus parameter (`≈12d²`/blok), lapisan keluaran (`Z=H·Eᵀ`), ukuran matriks & hitungan operasi; catatan Bab 16–17, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui. **Bagian III (Transformer) tuntas.**
- Fase 10 (Latih Mini-LLM dari Nol, Bab 18–19, 21) dimulai 🔄 lalu dituntaskan ✅ — **MILESTONE**: pretraining (loss, batch, scaling law, Chinchilla), inference (greedy/sampling/temperature/top-k/p/beam, KV cache/prefill-decode), dan replikasi mini-LLM 188 parameter dari nol (loss `2,4480 → 0,0955`, distribusi = proporsi data, cos(meja,tikar) `0,9960`, attention one-hot); catatan Bab 18/19/21, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui.
- Fase 11 (Port PyTorch + Model Kecil, Bab 18–20) dimulai 🔄 lalu dituntaskan ✅: port PyTorch (`torch/functional.py`) dengan uji **paritas** terhadap NumPy, model GPT char-level (`torch/model.py`) + korpus & skrip latih, dan matematika penyelarasan Bab 20 (SFT/reward/RLHF/DPO/LoRA di `np/alignment.py`); catatan Bab 20, `cheatsheet`/`glosarium`/`README`/`PANDUAN` diperbarui.
- Fase 12 (Layanan Inference & Demo Deploy) dimulai 🔄 lalu dituntaskan ✅: FastAPI (`/health`, `/generate`, `/explain`, halaman chat, rate-limit), artefak deploy EasyPanel (Dockerfile + build-push), runbook deploy & kegunaan, catatan Bab 22 & Lampiran; `README`/`PANDUAN`/`cheatsheet` diperbarui. **Seluruh 22 bab tuntas.**
### Fixed

## [0.1.0] - 2026-10-11
### Added
- Inisialisasi proyek `aasallm`: belajar & membangun LLM dari nol mengikuti buku *"Memahami Matematika di Balik LLM"*.
