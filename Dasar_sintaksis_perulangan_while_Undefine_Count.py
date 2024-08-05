"""
program perulangan membaca buku dengan while sampai paham
"""
book_count = 10
print('ibu berkata "baca semua bukumu"')

understood_count = 0
read_count = 0
print(f"jumlah buku terbaca yang sudah terbaca dan dipahami {understood_count}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"buku ke {understood_count + 1} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"buku terbaca dan dipahami ke {understood_count}")

print(f"jumlah buku terbaca dan dipahami {understood_count}")

if understood_count == book_count:
    print('bu, Semua buku sudah dipahami')
else:
    print(f"bu, tidak semua buku bisa dipahami, budi hanya bisa memahami {understood_count} buku")
