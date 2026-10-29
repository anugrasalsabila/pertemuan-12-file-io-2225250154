
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim, nilai))
                except ValueError:
                    print(f"Baris {nomor} tidak valid: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")
        return None

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    daftar_nilai = [nilai for nim, nilai in data]
    jumlah_data = len(data)
    rata_rata = sum(daftar_nilai) / jumlah_data
    nilai_minimum = min(daftar_nilai)
    nilai_maksimum = max(daftar_nilai)
    jumlah_lulus = sum(1 for nilai in daftar_nilai if nilai >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {nilai_minimum:g}\n")
        file.write(f"Nilai maksimum: {nilai_maksimum:g}\n")
        file.write(f"Jumlah lulus (nilai >= 60): {jumlah_lulus}\n")

    print(f"Jumlah data valid: {jumlah_data}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Nilai minimum: {nilai_minimum:g}")
    print(f"Nilai maksimum: {nilai_maksimum:g}")
    print(f"Jumlah lulus (nilai >= 60): {jumlah_lulus}")
    print(f"Rekap berhasil disimpan ke {nama_file}")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

# jalankan alur utama
data = baca_data(input_file)

if data is not None:
    tulis_rekap(output_file, data)