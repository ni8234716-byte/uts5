def format_rupiah(n):
    hasil = "{:,}".format(n)
    hasil = hasil.replace(",", ".")
    return f"Rp {hasil}"



