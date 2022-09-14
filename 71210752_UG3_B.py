#Irenne Dwita Natalia
#71210752
#Unguided3

angka = int(input("Masukkan range data: "))
faktorial = 1
dict_hasil = dict()
for i in range(angka):
    import math
    faktorial = math.factorial(i)
    hasil = (f'{faktorial}')
    dict_hasil[i] = hasil
print(dict_hasil)


