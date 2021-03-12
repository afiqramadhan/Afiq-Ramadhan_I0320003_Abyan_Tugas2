import math

#menampilkan informasi program
print("Menghitung Luas Persegi Panjang")

#input nilai panjang dan lebar
panjang = float(input("Masukkan nilai panjang: "))
lebar = float(input("Masukkan nilai lebar: "))

#menghitung luas persegi panjang
luas_persegi_panjang = panjang * lebar

#menampilkan hasil perhitungan
print("Luas Persegi Panjang: ", luas_persegi_panjang)


#menampilkan informasi program
print("Menghitung Luas Lingkaran")

#input nilai diameter
d = float(input("Masukkan nilai diameter: "))

#menghitung luas lingkaran
luas_lingkaran = 3.14 * (d ** 2) / 4

#menampilkan hasil perhitungan
print("Luas Lingkaran: ", luas_lingkaran)

#menampilkan informasi program
print("Menghitung Luas Permukaan Kubus")

#input nilai panjang sisi kubus
s = float(input("Masukkan panjang sisi kubus: "))

#menghitung luas permukaan kubus
luas_permukaan_kubus = (s ** 2) * 6

#menampilkan hasil perhitungan program
print("Luas Permukaan Kubus: ",luas_permukaan_kubus)

#menampilkan informasi program
print("Konversi Celcius ke Skala Lain")

#input besar suhu dalam Celcius
C = float(input("Masukkan Besar Suhu (Celcius): "))

#melakukan konversi suhu
Reamur = 4 * C / 5
Fahrenheit = (9 * C / 5) + 32
Kelvin  = C + 273

#menampilkan hasil konversi suhu
print("Reamur: ", Reamur)
print("Fahrenheit: ", Fahrenheit)
print("Kelvin: ", Kelvin)


#menampilkan informasi program
print("Konversi Reamur ke Skala Lain")

#input besar suhu dalam Celcius
R = float(input("Masukkan Besar Suhu (Reamur): "))

#melakukan konversi suhu
Fahrenheit = (9 * R / 4) + 32
Kelvin  = (5 * R / 4) +273
Celcius = 5 * R /4

#menampilkan hasil konversi suhu
print("Fahrenheit: ", Fahrenheit)
print("Kelvin: ", Kelvin)
print("Celcius: ", Celcius)