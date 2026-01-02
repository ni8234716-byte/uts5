import math

def kubus(s):
    return s ** 3

def balok(p, l, t):
    return p * l * t

def prisma_segitiga(a, ts, tp):
    return 0.5 * a * ts * tp

def limas_segiempat(s, t):
    return 1/3 * s * s * t

def tabung(r, t):
    return math.pi * r * r * t

def kerucut(r, t):
    return 1/3 * math.pi * r * r * t

def bola(r):
    return 4/3 * math.pi * r ** 3

def prisma_segiempat(p, l, t):
    return p * l * t

def limas_segitiga(a, ts, t):
    return 1/3 * 0.5 * a * ts * t

def prisma_lingkaran(r, t):
    return math.pi * r * r * t
