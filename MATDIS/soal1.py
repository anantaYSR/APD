def main(a, b):
    hasil = cari_pbb(a,b)
    print("PBB (%d, %d) = %d" % (a,b,hasil))
    

def cari_pbb(a,b):

    print ("=======================================")  
    print ("====== PERSAMAAN KOMBINASI LANJAR =====")  
    print ("=======================================\n")  
    # a selalu lebih besar dari b
    if (b > a):
        b,a = a,b

    jumlah_persamaan = []

    while (a % b != 0):
        q,r = a//b, a%b
        jumlah_persamaan.append(q)
        
        print("%d = %d(%d) + %d" % (a,b,q,r))
        a = b
        b = r
    print ("=======================================\n")    
    return r

main(1242, 1986)

