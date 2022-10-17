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