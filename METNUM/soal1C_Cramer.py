#Metode cramer

a1=int(input("x1: "))
b1=int(input("y1: "))
c1=int(input("Hasil: "))

a2=int(input("x2: "))
b2=int(input("y2: "))
c2=int(input("Hasil: "))

x=(c1*b2-c2*b1)/(a1*b2-a2*b1)
y=(c2*a1-c1*a2)/(a1*b2-a2*b1)

print(f"Nilai X adalah {x} dan nilai Y adalah {y} dari persamaan {a1}x+{b1}y={c1} dan persamaan {a2}x+{b2}y={c2}")