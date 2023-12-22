while True :
      print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")
      nama_input = input("Masukkan nama file input daftar makanan: ")
      nama_output = input("Masukkan nama file output: ")
      try:
            input_file = open(f"{nama_input}", "r")
            output_file = open(f"{nama_output}", "w")
            break
      except FileNotFoundError:
            print("Maaf, file input tidak ada")

while True :
      #Tampilan Menu Utama
      print("Apa yang ingin kamu lakukan?")
      print("================================================")
      print("1. Tampilkan daftar makanan pertama")
      print("2. Tampilkan daftar makanan kedua")
      print("3. Tampilkan gabungan makanan dari dua daftar")
      print("4. Tampilkan makanan yang sama dari dua daftar")
      print("5. Keluar")
      print("================================================")
      choice = input("Masukkan aksi yang ingin dilakukan: ")

      # Inisialisasi variabel string untuk daftar makanan pertama dan kedua
      daftar_makanan_1 = ""
      daftar_makanan_2 = ""
      # Inisialisasi variabel string untuk gabungan makanan
      gabungan_makanan = ""
      # Inisialisasi variabel string untuk makanan yang sama
      makanan_sama = ""
      
      def clean(nama):
            nama2 = ""
            i = 0
            while (len(nama) != 0) :
                  try :
                        idx = int(nama.index(",")) + 1
                  except ValueError :
                        nama2 += nama.lower()
                        i += 1
                        break

                  if (nama[:idx].lower() in nama2) :
                        nama = nama[idx:]
                        pass
                  else :
                        nama2 += nama[:idx].lower()
                        i += 1 
            return nama2.lower()
      
      #Conditional 1
      if (choice == '1') :
            print("Daftar makanan pertama:")
            output_file = open(f"{nama_output}", "a")
            print("Daftar makanan pertama:",file = output_file)
            input_file = open(f"{nama_input}", "r")
            lines = input_file.readlines()  # Baca kembali file inputprint("daftar_makanan")
            for line in lines:
                  # Mencari indeks titik dua (:)
                  colon_index = line.index(':')

                  # Mengambil nomor daftar makanan
                  nomor_daftar = line[:colon_index].strip()

                  # Mengambil daftar makanan
                  daftar_makanan = line[colon_index + 1:].strip()

                  # Membersihkan dan menggabungkan makanan
                  daftar_makanan = clean(daftar_makanan)

                  # Cetak daftar makanan pertama
                  if nomor_daftar == "Daftar Makanan 1":
                        print(daftar_makanan.lower(),'\n')
                        print(daftar_makanan.lower(),'\n',file = output_file)
            input_file.close()
            output_file.close()
      
      #conditional 2
      elif(choice == '2'):
            print("Daftar makanan kedua:")      
            output_file = open(f"{nama_output}", "a")
            print("Daftar makanan kedua:",file = output_file)   
            input_file = open(f"{nama_input}", "r")
            lines = input_file.readlines()  # Baca kembali file input
            for line in lines:
                  # Mencari indeks titik dua (:)
                  colon_index = line.index(':')

                  # Mengambil nomor daftar makanan
                  nomor_daftar = line[:colon_index].strip()

                  # Mengambil daftar makanan
                  daftar_makanan = line[colon_index + 1:].strip()

                  # Membersihkan dan menggabungkan makanan
                  daftar_makanan = clean(daftar_makanan)

                  # Cetak daftar makanan kedua
                  if nomor_daftar == "Daftar Makanan 2":
                        print(daftar_makanan.lower(),'\n')
                        print(daftar_makanan.lower(),'\n',file = output_file)
            input_file.close()
            output_file.close()
      elif(choice == '3'):
            input_file = open(f"{nama_input}", "r")
            output_file = open(f"{nama_output}", "a")
            print("Gabungan makanan favorit dari kedua daftar:")
            print("Gabungan makanan favorit dari kedua daftar:",file = output_file)
            lines = input_file.readlines()  # Baca kembali file input
            for line in lines:
                  # Mencari indeks titik dua (:)
                  colon_index = line.index(':')

                  # Mengambil nomor daftar makanan
                  nomor_daftar = line[:colon_index].strip()

                  # Mengambil daftar makanan
                  daftar_makanan = line[colon_index + 1:].strip()

                  # Membersihkan dan menggabungkan makanan
                  daftar_makanan = clean(daftar_makanan)

                  # Memisahkan makanan ke daftar yang sesuai
                  if nomor_daftar == "Daftar Makanan 1":
                        daftar_makanan_1 = daftar_makanan.lower()
                  elif nomor_daftar == "Daftar Makanan 2":
                        daftar_makanan_2 = daftar_makanan.lower()
            
            # Menggabungkan dua daftar makanan
            gabungan_makanan = daftar_makanan_1 +","+ daftar_makanan_2
            clean_gabungan_makanan = clean(gabungan_makanan)
            print(clean_gabungan_makanan, "\n")
            print(clean_gabungan_makanan,'\n', file = output_file)
            input_file.close()
            output_file.close()

      elif(choice == '4'):
            input_file = open(f"{nama_input}", "r")
            lines = input_file.readlines()  # Baca kembali file input
            # Cetak makanan yang sama
            print("Makanan yang sama dari dua daftar:")
            print(makanan_sama)
            input_file.close()
      elif(choice == '5'):
           print("Terima kasih telah menggunakan program ini!")
           print(f"Semua keluaran telah disimpan pada file {nama_output}")
           input_file.close()
           output_file.close()
           exit()
      else:
           pass
      
