#Mengatur loop menu utama
program = True
#Inisiasi list kosong
list_nama = []
list_nilai = []
#Inisiasi index orang ke-n
idx = 0

while program :
      print("Selamat datang di Database Nilai Dek Depe")
      print("1. Tambah data ke database")
      print("2. Baca data dari database")
      print("3. Update data di database")
      print("4. Hapus data dari database")
      print("5. Keluar")
      case = input("Masukkan kegiatan yang ingin dilakukan: ")

      #Kasus 1
      if case == '1' : 
            nama = input("Masukkan nama: ")
            try :
                  #Nama terdapat dalam list
                  check = list_nama.index(nama.lower())
                  print("Nama sudah terdapat di dalam database\n")
                  continue
            except ValueError :
                  #Nama belum ada, memasukkan nama ke dalam list 
                  list_nama.append(nama.lower())
            i = 0
            while True :
                  nilai = input(f"Masukkan nilai Lab {i+1} (ketik STOP untuk selesai): ")
                  if nilai.lower() == "stop" :
                        print(f"Berhasil menambahkan {i} nilai untuk {nama} ke database\n")
                        idx += 1
                        break
                  try :
                        int(nilai) #Check apakah angka?
                  except ValueError :
                        #Input nilai bukan angka
                        print("Masukkan nilai dalam bentuk angka\n")
                        continue
                  #Validasi input angka sesuai dalam rentang 0 - 100
                  if (int(nilai) >= 0 and int(nilai) <= 100) :
                        #Membuat list dalam list
                        if i == 0 and idx == 0 :
                              list_nilai.append([nilai])
                        #Membuat list dalam list untuk orang selanjutnya
                        elif i == 0 :
                              list_nilai.append([nilai])
                        #Menambahkan nilai ke dalam list orang ke-idx
                        else :
                              list_nilai[idx].extend([nilai])
                        i += 1
                  else :
                        print("Masukkan dalam rentang 1 - 100")
      #Kasus 2
      elif case == '2' :
            try :
                  nama = input("Masukkan nama: ")
                  idx_nama = list_nama.index(nama.lower())
            except ValueError :
                  #Nama tidak tersedia
                  print("Nama tidak ada dalam database\n")
                  continue
            else :
                  try :
                        idx_nilai = input("Masukkan nilai Lab ke berapa yang ingin dilihat: ")
                        check = list_nilai[int(idx_nama)][int(idx_nilai)-1]
                        print(f"Nilai Lab {idx_nilai} {nama} adalah {float(list_nilai[int(idx_nama)][int(idx_nilai)-1])}\n")
                  except IndexError :
                        #Diluar jangkauan lab yang sudah dikerjakan
                        print(f"Tidak terdapat nilai untuk Lab {idx_nilai}\n")
                        continue
                  except TypeError :
                        #Nilai telah dihapus
                        print(f"Tidak terdapat nilai untuk Lab {idx_nilai}\n")
                        continue
      #Kasus 3
      elif case == '3' :
            try :
                  nama = input("Masukkan nama: ")
                  idx_nama = list_nama.index(nama.lower())
            except ValueError :
                  #Nama tidak tersedia
                  print("Nama tidak ada dalam database\n")
                  continue
            try :
                  idx_nilai = input("Masukkan nilai Lab ke berapa yang ingin diubah: ")
                  check = list_nilai[int(idx_nama)][int(idx_nilai)-1]
            except IndexError :
                  #Diluar jangkauan lab yang sudah dikerjakan
                  print(f"Tidak terdapat nilai untuk Lab {idx_nilai}\n")
                  continue
            while True :
                  nilai_baru = input(f"Masukkan nilai baru untuk Lab {idx_nilai}: ")
                  try :
                        int(nilai_baru) #Check apakah angka?
                  except ValueError :
                        #Nilai bukan dalam bentuk angka
                        print("Masukkan nilai dalam bentuk angka\n")
                        continue
                  if (int(nilai_baru) >= 0 and int(nilai_baru) <= 100) :
                        nilai_lama = list_nilai[idx_nama][int(idx_nilai)-1]
                        list_nilai[int(idx_nama)][int(idx_nilai)-1] = nilai_baru
                        try :
                              print(f"Berhasil mengupdate nilai Lab {idx_nilai} Kak Kulus dari {float(nilai_lama)} ke {float(nilai_baru)}\n")
                              break
                        except TypeError:
                              #Nilai sudah dihapus
                              print(f"Tidak terdapat nilai untuk Lab {idx_nilai}")
                              break
                  else :
                        print("Masukkan dalam rentang 1 - 100")
      #Kasus 4
      elif case == '4' :
            try :
                  nama = input("Masukkan nama: ")
                  idx_nama = list_nama.index(nama.lower())
            except ValueError :
                  #Nama tidak tersedia
                  print("Nama tidak ada dalam database\n")
                  continue
            try :
                  idx_nilai = input("Masukkan nilai Lab ke berapa yang ingin dihapus: ")
                  check = list_nilai[int(idx_nama)][int(idx_nilai)-1] #Check IndexError
                  float(check) #Check TypeError
            except IndexError :
                  #Diluar jangkauan lab yang sudah dikerjakan
                  print(f"Tidak terdapat nilai untuk Lab {idx_nilai}\n")
                  continue 
            except TypeError :
                  #Nilai telah dihapus
                  print(f"Tidak terdapat nilai untuk Lab {idx_nilai}\n")
                  continue
            #Menghapus nilai dari list
            list_nilai[int(idx_nama)][int(idx_nilai)-1] = None
            print(f"Berhasil menghapus nilai Lab {idx_nilai} {nama} dari database\n")
      #Kasus 5 (Keluar dari program)
      elif case == '5' :
            print("Terimakasih telah menggunakan Database Nilai Dek Depe")
            program = False
      #Pilihan tidak tersedia (kembali ke menu utama)
      else :
            pass