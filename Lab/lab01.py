#Melakukan input pesan, angka 1, dan angka 2
pesan = input("Pesan Kelompok Zog: ")
angka1 = int(input("Angka 1: "))
angka2 = int(input("Angka 2 : "))

#Mengubah pesan hex string menjadi byte string
pesan_hex = bytes.fromhex(pesan)

#Mengubah pesan byte string menjadi sebuah string 
pesan_string = pesan_hex.decode("ASCII")

#Menghitung password dan mengubahnya ke biner
password = bin(angka1 * angka2 * 13)

#Melakukan pencetakan pesan yang telah ditranslate dan password dalam biner
print('Pesan "' + pesan_string + '" telah diterima dengan password "' + password +'".')