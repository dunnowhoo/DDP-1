running = True
while running :
      #Tampilan Menu Utama
      print("Selamat Datang di Toko Buku place Anak Chill")
      print("============================================")
      print("1. Pinjam Buku")
      print("2. Keluar")
      print("============================================")
      choice = input("Apa yang ingin anda lakukan: ")

      #Conditional jika memilih menu 1
      if (choice == '1') :
            nama = input("Masukkan nama anda: ")
            saldo = float(input("Masukkan saldo anda: "))
            membership = input("Apakah anda member? [Y/N]: ")
            percobaan = 0

            #conditional jika punya membership
            if (membership == 'Y') :
                  percobaan = 0

                  #Perulangan selama 3 kali percobaan jika ID salah
                  while percobaan < 3 :
                        id = int(input("Masukkan ID anda: "))
                        total = 0
                        # Menggunakan loop untuk menjumlahkan semua digit dengan konsep modulo
                        while id > 0:
                              digit = id % 10  # Mengambil digit paling kanan
                              total += digit  # Menambahkan digit ke total
                              id //= 10  # Menghapus digit paling kanan

                        #Jika ID benar keluar dari perulangan
                        if (total == 23) :
                              print("Login member berhasil!\n")
                              break
                        #Kembali ke menu utama jika sudah 3 kali percobaan
                        elif (percobaan == 2) :
                              print("ID anda salah!")
                              print("Program akan kembali ke menu utama\n")
                              break
                        #Memunculkan keterangan bahwa ID salah
                        else :
                              print("ID anda salah!")
                              percobaan += 1
            #Conditional jika bukan member
            elif (membership == 'N') :
                  print("Login non-member berhasil!\n")

            #Menu Katalog Buku
            while percobaan < 2 or total == 23 : #Hanya masuk ke perulangan jika input ID benar(untuk member) atau jika input ID salah 3 kali maka kembali ke menu utama
                  print("============================================")
                  print("Katalog Buku Place Anak Chill")
                  print("============================================")
                  print("X-Man (Rp 7.000/hari)")
                  print("Doraemoh (Rp 5.500/hari)")
                  print("Nartoh (Rp 4.000/hari)")
                  print("============================================")
                  print("Exit")
                  print("============================================")

                  judul_buku = input("Buku yang dipilih: ")

                  if (judul_buku.lower() == "exit") :
                        break
                  durasi = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
            
                  if (judul_buku.lower() == "x-man") :
                        if (membership == 'Y') : #harga dengan diskon
                              total_harga = durasi * 7000 * 0.8
                        else :
                              total_harga = durasi * 7000
                  elif (judul_buku.lower() == "doraemoh") :
                        if (membership == 'Y') : #harga dengan diskon
                              total_harga = durasi * 5500 * 0.8
                        else :
                              total_harga = durasi * 5500
                  elif (judul_buku.lower() == "nartoh") :
                        if (membership == 'Y') : #harga dengan diskon
                              total_harga = durasi * 4000 * 0.8
                        else :
                              total_harga = durasi * 4000
                  else :
                        print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!\n")
                        continue

                  if saldo >= total_harga:
                        saldo = saldo - total_harga
                        print(f"Berhasil meminjam buku {judul_buku} selama {durasi} hari.\nSaldo anda saat ini Rp{saldo}\n")
                  elif saldo < total_harga:
                        print(f"Tidak berhasil meminjam buku {judul_buku}! Saldo anda kurang Rp{total_harga-saldo}\n")

      else :
            #Keluar dari program
            print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
            exit()