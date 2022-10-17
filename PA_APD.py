import sys
import os
def clear():
    os.system("cls" if os.name=="nt" else "clear")

# UTILITY
def printc(text, color):
  Colour = ("Black","Red","Green","Yellow","Blue","Purple","Cyan","White")
  SelectedColour = Colour.index(color) + 30
  print(f"\033[0;{SelectedColour};40m{text}\033[0;37;40m")

def partition(array, start, end, key):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high][key] >= pivot[key]:
            high = high - 1
        while low <= high and array[low][key] <= pivot[key]:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high
def quick_sort(array, start, end, key):
   if start >= end:
      return
   p = partition(array, start, end, key)
   quick_sort(array, start, p - 1, key)
   quick_sort(array, p + 1, end, key)


def linear_search(arr, keyword):
    result = []
    for item in arr:
        is_found = False
        for key, value in item.items():
            is_found = keyword.lower() in str(value).lower()
            if is_found:
                break
        if is_found:
            result.append(item)
    return result
array = [
    {"nama": "Ananta", "nim": 2109106024, "helm": "Ya", "jenis_kendaraan": "Motor", "plat": "KT 2101 AB", "lokasi_parkir": "Gedung Baru Teknik",  
    "tanggal" : "23-02-2022", "no_hp": 6282255447867},
    {"nama": "Herni", "nim": 2109106001, "helm": "Tidak", "jenis_kendaraan": "Mobil", "plat": "KT 2102 CD", "lokasi_parkir": "Gedung Baru Teknik",  
    "tanggal" : "23-02-2022", "no_hp": 6287756396875},
    {"nama": "Mikey", "nim": 2009106002, "helm": "Tidak", "jenis_kendaraan": "Mobil", "plat": "KT 2123 DS", "lokasi_parkir": "Gedung Lama Teknik",  
    "tanggal" : "23-02-2022", "no_hp": 6280980564167},
    {"nama": "Nande", "nim": 2009106003, "helm": "Ya", "jenis_kendaraan": "Motor", "plat": "KT 2131 CR", "lokasi_parkir": "Gedung Lama Teknik",  
    "tanggal" : "23-02-2022", "no_hp": 6282243236575},
    {"nama": "Draken", "nim": 1909106004, "helm": "Ya", "jenis_kendaraan": "Motor", "plat": "KT 2153 UH", "lokasi_parkir": "GOR 27",  
    "tanggal" : "23-02-2022", "no_hp": 6282255447867}
]

def data_parkiran():
    clear()
    data={}
    while True:
        try:
            data["nama"]=str(input("Masukkan nama: "))
            data["nim"]=int(input("Masukkan NIM: "))
            data["helm"]=str(input("Apakah membawa helm? (Ya/Tidak) "))
            data["jenis_kendaraan"]=str(input("Masukkan jenis kendaraan (Mobil/Motor): "))
            plat=str(input("Masukkan nomor kendaraan: "))
            data["plat"]=plat.upper()
            print("""
            1. Gedung Baru Teknik
            2. Gedung Lama Teknik
            3. GOR 27
            """)
            lokasi=int(input("Masukkan pilihan: (1/2/3) "))
            if lokasi==1:
                data["lokasi_parkir"]="Gedung Baru Teknik"
            elif lokasi==2:
                data["lokasi_parkir"]="Gedung Lama Teknik"
            elif lokasi==3:
                data["lokasi_parkir"]="GOR 27"
            else:
                print("Pilihan tidak ada")
            data["tanggal"]=str(input("Masukkan tanggal: (DD-MM-YYYY) "))
            data["no_hp"]=int(input("Masukkan nomor HP/Whatsapps: "))
            array.append(data)
            break
        except:
            print("\n \033[31mInputan anda salah silahkan masukan ulang\033[0m ")
            input("\33[94mTekan enter untuk melanjutkan\33[0m ")
    clear()
        

def output(key):
    print("Nama             : ", key["nama"])
    print("Nim              : ", key["nim"])
    print("Membawa helm     : ", key["helm"])
    print("Jenis kendaraan  : ", key["jenis_kendaraan"])
    print("Nomor kendaraan  : ", key["plat"])
    print("Tempat parkir    : ", key["lokasi_parkir"])
    print("Tanggal parkir   : ", key["tanggal"])
    print("Nomor Telepon    : ", key["no_hp"])

def tampilan_data():
    clear()
    for y, x in enumerate(array):
        x.update({"loker": int(y)+1})
        print("\nNomor Loker      : ", x["loker"])
        output(x)
    input("\33[94m\nTekan enter untuk melanjutkan\33[0m ")

def ubah_data():
    tampilan_data()
    while True:
        try:
            loker=int(input("\n\033[32mMasukkan nomor loker yang ingin di ubah:\033[0m "))
            break
        except:
            print("\n\033[31mInputan anda salah silahkan masukan ulang \033[0m")
    clear()
    for data in array:
        if data["loker"]==loker:
            while True:
                try:
                    nama=str(input("Masukkan nama: "))
                    data["nama"]=nama
                    nim=int(input("Masukkan NIM: "))
                    data["nim"]=nim
                    helm=str(input("Apakah membawa helm? (Ya/Tidak) "))
                    data["helm"]=helm
                    data["jenis_kendaraan"]=str(input("Masukkan jenis kendaraan (Mobil/Motor): "))
                    plat=str(input("Masukkan nomor kendaraan: "))
                    data["plat"]=plat.upper()
                    print("""
                    1. Gedung Baru Teknik
                    2. Gedung Lama Teknik
                    3. GOR 27
                    """)
                    lokasi=int(input("Masukkan pilihan: (1/2/3) "))
                    if lokasi==1:
                        data["lokasi_parkir"]="Gedung Baru Teknik"
                    elif lokasi==2:
                        data["lokasi_parkir"]="Gedung Lama Teknik"
                    elif lokasi==3:
                        data["lokasi_parkir"]="GOR 27"
                    else:
                        printc("Pilihan tidak ada","Red")
                    tanggal=str(input("Masukkan tanggal: (DD-MM-YYYY) : "))
                    data["tanggal"]=tanggal
                    hp=int(input("Masukkan nomor HP/Whatsapps: "))
                    data["no_hp"]=hp
                    print("\n\033[92mData berhasil diubah!\033[0m")
                    input("\33[94mTekan enter untuk melanjutkan\33[0m ")
                    break
                except:
                    print("\n\033[31mInputan anda salah silahkan masukan ulang\033[0m")
def hapus_data():
    tampilan_data()
    while True:
        try:
            urutan=int(input("\nNomor loker ke berapa yang ingin dihapus? "))
            break
        except:
            print("\n\033[31mInputan anda salah silahkan masukan ulang \033[0m")
    clear()
    for data in array:
        if data["loker"]==urutan:
            print("\nNomor Loker      : ", data["loker"])
            output(data)
            delete=str(input("\n\033[32mApakah ingin menghapus (y/n):\033[0m "))
            if delete=="y":
                for index in range(len(array)):
                    if array[index]["loker"]==urutan:
                        del array[index]
                        break
            print("\n\033[92mData berhasil dihapus!\033[0m")
            input("\33[94mTekan enter untuk melanjutkan\33[0m")
    clear()
def menu_crud():
    clear()
    print("""\033[93m
        =================================
                MENU MANAJEMEN DATA
        =================================
        [1] Tampilan Data
        [2] Tambah Data
        [3] Ubah Data
        [4] Hapus Data
        [5] Menu Utama
        \033[0m""")  
    
    while True:
        try:
            pilih=int(input("\nMasukkan pilihan anda (1/2/3/4/5): "))
            break
        except:
            print("\n\033[31mInputan anda salah silahkan masukan ulang \033[0m")
            
    if pilih==1:
        tampilan_data()
        menu_crud()
    elif pilih==2:
        data_parkiran()
        menu_crud()
    elif pilih==3:
        ubah_data()
        menu_crud()        
    elif pilih==4:
        hapus_data()
        menu_crud()
    elif pilih==5:
        clear()
        menu_utama()
    clear()
        
def menu_pengurutan():
    clear()
    print("""\033[93m
                ===========================================
                            MENU PENGURUTAN DATA
                ===========================================
                [1] Pengurutan Berdasarkan Nama
                [2] Pengurutan Berdasarkan NIM
                [3] Pengurutan Berdasarkan Nomor Kendaraan
                [4] Menu Utama
                \033[0m""")
    
    while True:
        try:
            pilihan=int(input("Masukkan pilihan: (1/2/3/4) "))
            break
        except:
            print("\n\033[31mInputan anda salah silahkan masukan ulang \033[0m")
            
    if pilihan==1:
        clear()
        quick_sort(array, 0, len(array) - 1, "nama")
        for x in array:
            output(x)
            print("\n")
        input("\33[94m\nTekan enter untuk melanjutkan\33[0m ")

        menu_pengurutan()
    elif pilihan==2:
        clear()
        quick_sort(array, 0, len(array) - 1, "nim")
        for x in array:
            output(x)
            print("\n")
        input("\33[94m\nTekan enter untuk melanjutkan\33[0m ")
        menu_pengurutan()
    elif pilihan==3:
        quick_sort(array, 0, len(array) - 1, "plat")
        for x in array:
            output(x)
            print("\n")
        input("\33[94m\nTekan enter untuk melanjutkan\33[0m ")
        menu_pengurutan()
    elif pilihan==4:
        clear()
        menu_utama()
    else:
        print("\033[31mPilihan tidak ada \033[0m")
    input("\33[94m\nTekan enter untuk melanjutkan\33[0m ")
    clear()

def menu_pencarian():
    clear()
    print("""\033[93m
    1. Nama
    2. NIM
    3. Helm (ya/tidak)
    4. Jenis kendaraan (mobil/motor)
    5. Plat nomor kendaraan
    6. Lokasi parkir
        -.Gedung Baru Teknik
        -.Gedung Lama Teknik
        -.Gor 27
    7. Tanggal (DD-MM-YY)
    8. No Hp/WA
    \033[0m""")
    cari=input("\nMasukkan data di atas yang ingin dicari : ")
    print("\n")
    searched = linear_search(array, cari)
    if searched !=[]:
        for i in searched:
            output(i)
            print("\n")
            
    else:
        print("\033[31mData Tidak Ditemukan\n\033[0m")
    input("\33[94m\nTekan enter untuk melanjutkan\33[0m ")
    clear()
    menu_utama()
        
def menu_utama():
    print("""\033[93m
            =================================
                        MENU UTAMA
            =================================
            [1] Manajement Data 
            [2] Pengurutan Data
            [3] Pencarian Data
            [4] Stop Program
        \033[0m""")
    
    while True:
        try:
            pilih=int(input("Masukkan pilihan: (1/2/3/4): "))
            break
        except:
            print("\n \033[31mInputan anda salah silahkan masukan ulang \033[0m")
            
    clear()
    if pilih==1:
        menu_crud()
        clear()
    elif pilih==2:
        menu_pengurutan()
        clear()
    elif pilih==3:
        clear()
        menu_pencarian()
    elif pilih==4: 
        sys.exit()
    clear()
        

menu_utama()