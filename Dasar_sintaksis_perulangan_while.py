"""
progran perulangan membaca buku dengan while
"""
jumlah_buku = 10
print('ibu berkata "baca semua bukumu"')

jumlah_buku_terbaca = 0
print(f"jumlah buku terbaca yang sudah terbaca {jumlah_buku_terbaca}")

while jumlah_buku_terbaca < jumlah_buku:
    jumlah_buku_terbaca = jumlah_buku_terbaca + 1
    print(f"buku terbaca ke {jumlah_buku_terbaca}")

print(f"jumlah buku terbaca {jumlah_buku_terbaca}")
