def format_rupiah(angka):
    return "Rp " + format(angka, ",").replace(",", ".")
    
def parse_list(list_string):
    return list(map(int, list_string.split()))