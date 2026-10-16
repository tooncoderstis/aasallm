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
