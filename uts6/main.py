from run import run

print("=== PENENTUAN KATEGORI NILAI ===")
nilai = int(input("Masukkan nilai: "))

hasil = run(nilai)
print("Kategori Nilai:", hasil)

print("\n====soal nomor 2====")
from logika import konversi_nilai

print("=== penentuan nilai berdasarkan huruf ===")

huruf = input("Masukkan huruf nilai: ")

nilai = konversi_nilai(huruf)

if nilai is not None:
    print("Nilai Angka =", nilai)
else:
    print("Huruf nilai tidak valid ")

