
# Pertemuan 12 - File I/O dan Error Handling

Nama: Intan Anugra Salsabila
NIM: 2225250154
Kelas: 3F

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM,nilai

Contoh isi data/nilai.txt:

    A001,85
    A002,78
    A003,92
    A004,abc
    A005,74
    A006,88

## Cara Menjalankan
py tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError
- ValueError

## Test Case

| Kasus | Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Latihan 1 | Menulis file catatan.txt | Isi file tersimpan | Teks Algoritma dan Pemrograman dan Pertemuan 12 tampil | Berhasil |
| Latihan 3 | Append file | Teks baru ditambahkan ke akhir file | Program berjalan tanpa error | Berhasil |
| Latihan 4 | Memproses baris data dengan nilai invalid | Data valid diproses dan nilai invalid ditangani | A001, A002, A003 tampil, lalu terjadi ValueError pada A004,abc | Belum berhasil |
| Latihan 5 | File tidak ditemukan | Pesan file tidak ditemukan ditampilkan | Pesan File tidak ditemukan. tampil | Berhasil |
| Latihan 6 | Input nilai berupa angka | Nilai dikonversi ke float | Input 95 menghasilkan Nilai = 95.0 | Berhasil |
| Tugas 5 | Rekap nilai dengan data invalid | Data invalid dilewati dan data valid tetap direkap | 5 data valid, rata-rata 83.40, maksimum 92, dan 5 mahasiswa lulus | Berhasil |

## Refleksi
Pada pertemuan ini, saya mempelajari cara membaca, menulis, dan menambahkan data ke file menggunakan Python. Saya juga mempelajari penggunaan try-except untuk menangani FileNotFoundError dan ValueError.

Pada latihan 4, program berhenti ketika menemukan nilai A004,abc karena teks tersebut tidak dapat dikonversi menjadi float. Pada latihan 5, program berhasil menampilkan pesan File tidak ditemukan. ketika file yang dicari tidak tersedia.

Pada tugas rekap nilai, program berhasil melewati data invalid A004,abc dan memproses lima data valid lainnya. Hasil pengolahan menunjukkan rata-rata nilai 83.40, nilai maksimum 92, dan jumlah mahasiswa yang lulus sebanyak 5 orang dengan batas nilai minimal 60.