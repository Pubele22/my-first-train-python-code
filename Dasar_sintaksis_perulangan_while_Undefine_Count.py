"""
progran perulangan membaca buku dengan while sampai paham
"""
jumlah_buku = 10
print('ibu berkata "baca semua bukumu"')

jumlah_buku_terbaca_dipahami = 0
total_jumlah_baca = 0
print(f"jumlah buku terbaca yang sudah terbaca dan dipahami {jumlah_buku_terbaca_dipahami}")

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_terbaca_dipahami == 9:
        print(f"buku ke {jumlah_buku_terbaca_dipahami + 1} belum paham")
    else:
        jumlah_buku_terbaca_dipahami = jumlah_buku_terbaca_dipahami + 1
        print(f"buku terbaca dan dipahami ke {jumlah_buku_terbaca_dipahami}")

print(f"jumlah buku terbaca dan dipahami {jumlah_buku_terbaca_dipahami}")

if jumlah_buku_terbaca_dipahami == jumlah_buku:
    print('bu, Semua buku sudah dipahami')
else:
    print(f"bu, tidak semua buku bisa dipahami, budi hanya bisa memahami {jumlah_buku_terbaca_dipahami} buku")
