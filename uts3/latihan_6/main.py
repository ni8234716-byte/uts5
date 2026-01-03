from utils import parse_harga, total_harga, hitung_pajak, format_rupiah

data_input = input("Masukkan harga barang: ")

daftar_harga = parse_harga(data_input)
total = total_harga(daftar_harga)
pajak = hitung_pajak(total)
total_bayar = total + pajak

print("Daftar harga barang:", daftar_harga)
print("Total harga :", format_rupiah(total))
print("Pajak       :", format_rupiah(pajak))
print("Total bayar :", format_rupiah(total_bayar))

