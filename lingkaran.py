import math

# Input jari-jari lingkaran dari pengguna
jari_jari = int(input("Masukkan jari-jari lingkaran: "))

# Hitung luas lingkaran
luas = math.pi * jari_jari ** 2

# Hitung keliling lingkaran
keliling = 2 * math.pi * jari_jari

# Tampilkan hasil
print(f"Luas lingkaran: {luas:.2f}")
print(f"Keliling lingkaran: {keliling:.2f}")