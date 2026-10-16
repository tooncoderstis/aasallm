# Cheatsheet — Rumus & Simbol

Ringkasan rumus dan simbol yang muncul di catatan belajar. Bertumbuh tiap bab (Fase 1).

## Notasi dasar

| Simbol | Arti |
|---|---|
| `x` | skalar (satu angka) |
| **x** | vektor (deretan angka) |
| **X** | matriks (tabel angka) |
| `x_i` | elemen ke-`i` dari vektor **x** |
| `X_ij` | elemen baris `i`, kolom `j` dari matriks **X** |
| `x_t` | token (atau nilainya) pada posisi ke-`t` |
| `V` | ukuran kosakata (jumlah token) |
| `d` / `d_model` | dimensi model (panjang vektor tiap token) |
| `L` | jumlah lapisan Transformer |
| `d_ff` | dimensi lapisan feed-forward (umumnya `4d`) |
| `∑` (sigma) | penjumlahan semua suku |
| `∏` (pi) | perkalian semua suku |
| `eˣ` / `exp(x)` | eksponensial (selalu positif) |
| `ln(x)` | logaritma natural (kebalikan `eˣ`) |
| `∂` | turunan parsial |
| `∇` | gradien (kumpulan turunan parsial) |
| `‖x‖` | norma (panjang) vektor `x` |
| `x · y` | dot product |
| `xᵀ` | transpos dari `x` |
| `max` / `argmax` | nilai terbesar / posisi nilai terbesar |
| `𝔼[·]` | ekspektasi (nilai rata-rata) |
| `∼` | berdistribusi sebagai |
| `≈` | kira-kira sama dengan |
| `∝` | sebanding dengan (sampai faktor konstan) |
| `∈`, `ℝⁿ` | anggota dari; himpunan vektor `n` bilangan real |

## Rumus per bab

### Bab 1 — Apa yang dihitung LLM
- Prediksi token berikutnya: `P(x_{t+1} | x_1, …, x_t)`
- Probabilitas kalimat (aturan rantai): `P(x_1, …, x_n) = ∏_{t=1}^{n} P(x_t | x_1, …, x_{t-1})`
- Jumlah parameter Transformer decoder: `N ≈ V·d + L·(4d² + 2·d·d_ff)`; jika `d_ff = 4d` maka `N ≈ V·d + L·12d²`

### Bab 2 — Kamus notasi
- Penjumlahan: `∑_{i=1}^{n} a_i = a_1 + a_2 + … + a_n`
- Perkalian: `∏_{i=1}^{n} a_i = a_1 × a_2 × … × a_n`
- Eksponensial: `e^{a+b} = e^a × e^b`; `e⁰ = 1`; `eˣ > 0` selalu
- Logaritma: `ln(1) = 0`; `ln(a × b) = ln(a) + ln(b)`; `ln(x) < 0` untuk `0 < x < 1`
- Ganti basis: `log₂(x) = ln(x) / ln(2)`
- Loss LLM: `−ln(p)` (positif karena `ln(p)` negatif untuk `p ∈ (0,1)`)

### Bab 3 — Vektor
- Penjumlahan: `a + b = [a_1+b_1, …, a_n+b_n]` (dimensi harus sama)
- Kali skalar: `c·x = [c·x_1, …, c·x_n]`
- Dot product: `a · b = ∑_{i=1}^{n} a_i b_i` → dua vektor jadi satu skalar
- Norma L2: `‖x‖ = √(∑ x_i²)`; hubungan `‖x‖² = x · x`
- Cosine similarity: `cos(θ) = (a·b)/(‖a‖‖b‖) ∈ [−1, +1]`
- Hadamard (elemen-per-elemen): `(a ⊙ b)_i = a_i b_i` → hasil vektor
- `Var(q·k) = d_k` untuk komponen normal standar (alasan pembagian `√d_k` di attention)

### Bab 4 — Matriks
- Ukuran: `A ∈ ℝ^{m×n}` (baris dulu, lalu kolom); `A_ij` = baris `i`, kolom `j`
- Transpos: `(Aᵀ)_ij = A_ji`; `(AB)ᵀ = BᵀAᵀ`
- Perkalian: `C_ij = ∑_p A_ip B_pj`; syarat dimensi tengah cocok: `(m×k)·(k×n)=(m×n)`
- Perkalian tidak komutatif: `AB ≠ BA`
- Transformasi linear: `y = xW`; dua lapisan linear = satu lapisan → non-linear wajib (Bab 9)
- Batch: `Q = HW_Q` menghasilkan query untuk semua token sekaligus
- Biaya: `FLOP ≈ 2·m·n·k`; attention berskala `n²`

### Bab 5 — Probabilitas
- Distribusi: `0 ≤ P(ω) ≤ 1` dan `∑ P(ω) = 1`
- Seragam: `P(ω) = 1/|Ω|`
- Bersyarat: `P(A | B) = P(A ∩ B) / P(B)`
- Aturan rantai: `P(x_1,…,x_n) = ∏_{t=1}^{n} P(x_t | x_{<t})` (berlaku persis)
- Log-prob: `log P(x_1,…,x_n) = ∑ log P(x_t | x_{<t})` (stabilitas numerik)
- Ekspektasi: `E[f] = ∑ P(x) f(x)`; varians `Var(x) = E[(x−E[x])²]`; `σ = √Var`
- Normalisasi LayerNorm: `ĥ = (h − μ)/σ`
- Normal: `p(x) = (1/(σ√(2π))) exp(−(x−μ)²/(2σ²))`
- Sampling: inverse-CDF — pilih token pertama yang `C_k > u`
