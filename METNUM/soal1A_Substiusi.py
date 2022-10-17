#Persamaan 1
x1 = 3
y1 = 5
total1 = 44
#persamaan 2
x2 = 5
y2 = 2
total2 = 29

print ("\nPENYELESAIAN DENGAN METODE SUBSTITUSI")
print(f"Persamaan 1  {x1}x + {y1}y = {total1}")
print(f"Persamaan 2  {x2}x + {y2}y = {total2}")
print("----------------------------------")
print(f"{x1}x = {total1} - {y1}y")
print(f" x = ({total1} - {y1}y) / {x1}")
print("-----------------------------------")

#Proses mencari nilai y
print("Mencari nilai y")
print(f"{x2}x + {y2}y = {total2}")
print(f"{x2} * (({total1} - {y1}y)/{x1}) + {y2}y = {total2}")

#Proses mencari nilai 1 y
proses1_y= total1*x2
#Proses mencari nilai 2 y
proses2_y= y1*x2 

print(f"({proses1_y} - {proses2_y}y)/{x1} + {y2}y = {total2}")
print(f" ------------------------- x {x1}")

#Proses mencari nilai 3 y
proses3_y= y2*x1
#Proses mencari nilai 4 y
proses4_y= total2*x1

print(f"{proses1_y} - {proses2_y}y + {proses3_y}y = {proses4_y}")
print(f"- {proses2_y}y + {proses3_y}y = {proses4_y} - {proses1_y}")

#Proses mencari nilai 5 y
proses5_y= (-proses2_y)+proses3_y
#Proses mencari nilai 6 y
proses6_y= proses4_y-proses1_y

print(f"{proses5_y}y = {proses6_y}")
print(f"y = {proses6_y} / {proses5_y}")

#hasil y
y= proses6_y/proses5_y

print(f"y = {y}")
print("-----------------------------------")
print ("Mencari nilai x")
print(f"{x1}x + {y1}y = {total1}")

#Proses hitung 1 x
proses1_x= y1*y

print(f"{x1}x + {proses1_x} = {total1}")
print(f"{x1}x = {total1} - {proses1_x}")

#Proses hitung 2 x
proses2_x= total1-proses1_x

print(f"{x1}x = {proses2_x}")
print(f"x = {proses2_x} / {x1}")

#Hasil x
x= proses2_x/x1
print(f"x = {x}")