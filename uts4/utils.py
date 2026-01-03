import math

def persegi(s):
    return s * s

def persegi_panjang(p, l):
    return p * l

def segitiga(a, t):
    return 0.5 * a * t

def jajar_genjang(a, t):
    return a * t

def layang_layang(d1, d2):
    return 0.5 * d1 * d2

def belah_ketupat(d1, d2):
    return 0.5 * d1 * d2

def trapesium(a, b, t):
    return 0.5 * (a + b) * t

def lingkaran(r):
    return math.pi * r * r

def heksagon(s):
    return (3 * math.sqrt(3) / 2) * s * s

def pentagon(s):
    return (5 * s * s) / (4 * math.tan(math.pi / 5))