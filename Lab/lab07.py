#Dictionary untuk menampung relasi {parent : [children]}
relasi = {}

#Input data relasi
print("Masukkan data relasi:")
def input_relasi () :
      '''Fungsi ini untuk input data relasi'''
      data = input()
      if data == 'SELESAI' :
            pass
      else :
            data = data.strip().split()
            parent = data[0]
            child = data[1]
            #Jika parent belum ada di relasi, buat list kosong untuk menyimpan keturunan
            if parent not in relasi :    
                  relasi[parent] = []
            #Masukkan child  ke dalam list keturunan
            relasi[parent].append(child) 
            return input_relasi()

def cek_keturunan(relasi, parent, child) :
      '''Fungsi untuk mengecek keturunan'''
      #Jika parent tidak terdapat dalam relasi
      if parent not in relasi : 
            return False
      #Jika child merupakan keturunan parent
      if child in relasi[parent] : 
            return True
      #Mengecek secara rekursif apakah ada 'child' dari setiap keturunan parent , True jika ada, False jika tidak ada
      return any(cek_keturunan(relasi, keturunan, child) for keturunan in relasi[parent]) 

def cetak_keturunan(relasi, parent) :
      '''Fungsi untuk mencetak keturunan'''
      if parent in relasi :
            #Mencetak values (list) dari parent
            print("- " + " ".join(relasi[parent]))
            for keturunan in relasi[parent] :
                  #Mendapatkan keturunan dari setiap child parent
                  cetak_keturunan(relasi, keturunan)

def jarak_generasi(relasi, parent, child) :
      '''Fungsi untuk menghitung jarak generasi'''
      #Base case
      if child == parent : 
                  #Return 0 karena sudah tidak dapat naik silsilah
                  return 0
      else :
            #Menjadikan parent dari child sebelumya menjadi new_child lalu di rekursi sampai ketemu dengan parent yang diinput
            new_child = "".join([key for key, keturunan in relasi.items() if child in keturunan])
            #Setiap naik silsilah ditambah 1
            return 1 + jarak_generasi(relasi, parent, new_child)

#Memanggil fungsi input data relasi
input_relasi()
#Menu utama
while True :
      print("=====================================================================")
      print("Selamat Datang di Relation Finder! Pilihan yang tersedia:")
      print("1. CEK_KETURUNAN")
      print("2. CETAK_KETURUNAN")
      print("3. JARAK_GENERASI")
      print("4. EXIT")
      case = input("Masukkan pilihan: ")

      if case == '1' :
            parent = input("Masukkan nama parent: ")
            child = input("Masukkan nama child: ")
            if cek_keturunan(relasi, parent, child) :
                  print(f"{child} benar merupakan keturunan dari {parent}")
            else :
                  print(f"{child} bukan merupakan keturunan dari {parent}")

      elif case == '2' :
            parent = input("Masukkan nama parent: ")
            cetak_keturunan(relasi, parent)

      elif case == '3' :
            parent = input("Masukkan nama parent: ")
            child = input("Masukkan nama child: ") 
            if parent == child :
                  print(f"{parent} memiliki hubungan dengan {child} sejauh 0")
            elif cek_keturunan(relasi, parent, child) :
                  jarak = jarak_generasi(relasi, parent, child)
                  print(f"{parent} memiliki hubungan dengan {child} sejauh {jarak}")
            else :
                  print(f"Tidak ada hubungan antara {parent} dengan {child}")

      elif case == '4' :
            print("=====================================================================")
            print("Terima kasih telah menggunakan Relation Finder!")
            exit()

      else :
            pass