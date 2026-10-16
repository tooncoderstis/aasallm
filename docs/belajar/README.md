# Catatan Belajar — Memahami Matematika di Balik LLM

Ringkasan tiap bab ditulis ulang dengan bahasa sendiri (Indonesia), disertai kode pendamping di `src/aasallm/` dan uji di `tests/`.

> Sumber acuan: buku *"Memahami Matematika di Balik LLM"* (PDF di root: `LLM.pdf`, `per bab/`). Catatan ini **bukan** salinan; fokus pada konsep, rumus kunci, dan contoh angka.

## Bagian I — Fondasi (Fase 1)
- [ ] Bab 1 — Apa Sebenarnya yang Dihitung LLM?
- [ ] Bab 2 — Kamus Notasi: Cara Membaca Rumus
- [ ] Bab 3 — Vektor
- [ ] Bab 4 — Matriks dan Perkalian Matriks
- [ ] Bab 5 — Probabilitas
- [ ] Bab 6 — Teori Informasi: Entropi, Cross-Entropy, Perplexity
- [ ] Bab 7 — Turunan, Gradien, dan Aturan Rantai

## Bagian II — Komponen Neural (Fase 2–6)
- [ ] Bab 8 — Dari Teks ke Angka: Tokenisasi dan Embedding
- [ ] Bab 9 — Neuron, Lapisan, dan Fungsi Aktivasi
- [ ] Bab 10 — Softmax dan Fungsi Kerugian
- [ ] Bab 11 — Backpropagation
- [ ] Bab 12 — Optimizer: SGD, Momentum, dan Adam

## Bagian III — Transformer (Fase 7–9)
- [ ] Bab 13 — Attention: Query, Key, Value
- [ ] Bab 14 — Multi-Head Attention
- [ ] Bab 15 — Informasi Posisi: Positional Encoding dan RoPE
- [ ] Bab 16 — Blok Transformer Lengkap
- [ ] Bab 17 — Lapisan Keluaran dan Perjalanan Penuh Satu Token

## Bagian IV — Pelatihan & Praktik (Fase 10–11)
- [ ] Bab 18 — Pretraining: Objektif, Batch, dan Scaling Law
- [ ] Bab 19 — Inference: Sampling, Temperature, dan KV Cache
- [ ] Bab 20 — Setelah Pretraining: SFT, RLHF, DPO, LoRA
- [ ] Bab 21 — Mengamati Mini-LLM Belajar dari Nol
- [ ] Bab 22 — Peta Besar
- [ ] Lampiran — Rincian Eksperimen Bab 21

## Berkas pendukung
- [ ] `cheatsheet.md` — ringkasan rumus & simbol
- [ ] `glosarium.md` — istilah kunci

## Konvensi penulisan
- Mulai dengan "Masalah" lalu "Gagasan", diakhiri "Inti bab".
- Setiap rumus disertai satu contoh angka yang bisa dihitung ulang.
- Tautkan ke kode (`src/aasallm/...`) dan uji (`tests/...`) yang relevan.
