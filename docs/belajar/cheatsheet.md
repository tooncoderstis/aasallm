# Cheatsheet — Rumus & Simbol

Ringkasan rumus dan simbol yang muncul di catatan belajar. Bertumbuh tiap bab (Fase 1).

## Notasi dasar

| Simbol | Arti |
|---|---|
| `x_t` | token (atau nilainya) pada posisi ke-`t` |
| `V` | ukuran kosakata (jumlah token) |
| `d` / `d_model` | dimensi model (panjang vektor tiap token) |
| `L` | jumlah lapisan Transformer |
| `d_ff` | dimensi lapisan feed-forward (umumnya `4d`) |
| `∑` (sigma) | penjumlahan semua suku |
| `∏` (pi) | perkalian semua suku |
| `∂` | turunan parsial |
| `‖x‖` | norma (panjang) vektor `x` |
| `xᵀ` | transpos dari `x` |

## Rumus per bab

### Bab 1 — Apa yang dihitung LLM
- Prediksi token berikutnya: `P(x_{t+1} | x_1, …, x_t)`
- Probabilitas kalimat (aturan rantai): `P(x_1, …, x_n) = ∏_{t=1}^{n} P(x_t | x_1, …, x_{t-1})`
- Jumlah parameter Transformer decoder: `N ≈ V·d + L·(4d² + 2·d·d_ff)`; jika `d_ff = 4d` maka `N ≈ V·d + L·12d²`
