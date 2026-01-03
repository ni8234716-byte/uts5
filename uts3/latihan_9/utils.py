def input_nilai(jumlah):
    nilai = []
    for i in range(jumlah):
        n = float(input(f"Masukkan nilai siswa ke-{i+1}: "))
        nilai.append(n)
    return nilai

def hitung_rata(nilai):
    total = 0
    for n in nilai:
        total += n
    return total / len(nilai)
