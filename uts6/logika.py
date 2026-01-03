def tentukan_kategori(nilai):
    if 85 <= nilai <= 100:
        return "A"
    elif 80 <= nilai <= 84:
        return "A-"
    elif 75 <= nilai <= 79:
        return "B+"
    elif 70 <= nilai <= 74:
        return "B"
    elif 65 <= nilai <= 69:
        return "B-"
    elif 60 <= nilai <= 64:
        return "C+"
    elif 55 <= nilai <= 59:
        return "C"
    elif 45 <= nilai <= 54:
        return "D"
    elif nilai < 45:
        return "E"
    else:
        return "Nilai tidak valid"

def konversi_nilai(huruf):
    huruf = huruf.lower()

    if huruf == "a":
        return 4
    elif huruf == "a-":
        return 3.75
    elif huruf == "a+":
        return 3.5
    elif huruf == "b+":
        return 3
    elif huruf == "b":
        return 2.75
    elif huruf == "b-":
        return 2.5
    elif huruf == "c+":
        return 2
    elif huruf == "c":
        return 1
    elif huruf == "d":
        return 1
    elif huruf == "e":
        return 0
    else:
        return None
