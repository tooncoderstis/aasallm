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
