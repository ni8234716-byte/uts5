from utils import parse_number, format_decimal

angka_input = input("Masukkan angka desimal : ")
jumlah_koma = int(input("Masukkan jumlah angka di belakang koma: "))

angka = parse_number(angka_input)
hasil = format_decimal(angka, jumlah_koma)

print("Hasil konversi:", hasil)