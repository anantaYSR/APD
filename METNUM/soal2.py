import matplotlib.pyplot as plt #Library untuk grafik

x = 3.2

#titik 1
x1 = 1
y1 = 1.50

#titik 2
x2 = 2
y2 = 2.1

#titik 3
x3 = 5
y3 = 4.2

#Menampilkan langkah-langkah pengerjaan 
print(f"y= y1*(x-x2)(x-x3)/(x1-x2)(x1-x3) + y2*(x-x1)(x-x3)/(x2-x1)(x2-x3) + y3*(x-x1)(x-x2)/(x3-x1)(x3-x2) ")
print(f"y= ({y1} * ({x} - {x2}) * ({x} - {x3}) / ({x1} - {x2}) * ({x1} - {x3})) + ({y2} * ({x} - {x1}) * ({x} - {x3}) / ({x2} - {x1}) * ({x2} - {x3})) + ({y3} * ({x} - {x1}) * ({x} - {x2}) / ({x3} - {x1}) * ({x3} - {x2}))")
print(f"y= ({y1} * {round(x-x2,2)} * {round(x-x3,2)} / {x1-x2} * {x1-x3}) + ({y2} * {x-x1} * {round(x-x3,2)} / {x2-x1} * {x2-x3}) + ({y3} * {x-x1} * {round(x-x2,2)} / {x3-x1} * {x3-x2})")
print(f"y= ({y1} * {(x-x2)*(x-x3)} / {(x1-x2)*(x1-x3)}) + ({y2} * {(x-x1)*(x-x3)} / {(x2-x1)*(x2-x3)}) + ({y3} * {round((x-x1)*(x-x2),2)} / {(x3-x1)*(x3-x2)})")
print(f"y= ({y1*((x-x2)*(x-x3))} / {(x1-x2)*(x1-x3)}) + ({round(y2*((x-x1)*(x-x3)),2)} / {(x2-x1)*(x2-x3)}) + ({round(y3*((x-x1)*(x-x2)),2)} / {(x3-x1)*(x3-x2)})")
print(f"y= {y1*((x-x2)*(x-x3))/((x1-x2)*(x1-x3))} + {round(y2*((x-x1)*(x-x3))/((x2-x1)*(x2-x3)),2)} + {round(y3*((x-x1)*(x-x2))/((x3-x1)*(x3-x2)),2)}")

#Menentukan nilai y 1
yI=y1*((x-x2)*(x-x3))/((x1-x2)*(x1-x3))

#Menentukan nilai y 2
yII=y2*((x-x1)*(x-x3))/((x2-x1)*(x2-x3))

#Menentukan nilai y 3
yIII=y3*((x-x1)*(x-x2))/((x3-x1)*(x3-x2))

#menampilkan nilai y
y= round(yI+yII+yIII,2)
print(f"y= {y}")

listx=[x,x1,x2,x3]
listy=[y,y1,y2,y3]

#pengurutan nilai x pada grafik
for i in range (len(listx)-1):
    for j in range (len(listx)-1):
        if listx[j]>listx[j+1]:
            swap=listx[j]
            listx[j]=listx[j+1]
            listx[j+1]=swap

#pengurutan nilai y pada grafik
for i in range (len(listy)-1):
    for j in range (len(listy)-1):
        if listy[j]>listy[j+1]:
            swap=listy[j]
            listy[j]=listy[j+1]
            listy[j+1]=swap

#fungsi menampilkan grafik
plt.title("Grafik Interpolasi Kuadratik")
plt.plot(listx, listy, marker="o")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()     
plt.show()