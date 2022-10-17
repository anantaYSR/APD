#faktorial 
print('============================')
print('Program Menghitung Permutasi')
print('============================')
n = int(input('Masukkan jumlah jenis buku : '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')

n = int(input('Masukkan jumlah buku Basis Data : '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')

n = int(input('Masukkan jumlah buku Metode Numerik : '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')

n = int(input('Masukkan jumlah buku Algoritma Pemograman : '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')

n = int(input('Masukkan jumlah buku Jaringan : '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')


# fungsi perkalian
def multiply(a,b,c,d,e):
   return a * b * c * d * e
   
print('\n========================================')
print('==============Pekalian================')
print('========================================')
num1 = int(input("Masukkan bilangan pertama : "))
num2 = int(input("Masukkan bilangan kedua   : "))
num3 = int(input("Masukkan bilangan ketiga  : "))
num4 = int(input("Masukkan bilangan keempat : "))
num5 = int(input("Masukkan bilangan kelima  : "))

print('Hasil:')
print(num1,"",num2,"",num3,"",num4,"",num5,"=", multiply(num1,num2,num3,num4,num5))