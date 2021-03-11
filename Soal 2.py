#menampilkan judul halaman
print("WELCOME TO MY PERSONAL LIFE")

#memasukkan variabel yang digunakan
nama_depan = "Afiq"
nama_belakang = "Ramadhan"
nama = nama_depan + " " + nama_belakang
tahun_lahir = 2001
tahun_sekarang = 2021
bulan_lahir = 12
bulan_sekarang = 3
umur = (tahun_sekarang - tahun_lahir) * 12 + (bulan_lahir - bulan_sekarang)
alamat = "Langenharjo, Sukoharjo"
gender = "Laki-Laki"
agama = "Islam"
prodi = "Teknik Industri"
univ = "Universitas Sebelas Maret"
tinggiku = 165
berat_badanku = 55
berat_idealku = (tinggiku - 100) - (tinggiku / 10)


#proses mencetak variabel
print("Namaku", nama)
print('Aku berusia', umur)
print("Umurku sekarang dalam bulan adalah", umur)
print("Aku tinggal di", alamat)
print("Aku beragama", agama)
print("Sekarang aku sedang menempuh pendidikan di", univ, "di jurusan", prodi)
print("Aku memiliki berat badan ideal yaitu", berat_idealku)

#menghitung berat badan ideal sesorang
print("Apa kamu ingin tau berat badan idealmu?")
ingin = int(input("Aku akan membantumu menghitung berat idealmu, apa kamu ingin: "))
if ingin == 1:
    print("Aku perlu tahu berat dan tinggimu")
    #input nilai tinggi dan berat badan
    tinggi = float(input("Masukkan tinggi badanmu: "))
    berat = float(input("Masukkan berat badanmu: "))
    berat_ideal =(tinggi - 100) - (tinggi / 10)
    #menampilkan hasil perhitungan
    print("Berat idealmu adalah", berat_ideal)
elif ingin == 0:
    print("Oke")

