#fungsi 
def buka_file(txt):
    #membaca file text dan menghapus newline diganti dengan tanpa space
    data_file = open(txt,"r")
    text = data_file.readline().replace("\n", "")

    """
        Membuka file text
        Pembuatan fungsi dimana membuat dict dengan key nama hari dan value jumlah peminjaman 
    """

    #List kosong digunakan untuk menampung hari dan banyaknya buku yang dipinjam 
    data_hari = []

    #Perulangan untuk meng-update dict dari nama_hari
    while text != "" :
        nama_hari  = {"Senin":0,"Selasa":0,"Rabu":0,"Kamis":0,"Jumat":0,"Sabtu":0}
        data = text.split()
        nama_hari["Senin"] = data[2]
        nama_hari["Selasa"] = data[3]
        nama_hari["Rabu"] = data[4]
        nama_hari["Kamis"] = data [5]
        nama_hari["Jumat"] = data[6]
        nama_hari["Sabtu"] = data[7]
        print(nama_hari)
        text = data_file.readline().replace("\n", "")
        data_hari.append(nama_hari)
    data_file.close()

    #hasil yang sudah didapatkan di return kan agar dapat digunakan pada fungsi selanjutnya
    return data_hari

def favorit(buku_favorit):
    """
        Fungsi untuk mencari buku terfavorit, yang mana paling banyak dipinjam pada hari tersebut
                                                &
        Untuk mengembalikan buku favorit untuk setiap isbn  
    """

    #list kosong untuk menyimpan data buku peminjmanan terbanyak untuk setiap buku
    max_buku = []

    #Mencari buku terbanyak yang dipinjamkan untuk isbn 1 dan disimpan pada list kosong yang sudah dibuat
    nilai_max1 = buku_favorit[0]
    hari = max(nilai_max1, key = nilai_max1.get)
    jumlah = nilai_max1[hari]
    var = "{}"" "":"" ""{}".format(hari, jumlah)
    max_buku.append(var)

    #Mencari buku terbanyak yang dipinjamkan untuk isbn 2 dan disimpan pada list kosong yang sudah dibuat
    nilai_max2 = buku_favorit[1]
    hari = max(nilai_max2, key = nilai_max2.get)
    jumlah = nilai_max2[hari]
    var = ("{}"" "":"" ""{}".format(hari, jumlah))
    max_buku.append(var)

    #Mencari buku terbanyak yang dipinjamkan untuk isbn 3 dan disimpan pada list kosong yang sudah dibuat
    nilai_max3 = buku_favorit[2]
    hari = max(nilai_max3, key = nilai_max3.get)
    jumlah = nilai_max3[hari]
    var = ("{}"" "":"" ""{}".format(hari, jumlah))
    max_buku.append(var)
    
    #Mencari buku terbanyak yang dipinjamkan untuk isbn 4 dan disimpan pada list kosong yang sudah dibuat
    nilai_max4 = buku_favorit[3]
    hari = max(nilai_max4, key = nilai_max4.get)
    jumlah = nilai_max4[hari]
    var = ("{}"" "":"" ""{}".format(hari, jumlah))
    max_buku.append(var)

    #Mencari buku terbanyak yang dipinjamkan untuk isbn 5 dan disimpan pada list kosong yang sudah dibuat
    nilai_max5 = buku_favorit[4]
    hari = max(nilai_max5, key = nilai_max5.get)
    jumlah = nilai_max5[hari]
    var = ("{}"" "" "":"" ""{}".format(hari, jumlah))
    max_buku.append(var)
    
    #hasil yang didapatkan di return kan agar dapat digunakan pada fungsi selanjutnya
    return max_buku
    
def cetak_buku(favorit):
    """
    Mencetak Fungsi favorit, sesuai dengan banyaknya peminjaman buku dengan key nama hari value
    Mencetak hari dan banyaknya setiap buku yang dipinjamkan
    """
    for buku in favorit:
        print(buku)

def report(ratarata):

    #List kosong tempat penyimpanan key
    buku = []

    #membuka list dari hasil fungsi buka_file 
    for idx, dicti in enumerate(ratarata):
        hasil = dicti

    #mengakses key, value dan menyimpan value kedalam list kosong 
        for k,v in hasil.items():
            hasil = buku.append(v)
    """
        Fungsi laporan, untuk mencari rata rata seluruh buku yang di pinjam selama 6 hari 
    """

    #casting data dan memasukan key kedalam sebuat list
    casting = map(int, buku)
    List = list(casting)

    #Menghitung dan mencetak rata rata
    rata2 = sum(List)/len(buku)
    print(rata2)
        

    


# #Main Program

#membuka file text
namafile = "main.txt"
#menyimpan dan menjalankan hasil dari file text
isi_file = buka_file(namafile)

#Menyimpan fungsi favorit dan mengakses hasil dari fungsi buka_file
Buku = favorit(isi_file)
#Mencetak hasil dari fungsi favorit
cetak_buku(Buku)

#menjalankan rata-rata dan mengakses hasil dari fungsi buka_file
report(isi_file)
