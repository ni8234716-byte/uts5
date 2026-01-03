from utils import nilai_terbesar, nilai_terkecil, parse_list

data_input = input("Masukkan Data: ")
data = parse_list(data_input)

print("Nilai Terbesar:", nilai_terbesar(data))
print("Nilai Terkecil:", nilai_terkecil(data))
