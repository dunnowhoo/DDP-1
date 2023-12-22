res1 = set() #set untuk isi tugas mahasiswa pertama
res2 = set() #set untuk isi tugas mahasiswa kedua
konten = []  #list berisi keseluruhan isi file
database_mhs = {} #database dictionary mahasiswa {nama : npm}
database_matkul = set() #database set daftar matkul

#Membuka dan mengekstrak isi file
with open ('Lab6.txt', 'r') as f:
      for line in f.readlines() :
            konten.append(line.strip())

#Mengekstrak nama dan npm ke dalam dictionary
for element in konten :
      if ';' in element :
                  temp = element.split(';')
                  database_mhs[temp[0]] = temp[1]
                  database_matkul.add(temp[2])

def cek_mahasiswa (nama) :
      '''Fungsi ini untuk mengecek apakah mahasiswa terdapat dalam data'''
      if nama not in database_mhs :
            if nama not in database_mhs.values() :
                  print("Informasi mahasiswa tidak ditemukan.\n")
                  return True

print("Selamat datang di program Plagiarism Checker!")
program = True
#Main program
while program :
      print("=====================================================================")
      matkul = input("Masukkan nama mata kuliah yang ingin diperiksa: ")

      if matkul.lower() == 'exit' :
            print("Terima kasih telah menggunakan program Plagiarism Checker!")
            exit()
      if matkul not in database_matkul :
            print(f"{matkul} tidak ditemukan\n")
            continue

      mahasiswa1 = input("Masukkan nama/NPM mahasiswa pertama:")
      if cek_mahasiswa(mahasiswa1) :
            continue

      mahasiswa2 = input("Masukkan nama/NPM mahasiswa kedua:")
      if cek_mahasiswa(mahasiswa2) :
            continue

      i = 0
      #Mengambil isi tugas sesuai dengan mahasiswa dan matkul yang dicari dan dimasukkan ke set 
      for element in konten :
            if (mahasiswa1 in element) and (matkul in element) :
                  temp = str(konten[i+2]).split()
                  len1 = len(temp)
                  res1 = set(temp)
            
            if (mahasiswa2 in element) and (matkul in element) :
                  temp = str(konten[i+2]).split()
                  len2 = len(temp)
                  res2 = set(temp) 
            i += 1

      #Mengganti NPM menjadi nama mahasiswa
      for nama, npm in database_mhs.items():
            if npm == mahasiswa1 :
                  mahasiswa1 = nama
            if npm == mahasiswa2 :
                  mahasiswa2 = nama

      #Menghitung tingkat kemiripan
      intersection = res1 & res2
      persentase = format(len(intersection)/len(res1) * 100, '.2f')

      #Klasifikasi tingkat plagiarisme
      if float(persentase) < 31 :
            tingkat_plagiarisme = "tidak terindikasi plagiarisme"
      elif float(persentase) < 70 :
            tingkat_plagiarisme = "terindikasi plagiarisme ringan"
      else :
            tingkat_plagiarisme = "terindikasi plagiarisme"

      #Mencetak hasil
      print("============================= Hasil =================================")
      print(f"Tingkat kemiripan tugas {matkul} {mahasiswa1} dan {mahasiswa2} adalah {persentase}%. {mahasiswa1} dan {mahasiswa2} {tingkat_plagiarisme}.\n")