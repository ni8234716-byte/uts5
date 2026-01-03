def parse_nilai(data):
    return list(map(int, data.split(",")))
    
def cek_kelulusan(nilai, kkm=75):
    rata_rata = sum(nilai) / len(nilai)
    if rata_rata >= kkm:
        return rata_rata, "LULUS"
    else:
        return rata_rata, "TIDAK LULUS"