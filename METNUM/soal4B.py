# Metode Numerik Nomor 4 b

import math
import numpy as np
from os import system

def f(x):
    # Persamaan x^2 - 2x -2
    fungsi = math.pow(x,2) - 2*x - 2 
    return fungsi


def regulaFalsi(a, b, toleransi, n):
    system("cls")
    persamaan = ['x^2-2*x-2']
    A = [2]
    B = [3]
    C = [15]
    i = 0
    fa = f(a)
    diketahui = {
    "x0" : A,
    "x1" : B,
    "Fungsi" : persamaan,
    "iterasi maksimum" : C
    
    }
    print ("diketahui pada soal")
    print ("iterasi akan berhenti ketika sudah mencapai iterasi maksimum atau fx lebih dari 0 atau error\n\n")
    print ("TABEL REGULA FALSI")

    print("--------------------------------------------------------------------------------------------------")
    print("%-20s %-20s %-20s %-20s %-20s" % ("n", "a", "b", "x", "f(x)/toleransi"))
    print("--------------------------------------------------------------------------------------------------") 

    # Dilakukan iterasi sampai dengan n yang diinginkan
    while(i <= n):
        x = (a*f(b)-b*f(a))/(f(b) - f(a))
        fx = f(x)
        i += 1

        # Jika f(x) = 0 atau akar telah ditemukan program akan berhenti.
        # Jika |f(x)| < angka toleransi program akan berhenti. Artinya nilai toleransi/error telah dicapai.
        if (fx == 0 or np.abs(f(x)) < toleransi):
            print(f"\nNilai x didapatkan pada saat iterasi ke {i-1}, dengan nilai x = {x}")
            break
        # Jika tidak maka iterasi akan terus berjalan sampai keadaan di atas.
        else:
            print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, a, b, x, f(x)))
        
        # Syarat metode tertutup, pada kasus ini Regula Falsi
        if (fa*fx > 0):
            a = x
        else:
            b = x

regulaFalsi(2, 3, 0.001, 15)

