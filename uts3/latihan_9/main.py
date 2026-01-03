from utils import input_nilai, hitung_rata

jumlah_siswa = int(input("Masukkan jumlah siswa: "))

print("\nInput Nilai Ujian 1")
nilai_ujian1 = input_nilai(jumlah_siswa)

print("\nInput Nilai Ujian 2")
nilai_ujian2 = input_nilai(jumlah_siswa)

rata1 = hitung_rata(nilai_ujian1)
rata2 = hitung_rata(nilai_ujian2)

print("\n===== HASIL NILAI =====")
print("Jumlah siswa:", jumlah_siswa)
print("Nilai Ujian 1:", nilai_ujian1)
print("Nilai Ujian 2:", nilai_ujian2)
print("Rata-rata Ujian 1:", round(rata1, 2))
print("Rata-rata Ujian 2:", round(rata2, 2))
