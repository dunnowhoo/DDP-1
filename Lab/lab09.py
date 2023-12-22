class Person:
    def __init__(self, name, payment, stamina):
        # Konstruktor untuk inisialisasi objek Person
        self.__name = name  # Variabel name bersifat private
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0

    def get_name(self):
        # Getter untuk mendapatkan nilai variabel name
        return self.__name

    def get_payment(self):
        # Getter untuk mendapatkan nilai variabel payment
        return self.__payment

    def get_stamina(self):
        # Getter untuk mendapatkan nilai variabel stamina
        return self.__stamina

    def get_total_work(self):
        # Getter untuk mendapatkan nilai variabel total_work
        return self.__total_work

    def set_stamina(self, new_stamina):
        # Setter untuk mengubah nilai variabel stamina
        self.__stamina = new_stamina

    def set_total_work(self, new_total_work):
        # Setter untuk mengubah nilai variabel total_work
        self.__total_work = new_total_work

    def is_available(self, cost_stamina):
        # Mengecek apakah Person dapat bekerja berdasarkan stamina yang cukup
        return self.__stamina >= cost_stamina

    def pay_day(self):
        # Menghitung gaji yang diperoleh berdasarkan rumus payment * total_work
        return self.__payment * self.__total_work

    def work(self, cost_stamina):
        # Melakukan pekerjaan dan mengurangi stamina
        if self.is_available(cost_stamina):
            self.__stamina -= cost_stamina
            self.__total_work += 1
            return True
        else:
            return False

    def __str__(self):
        # Representasi string objek Person
        class_name = self.__class__.__name__
        name = self.__name
        total_work = self.__total_work
        stamina = self.__stamina
        payday = self.pay_day()

        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payday:20}"


class Manager(Person):
    def __init__(self, name, payment, stamina):
        # Konstruktor untuk inisialisasi objek Manager
        super().__init__(name, payment, stamina)
        self.__list_worker = []  # List untuk menyimpan objek Worker

    def get_list_worker(self):
        # Getter untuk mendapatkan nilai variabel list_worker
        return self.__list_worker

    def hire_worker(self, name):
        # Merekrut Worker baru dan menambahkannya ke list_worker
        if name.lower() not in [worker.get_name().lower() for worker in self.__list_worker]:
            # Default payment dan stamina untuk Worker baru
            new_worker = Worker(name, 5000, 100)
            self.__list_worker.append(new_worker)
            self.set_stamina(self.get_stamina() - 10)
            self.set_total_work(self.get_total_work() + 1)
            print(f"Berhasil mendapat pegawai baru: {name}")
        else:
            self.set_stamina(self.get_stamina() - 10)
            print("Sudah ada!")

    def fire_worker(self, name):
        # Memecat Worker dari list_worker
        for worker in self.__list_worker:
            if worker.get_name().lower() == name.lower():
                self.__list_worker.remove(worker)
                self.set_stamina(self.get_stamina() - 10)
                self.set_total_work(self.get_total_work() + 1)
                print(f"Berhasil memecat {name}")
                return None
        self.set_stamina(self.get_stamina() - 10)
        print("Nama tidak ditemukan")

    def give_work(self, name, bonus, cost_stamina):
        # Memberikan pekerjaan kepada Worker
        for worker in self.__list_worker:
            if worker.get_name().lower() == name.lower():
                print("Hasil cek ketersediaan pegawai:")
                if worker.work(bonus, cost_stamina):
                    self.set_stamina(self.get_stamina() - 10)
                    self.set_total_work(self.get_total_work() + 1)
                    print("Pegawai dapat menerima pekerjaan")
                    print("========================================")
                    print(f"Berhasil memberi pekerjaan kepada {name}")
                    return
                else:
                    self.set_stamina(self.get_stamina() - 10)
                    print(f"{name} tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup.")
                    return
        self.set_stamina(self.get_stamina() - 10)
        print(f"Pegawai {name} tidak ditemukan")


class Worker(Person):
    def __init__(self, name, payment, stamina):
        # Konstruktor untuk inisialisasi objek Worker
        super().__init__(name, payment, stamina)
        self.__payment = payment
        self.__total_work = 0
        self.__bonus = 0  # Variabel bonus bersifat private
          
    def work(self, bonus, cost_stamina):
        # Melakukan pekerjaan dan menambahkan bonus
        if super().work(cost_stamina):
            self.set_bonus(self.get_bonus() + bonus)
            self.__total_work += 1
            return True
        return False

    def get_bonus(self):
        # Getter untuk mendapatkan nilai variabel bonus
        return self.__bonus

    def set_bonus(self, new_bonus):
        # Setter untuk mengubah nilai variabel bonus
        self.__bonus = new_bonus
    def pay_day(self):
        # Menghitung gaji yang diperoleh berdasarkan rumus payment * total_work + bonus
        return self.__payment * self.__total_work + self.get_bonus()


def main():
    # Input data manajer
    name = input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))
    manager = Manager(name, payment, stamina) 
    
    # Menu utama
    while manager.is_available(1):
        print("""
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """)

        choice = int(input("Masukkan pilihan: "))

        if choice == 1:
            # Menampilkan status manajer dan pegawai
            print(manager)
            for worker in manager.get_list_worker():
                print(worker)

        elif choice == 2:
            # Memberikan tugas kepada pegawai
            name = input("Tugas akan diberikan kepada: ")
            bonus = int(input("Bonus pekerjaan: "))
            cost_stamina = int(input("Beban stamina: "))
            manager.give_work(name, bonus, cost_stamina)

        elif choice == 3:
            # Merekrut pegawai baru
            new_worker = input("Nama pegawai baru: ")
            manager.hire_worker(new_worker)

        elif choice == 4:
            # Memecat pegawai
            fired_worker = input("Nama pegawai yang akan dipecat: ")
            manager.fire_worker(fired_worker)

        elif choice == 5:
            # Keluar dari program
            print("----------------------------------------")
            print("Berhenti mengawasi hotel, sampai jumpa !")
            print("----------------------------------------")
            exit()

    print("----------------------------------------")
    print("Stamina manajer sudah habis, sampai jumpa !")
    print("----------------------------------------")

if __name__ == "__main__":
    main()