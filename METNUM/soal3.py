# TANPA INPUTAN

from numpy import*

#~~~~~~inisialisasi matrik augment~~~~~#
A = array([
            [6.,12.,-3.,6.,-21],\
            [12.,6.,9.,-3.,51],\
            [18.,-9.,12.,12.,57],\
            [-6.,3.,-6.,-3,-27]])
print ('\n\nNilai Matriks =\n',A)

#===== METODE ELIMINASI GAUSS JORDAN =========#
n=len(A)
#~~~~~~proses triangularisasi/Eliminasi Guas Jordan~~~~~~~~~~#
for k in range(0,n-1):

    for i in range(k+1,n):
        m=A[i][k]/A[k][k]

        for j in range(0,n+1):
            A[i][j]=A[i][j]-m*A[k][j]

#~~~~~~proses substitusi-mundur~~~~~~~~#
X = zeros((n,1))
X[n-1][0]=A[n-1][n]/A[n-1][n-1]
for j in range(n-2,-1,-1):
    S=0
    for i in range(j+1,n):
        S=S+A[j][i]*X[i][0]
        X[j][0]=(A[j][n]-S)/A[j][j]
#======================================#
print ('\nHasil Eleminasi Guass Jordan =\n',X)


# DENGAN INPUTAN
# import numpy as np
# import sys

# # Reading number of unknowns
# n = int(input('Masukan Jumlah Matriks : '))

# # Making numpy array of n x n+1 size and initializing 
# # to zero for storing augmented matrix
# a = np.zeros((n,n+1))

# # Making numpy array of n size and initializing 
# # to zero for storing solution vector
# x = np.zeros(n)

# # Reading augmented matrix coefficients
# print('Masukan Koefesien Matriks :')
# for i in range(n):
#     for j in range(n+1):
#         a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# #~~~~~~proses triangularisasi/eleminasi Guass Jordan~~~~~~~~~~#
# for i in range(n):
#     if a[i][i] == 0.0:
#         sys.exit('Tidak boleh nilai pembagi = 0!')
        
#     for j in range(i+1, n):
#         ratio = a[j][i]/a[i][i]
        
#         for k in range(n+1):
#             a[j][k] = a[j][k] - ratio * a[i][k]

# #~~~~~~proses substitusi-mundur~~~~~~~~#
# x[n-1] = a[n-1][n]/a[n-1][n-1]

# for i in range(n-2,-1,-1):
#     x[i] = a[i][n]
    
#     for j in range(i+1,n):
#         x[i] = x[i] - a[i][j]*x[j]
    
#     x[i] = x[i]/a[i][i]

# # Displaying solution
# print('\nHasil dari Guass Jordan SPL  nya adalah: ')
# for i in range(n):
#     print('X%d = %0.2f' %(i,x[i]), end = '\t')

