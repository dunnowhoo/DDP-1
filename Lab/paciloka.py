class Hotel :
      def __init__(self, name, available_room, room_price):
            '''Fungsi ini untuk inisialisasi class Hotel'''
            self.name = name
            self.available_room = int(available_room)
            self.room_price = int(room_price)
            self.profit = 0
            self.guest = set()

      def booking(self, user, jumlah_kamar):
            '''Fungsi yang akan dipanggil ketika booking kamar hotel'''
            #Jika jumlah kamar tersedia dan saldo mencukupi
            if jumlah_kamar > 0 and jumlah_kamar <= int(self.available_room) and int(user.money) >= jumlah_kamar * self.room_price:
                  self.profit += jumlah_kamar * self.room_price   #Menambah profit hotel
                  self.available_room -= jumlah_kamar             #Mengurangi ketersediaan kamar
                  user.money -= jumlah_kamar * self.room_price    #Mengurangi saldo user
                  self.guest.add(user.name)                       #Menambah user ke daftar tamu
                  user.hotel_list.add(self.name)                  #Menambah hotel ke daftar hotel_list user
                  print(f"{user.name} berhasil melakukan booking di hotel {self.name} dengan jumlah {jumlah_kamar} kamar!")
            elif jumlah_kamar < 0 :
                  print("Jumlah kamar yang akan dipesan harus lebih dari 0!")
            else:
                print("Booking tidak berhasil!")

      def __str__(self):
          '''Fungsi yang mengkonversi object Hotel menjadi string'''
          return f"{self.name} | {', '.join(self.guest)}"

class User:
      def __init__(self, name, money):
            '''Fungsi ini untuk inisialisasi class User'''
            self.name = name
            self.money = int(money)
            self.hotel_list = set()
            
      def topup(self, jumlah_topup):
            '''Fungsi akan dipanggil ketika user melakukan topup'''
            #Jika jumlah topup lebih dari Rp 0
            if jumlah_topup > 0:
                  self.money = int(self.money) + jumlah_topup #Menambah saldo user
                  print(f"Berhasil menambahkan {jumlah_topup} ke user {self.name}. Saldo user menjadi {self.money}")
            else:
                  print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")

      def __str__(self):
          return f"{self.name} | {', '.join(self.hotel_list)}"

if __name__ == '__main__':
      #Inisialiasi List untuk menyimpan hotel dan user
      hotels = []
      users = []

      #Input data
      n_hotel = int(input("Masukan banyak hotel: "))
      n_user = int(input("Masukkan banyak user: "))

      #Iterasi untuk input atribut hotel
      for i in range (n_hotel) :
            name = input(f"Masukkan nama hotel ke-{i+1}: ")
            available_room  = input(f"Masukan banyak kamar hotel ke-{i+1}: ")
            room_price = input(f"Masukan harga satu kamar hotel ke-{i+1}: ")
            hotels.append(Hotel(name, available_room, room_price)) #Memanggil class Hotel dan dimasukkan ke list hotels

      #Iterasi untuk input atribut user
      for j in range (n_user) :
            name = input(f"Masukan nama user ke-{j+1}: ")
            money = input(f"Masukan saldo user ke-{j+1}: ")
            users.append(User(name, money)) #Memanggil class User dan dimasukkan ke dalam list users

      program = True
      #Menu Utama
      while (program) :
            print("\n=============Welcome to Paciloka!=============")
            choice = input("Masukkan Perintah: ")
            #Mencetak daftar hotel dan user yang tersedia
            if choice == '1' :
                  print("Daftar Hotel")
                  for index, hotel in enumerate(hotels, start=1):
                        print(f"{index}. {hotel.name}")
                  print("\nDaftar User")
                  for index, user in enumerate(users, start=1):
                        print(f"{index}. {user.name}")
            #Mencetak profit hotel
            elif choice == '2' :
                  hotel_name = input("Masukkan nama hotel: ")
                  found = False
                  i = 0
                  for hotel in hotels:
                        if hotel.name == hotel_name:
                              found = True
                              print(f"Hotel dengan nama {hotel_name} mempunyai profit sebesar {hotel.profit}")
                              break
                        i += 1
                        if not found and i == len(hotels): #Hotel tidak ditemukan dalam index terakhir list
                              print(f"Hotel dengan nama {hotel_name} tidak ditemukan!")
            #Mencetak saldo user
            elif choice == '3' :
                  user_name = input("Masukkan nama user: ")
                  found = False
                  i = 0
                  for user in users:
                        if user.name == user_name:
                              found = True
                              print(f"User dengan nama {user_name} mempunyai saldo sebesar {user.money}")
                              break
                        i += 1
                        if not found and i == len(users):
                              print(f"Nama user {user_name} tidak ditemukan di sistem!")
            #Menmabhakn saldo user
            elif choice == '4' :
                  user_name = input("Masukkan nama user: ")
                  found = False
                  i = 0
                  for user in users:
                        if user.name == user_name:
                              found = True
                              amount = int(input("Masukkan jumlah uang yang akan ditambahkan ke user: "))
                              user.topup(amount)
                              break
                        i += 1
                        if not found and i == len(users):
                              print(f"Nama user {user_name} tidak ditemukan di sistem!")
            #Booking Hotel
            elif choice == '5':  
                  found_user = False
                  found_hotel = False
              
                  user_name = input("Masukkan nama user: ")
                  i = 0
                  #Validasi User
                  for user in users:
                        if user.name == user_name:
                              found_user = True
                              break
                        i += 1
                        if not found and i == len(users):
                            print(f"User dengan nama {user_name} tidak ditemukan!")

                  if found_user :
                        hotel_name = input("Masukkan nama hotel: ")
                        i = 0
                        #Validasi Hotel
                        for hotel in hotels:
                              if hotel.name == hotel_name:
                                    found_hotel = True
                                    break
                              i += 1
                              if not found and i == len(hotels):
                                    print(f"Hotel dengan nama {hotel_name} tidak ditemukan!")

                  #Jika Hotel dan User tersedia
                  if found_user and found_hotel:
                        jumlah_kamar = int(input("Masukkan jumlah kamar yang akan dibooking: "))
                        user = next(user for user in users if user.name == user_name)
                        hotel = next(hotel for hotel in hotels if hotel.name == hotel_name)
                        hotel.booking(user, jumlah_kamar)
      
            #Mencetak pelanggan hotel
            elif choice == '6' :
                  hotel_name = input("Masukkan nama hotel: ")
                  found = False
                  i = 0
                  for hotel in hotels:
                        if hotel.name == hotel_name:
                              found = True
                              if len(hotel.guest) == 0 :
                                    print(f"Hotel {hotel.name} tidak memiliki pelanggan!") 
                              else :
                                    print(hotel)
                              break
                        i += 1
                        if not found and i == len(hotels):
                              print(f"Hotel dengan nama {hotel_name} tidak ditemukan!")
            #Mencetak daftar hotel yang dikunjungi user
            elif choice == '7' :
                  user_name = input("Masukkan nama user: ")
                  found = False
                  i = 0
                  for user in users:
                        if user.name == user_name:
                              found = True
                              if len(user.hotel_list) == 0:
                                    print(f"user {user.name} tidak pernah melakukan booking!")
                              else:
                                    print(user)
                              break
                        i += 1
                        if not found and i == len(users):
                              print(f"Nama user {user_name} tidak ditemukan di sistem!")
            #Keluar dari menu
            elif choice == '8' :
                  print("Terima kasih sudah mengunjungi Paciloka!")
                  program = False
            #Pilihan menu tidak sesuai
            else :
                  print("Perintah tidak diketahui! Masukkan perintah yang valid")