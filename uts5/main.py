from utils import *

while True:
    print("\n===== MENU BANGUN RUANG =====")
    print("1. Kubus")
    print("2. Balok")
    print("3. Prisma Segitiga")
    print("4. Limas Segiempat")
    print("5. Tabung")
    print("6. Kerucut")
    print("7. Bola")
    print("8. Prisma Segiempat")
    print("9. Limas Segitiga")
    print("10. Prisma Lingkaran")
    print("11. Keluar")

    pilih = int(input("Pilih bangun ruang: "))

    if pilih == 1:
        s = float(input("Masukkan sisi: "))
        print("Volume Kubus =", kubus(s))

    elif pilih == 2:
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        t = float(input("Masukkan tinggi: "))
        print("Volume Balok =", balok(p, l, t))

    elif pilih == 3:
        a = float(input("Masukkan alas segitiga: "))
        ts = float(input("Masukkan tinggi segitiga: "))
        tp = float(input("Masukkan tinggi prisma: "))
        print("Volume Prisma Segitiga =", prisma_segitiga(a, ts, tp))

    elif pilih == 4:
        s = float(input("Masukkan sisi alas: "))
        t = float(input("Masukkan tinggi limas: "))
        print("Volume Limas Segiempat =", limas_segiempat(s, t))

    elif pilih == 5:
        r = float(input("Masukkan jari-jari: "))
        t = float(input("Masukkan tinggi: "))
        print("Volume Tabung =", tabung(r, t))

    elif pilih == 6:
        r = float(input("Masukkan jari-jari: "))
        t = float(input("Masukkan tinggi: "))
        print("Volume Kerucut =", kerucut(r, t))

    elif pilih == 7:
        r = float(input("Masukkan jari-jari: "))
        print("Volume Bola =", bola(r))

    elif pilih == 8:
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        t = float(input("Masukkan tinggi: "))
        print("Volume Prisma Segiempat =", prisma_segiempat(p, l, t))

    elif pilih == 9:
        a = float(input("Masukkan alas segitiga: "))
        ts = float(input("Masukkan tinggi segitiga: "))
        t = float(input("Masukkan tinggi limas: "))
        print("Volume Limas Segitiga =", limas_segitiga(a, ts, t))

    elif pilih == 10:
        r = float(input("Masukkan jari-jari: "))
        t = float(input("Masukkan tinggi: "))
        print("Volume Prisma Lingkaran =", prisma_lingkaran(r, t))

    elif pilih == 11:
        print("Program selesai ")
        break

    else:
        print("Pilihan tidak valid!")

