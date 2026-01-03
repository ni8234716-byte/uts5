from utils import *

while True:
    print("\n=== HITUNG LUAS BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Layang-layang")
    print("6. Belah Ketupat")
    print("7. Trapesium")
    print("8. Lingkaran")
    print("9. Heksagon")
    print("10. Pentagon")
    print("11. Keluar")

    pilih = input("Pilih menu (1-11): ")

    if pilih == "11":
        print("Terima kasih sudah menggunakan program ini ")
        break

    elif pilih == "1":
        s = float(input("Masukkan sisi: "))
        print("Luas =", persegi(s))

    elif pilih == "2":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Luas =", persegi_panjang(p, l))

    elif pilih == "3":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas =", segitiga(a, t))

    elif pilih == "4":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas =", jajar_genjang(a, t))

    elif pilih == "5":
        d1 = float(input("Masukkan diagonal 1: "))
        d2 = float(input("Masukkan diagonal 2: "))
        print("Luas =", layang_layang(d1, d2))

    elif pilih == "6":
        d1 = float(input("Masukkan diagonal 1: "))
        d2 = float(input("Masukkan diagonal 2: "))
        print("Luas =", belah_ketupat(d1, d2))

    elif pilih == "7":
        a = float(input("Masukkan sisi atas: "))
        b = float(input("Masukkan sisi bawah: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas =", trapesium(a, b, t))

    elif pilih == "8":
        r = float(input("Masukkan jari-jari: "))
        print("Luas =", lingkaran(r))

    elif pilih == "9":
        s = float(input("Masukkan sisi: "))
        print("Luas =", heksagon(s))

    elif pilih == "10":
        s = float(input("Masukkan sisi: "))
        print("Luas =", pentagon(s))

    else:
        print("Menu tidak tersedia, silahkan coba lagi ")
