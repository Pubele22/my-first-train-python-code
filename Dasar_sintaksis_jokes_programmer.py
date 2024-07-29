"""
This my first demo project with python
"""
print("Hello World")
print("My Name is Yustino")

"""
semua sintaksi dasar bahasa pemrograman terdiri dari :
1. Sekuensial : Langkah Berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial

print('Ibu berkata "pergi ke toko"')
print('Budi menjawab "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab "Beli 1 botol susu, jika ada telur beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan

jumlah_botol_susu = 172
jumlah_telur = 1570
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu >0 :
    print("Budi mengecek harga dan ternyata cukup")
    if jumlah_telur ==0 :
        print("Budi membeli satu botol susu")
    else :
        print("Budi membeli 1 botol susu dan 6 butir telur")
else :
    print("Budi tidak jadi membeli satu botol susu")

print("Budi pulang kerumah")
print("menyampaikan hasilnya kepada ibu")

