# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknowns
n = int(input('Masukan Jumlah Matriks : '))

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Masukan Koefesien Matriks :')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

#~~~~~~proses triangularisasi/eleminasi Guass Jordan~~~~~~~~~~#
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Tidak boleh nilai pembagi = 0!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

#~~~~~~proses substitusi-mundur~~~~~~~~#
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

# Displaying solution
print('\nHasil dari Guass Jordan SPL  nya adalah: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')