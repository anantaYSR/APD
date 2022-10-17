#Rumus Faktorial 
print('Program Menghitung Permutasi')
n = int(input('Masukkan Total Semua Buku : '))

def rumus_faktorial (n):
  if n > 2:
    return n * rumus_faktorial(n - 1)

  return 2

faktorial = rumus_faktorial(n)
print(f'{n}! = {faktorial}')

n = int(input('Masukkan Total Buku Basis Data : '))

def rumus_faktorial (n):
  if n > 2:
    return n * rumus_faktorial(n - 1)

  return 2

faktorial = rumus_faktorial(n)
print(f'{n}! = {faktorial}')

n = int(input('Masukkan Total Buku Metode Numerik : '))

def rumus_faktorial (n):
  if n > 2:
    return n * rumus_faktorial(n - 1)

  return 2

faktorial = rumus_faktorial(n)
print(f'{n}! = {faktorial}')

n = int(input('Masukkan Total Buku Algoritma Pemograman : '))

def rumus_faktorial (n):
  if n > 2:
    return n * rumus_faktorial(n - 1)

  return 2

faktorial = rumus_faktorial(n)
print(f'{n}! = {faktorial}')

n = int(input('Masukkan Jumlah Buku Jaringan : '))

def rumus_faktorial (n):
  if n > 2:
    return n * rumus_faktorial(n - 1)

  return 2

faktorial = rumus_faktorial(n)
print(f'{n}! = {faktorial}')


#Rumus Urutan Susunan Bebas
def hasil(a,b,c,d,e):
   return a / (b * c * d * e)
   
print('================Hasil==================')
num1 = int(input("Masukkan Hasil Total Buku : "))
num2 = int(input("Masukkan Hasil Basis Data   : "))
num3 = int(input("Masukkan Hasil Metode Numerik  : "))
num4 = int(input("Masukkan Hasil Algoritma Pemrograman : "))
num5 = int(input("Masukkan Hasil Jaringan  : "))

print('Hasil:')
print(num1,"",num2,"",num3,"",num4,"",num5,"=", hasil(num1,num2,num3,num4,num5))