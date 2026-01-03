from utils import format_rupiah,parse_list

print("=== KASIR SEDERHANA ===")

jumlah_orang = int(input("Masukkan jumlah orang: "))

data_input = input("Masukkan data harga: ")
data = parse_list(data_input)

total = 0
daftar_harga = []

for i in range(1, jumlah_orang + 1):
    harga = int(input(f"Harga orang ke-{i}: "))
    daftar_harga.append(harga)
    total += harga

print("----------------------")
print("Daftar harga per orang:", daftar_harga)
print("Total Bayar:", format_rupiah(total))
