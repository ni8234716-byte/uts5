def parse_harga(data):
    # ubah "6,8,5,9" → [6, 8, 5, 9]
    return list(map(int, data.split(",")))


def total_harga(daftar_harga):
    return sum(daftar_harga)


def hitung_pajak(total):
    # Pajak dibulatkan ke bilangan bulat
    return round(total * 0.1)


def format_rupiah(angka):
    return "Rp " + format(angka, ",").replace(",", ".")
