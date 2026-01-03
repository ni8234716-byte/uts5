from utils import hitung_total_jumlah, parse_list

data_input = input("Masukkan Data: ")
data = parse_list(data_input)

total_jumlah = hitung_total_jumlah(data)

print("Total Jumlah Adalah:", total_jumlah)
