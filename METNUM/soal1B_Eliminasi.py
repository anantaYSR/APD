#Persamaan 1
x1 = 3
y1 = 5
c1 = 44
#persamaan 2
x2 = 5
y2 = 2
c2 = 29

print ("\nPENYELESAIAN DENGAN METODE ELIMINASI")
print(f"Persamaan 1  {x1}x + {y1}y = {c1}")
print(f"Persamaan 2  {x2}x + {y2}y = {c2}")
print("----------------------------------")
print("Proses eliminasi mencari nilai Y")

#eliminasi persamaan 1 untuk nilai y
x3= x2*x1
y3= y1*x2
c3= c1*x2

#eliminasi persamaan 2 untuk nilai y
x4= x1*x2
y4= y2*x1
c4= c2*x1

print(f"{x1}x + {y1}y = {c1} | {x2} | {x3}x + {y3}y = {c3}")
print(f"{x2}x + {y2}y = {c2} | {x1} | {x4}x + {y4}y = {c4}")
print("----------------------------------")
print(f"{x3}x + {y3}y = {c3}")
print(f"{x4}x + {y4}y = {c4}")
print("-------------------------------- -")

#Proses mencari nilai 1 y
proses1_1= y3-y4
#Proses mencari nilai 2 y
proses1_2= c3-c4

print(f"({x3}x - {x4}x) + ({y3}y - {y4}y) = ({c3} - {c4})")
print(f"{proses1_1}y = {proses1_2}")

#hasil y
y= proses1_2/proses1_1

print(f"y = {proses1_2} / {proses1_1}")
print(f"y = {y}")
print("\nProses eliminasi mencari nilai X")

#eliminasi persamaan 1 untuk nilai x
x3= x1*y2
y3= y1*y2
c3= c1*y2
#eliminasi persamaan 2 untuk nilai x
x4= x2*y1
y4= y2*y1
c4= c2*y1

print(f"{x1}x + {y1}y = {c1} | {y2} | {x3}x + {y3}y = {c3}")
print(f"{x2}x + {y2}y = {c2} | {y1} | {x4}x + {y4}y = {c4}")
print("----------------------------------")
print(f"{x3}x + {y3}y = {c3}")
print(f"{x4}x + {y4}y = {c4}")
print("-------------------------------- -")

#Proses mencari nilai 1 x
proses1_1= x3-x4
#Proses mencari nilai 2 x
proses1_2= c3-c4

print(f"({x3}x - {x4}x) + ({y3}y - {y4}y) = ({c3} - {c4})")
print(f"{proses1_1}x = {proses1_2}")

#hasil x
x = proses1_2/proses1_1

print(f"x = {proses1_2} / {proses1_1}")
print(f"x = {x}")