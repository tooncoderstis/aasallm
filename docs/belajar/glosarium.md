# Glosarium

Istilah kunci yang dipakai di catatan belajar. Bertumbuh tiap bab (Fase 1).

| Istilah | Arti singkat |
|---|---|
| **Token** | Potongan teks (bisa kata, sub-kata, atau karakter) yang menjadi satuan masukan/keluaran LLM. |
| **Kosakata (vocabulary)** | Himpunan semua token yang dikenal model; ukurannya `V`. |
| **`<bos>` / `<eos>`** | Token buatan penanda awal (`beginning of sequence`) dan akhir (`end of sequence`) urutan. |
| **Logit** | Angka mentah keluaran model sebelum diubah menjadi probabilitas (Bab 10). |
| **Softmax** | Fungsi yang mengubah deretan logit menjadi probabilitas (0–1, jumlah 1). Bab 10. |
| **Parameter** | Angka model yang ditentukan lewat pelatihan lalu dibekukan. |
| **Autoregressive generation** | Menghasilkan teks dengan mengulang prediksi satu token, menempelkannya ke masukan, lalu mengulang. |
| **KV cache** | Penyimpanan vektor key/value token lama agar inferensi tidak menghitung ulang semuanya. Bab 19. |
| **Distribusi probabilitas** | Daftar angka non-negatif yang jumlahnya 1, menyatakan kemungkinan tiap token. |
| **Skalar** | Satu angka tunggal (ditulis huruf kecil biasa, mis. `x`). |
| **Vektor** | Deretan angka berurutan (ditulis huruf kecil tebal, mis. **x**); simbol `‖x‖` = panjangnya. |
| **Matriks** | Tabel angka baris × kolom (ditulis huruf besar tebal, mis. **X**); `X_ij` = elemen baris `i` kolom `j`. |
| **Indeks** | Nomor urut elemen (angka kecil di bawah, mis. `x_3`). Buku memakai indeks mulai 1; kode mulai 0. |
| **Eksponensial `eˣ`** | Fungsi yang selalu bernilai positif dan naik cepat; `e ≈ 2,71828`. |
| **Logaritma natural `ln`** | Kebalikan `eˣ`; mengubah perkalian menjadi penjumlahan. Basis `e` (nat); basis 2 untuk bit. |
| **Nat / bit** | Satuan informasi: 1 nat = logaritma basis `e`, 1 bit = logaritma basis 2. Bab 6. |
| **argmax** | Indeks (posisi) tempat nilai terbesar berada — dipakai memilih token, bukan nilainya. |
| **Dot product** | Operasi dua vektor → satu skalar: `∑ a_i b_i`; ukuran kecocokan arah & besar. |
| **Norma (L2)** | Panjang vektor: `√(∑ x_i²)`; dasar RMSNorm & LayerNorm. |
| **Cosine similarity** | Dot product dibagi panjang kedua vektor; hanya mengukur kemiripan arah, rentang `[−1, +1]`. |
| **Hadamard product** | Perkalian elemen-per-elemen dua vektor (`a ⊙ b`); hasilnya vektor. |
| **d_model** | Dimensi vektor tiap token (mis. 768 untuk GPT-2 small, 12288 untuk GPT-3). |
| **Transpos (Aᵀ)** | Matriks A dengan baris dan kolom ditukar; dipakai di `QKᵀ`. |
| **Transformasi linear** | Operasi `y = xW`; menumpuknya tidak menambah kemampuan (butuh non-linear). |
| **FLOP** | Satu operasi aritmetika pada bilangan desimal; ukuran biaya komputasi. |
| **Batch** | Memproses banyak token sekaligus lewat satu perkalian matriks. |
| **Ruang sampel (Ω)** | Himpunan semua hasil yang mungkin; untuk LLM = kosakata. |
| **Probabilitas bersyarat** | `P(A\|B) = P(A ∩ B)/P(B)`; model bahasa = kalkulator probabilitas bersyarat. |
| **Ekspektasi `E[·]`** | Rata-rata berbobot: `∑ P(x) f(x)`. |
| **Varians / simpangan baku** | Sebaran nilai di sekitar rata-rata; dasar normalisasi LayerNorm. |
| **Distribusi normal** | Sebaran Gaussian `N(μ, σ²)`; untuk inisialisasi parameter & analisis skala. |
| **Sampling** | Memilih satu token dari distribusi (inverse transform sampling). |
