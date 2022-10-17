jumlah_soal = int(input("\nMasukkan jumlah soal: "))
seluruh_soal = int(input("Masukkan keseluruhan soal: "))
nilai_minimal = int(input("Masukkan nilai minimal: "))

keseluruhan = nilai_minimal * jumlah_soal
sisa_nilai = seluruh_soal - keseluruhan

n = jumlah_soal
r = sisa_nilai
print(f'\nJadi, nilai sejumlah {r} harus didistribusikan ke {n} soal')

# dikurang 1 karena telah menghitung nilai minimalnya
kombinasi_1 = (n + r - 1)
kombinasi_2 = r

if kombinasi_1 >= 0 and kombinasi_2 > 0 : #nilai kombinasi haruslah bilangan bulat positif
    print(f'\nMaka, banyak cara pemberian nilai adalah : C({kombinasi_1}, {kombinasi_2})\n')
else :
    print("\nBanyak cara tidak ditemukan karena tidak memenuhi syarat!\n")
    print(f'Dalam bentuk C : C({kombinasi_1},{kombinasi_2})\n')
