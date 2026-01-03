from utils import parse_nilai, cek_kelulusan

data = input("Masukkan nilai (pisahkan dengan koma): ")

nilai = parse_nilai(data)

rata_rata, status = cek_kelulusan(nilai)

print("Daftar nilai:", nilai)
print("Rata-rata nilai:", rata_rata)
print("Status kelulusan:", status)