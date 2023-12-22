import tkinter as tk
from tkinter import messagebox


class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Paciloka Hotel Booking")
        self.master.geometry("350x600")  # Menyesuaikan ukuran jendela

        self.dict_hotel = {
            'hotel1': [10, 250000, 'H1'],
            'hotel2': [12, 500000, 'H2'],
            'hotel3': [10, 7500000, 'H3'],
            'hotel4': [1, 1000000, 'H4'],
            'hotel5': [10, 900000, 'H5'],
            'hotel6': [10, 6000000, 'H6']
        }

        self.dict_fasilitas_tambahan = { 'None': 0, 'Extra Bed': 50000, 'Breakfast': 100000, 'Fancy Dinner': 150000}

        # Menampilkan informasi hotel di awal
        self.display_hotel_info()

        # Menampilkan menu pemesanan (input)
        self.show_booking_menu()

        #Menampilkan pesan pembuka
        messagebox.showinfo("Welcome", "Selamat Datang di Paciloka Booking Hotel! 🏨")

    def show_booking_menu(self):
        # Label dan Entry untuk Nama Pengguna
        self.username_label = tk.Label(self.master, text="Nama Pengguna:", justify='left', anchor='w')
        self.username_entry = tk.Entry(self.master, justify='left')
        self.username_label.place(x=10, y=10)
        self.username_entry.place(x=160, y=10)

        # Label dan Entry untuk Nama Hotel
        self.hotel_label = tk.Label(self.master, text="Nama Hotel:", anchor='w')
        self.hotel_entry = tk.Entry(self.master, justify='left')
        self.hotel_label.place(x=10, y=40)
        self.hotel_entry.place(x=160, y=40)

        # Label dan Dropdown untuk Fasilitas Tambahan
        self.fasilitas_label = tk.Label(self.master, text="Fasilitas Tambahan:", anchor='w')
        self.fasilitas_var = tk.StringVar(self.master)
        self.fasilitas_var.set(list(self.dict_fasilitas_tambahan.keys())[0])
        self.fasilitas_dropdown = tk.OptionMenu(self.master, self.fasilitas_var, *self.dict_fasilitas_tambahan.keys())
        self.fasilitas_label.place(x=10, y=70)
        self.fasilitas_dropdown.place(x=158, y=65)

        # Label dan Entry untuk Jumlah Kamar
        self.room_label = tk.Label(self.master, text="Jumlah Kamar:", anchor='w')
        self.room_entry = tk.Entry(self.master, justify='left')
        self.room_label.place(x=10, y=100)
        self.room_entry.place(x=160, y=100)

        # Tombol Pesan Kamar
        self.book_button = tk.Button(
            self.master, text="Pesan Kamar", command=self.booking)
        self.book_button.place(x=10, y=130)

        # Tombol Exit
        self.exit_button = tk.Button(
            self.master, text="Exit", command=self.exit_app)
        self.exit_button.place(x=10, y=160)

    def booking(self):
        #Mendapatkan username dan hotel_name
        username = self.username_entry.get()
        hotel_name = self.hotel_entry.get()
        #Validasi input harus berupa bilangan bulat
        try:
            num_rooms = int(self.room_entry.get())
        except:
            messagebox.showerror(
                "Error", "Jumlah kamar harus berupa bilangan bulat")
            return
        #Validasi nama minimal 3 huruf
        if len(username) < 3:
            messagebox.showerror(
                "Error", "Nama pengguna harus memiliki minimal 3 huruf.")
            return
        #Validasi nama hotel
        if hotel_name not in self.dict_hotel:
            messagebox.showerror("Error", "Nama hotel tidak valid.")
            return

        available_rooms, room_price, hotel_code = self.dict_hotel[hotel_name]
        fasilitas_price = self.dict_fasilitas_tambahan[self.fasilitas_var.get()]
        fasilitas = self.fasilitas_var.get()

        if num_rooms <= 0:
            messagebox.showerror("Error", "Jumlah kamar harus lebih dari 0.")
        elif num_rooms > available_rooms:
            messagebox.showerror(
                "Error", "Jumlah kamar yang tersedia tidak mencukupi.")
        else:
            total_price = (num_rooms * room_price) + \
                (fasilitas_price * num_rooms)
            remaining_rooms = available_rooms - num_rooms
            user_ticket_number = f"{hotel_code}/{remaining_rooms}/{username[:3].upper()}"

            self.dict_hotel[hotel_name] = [remaining_rooms,
                                           room_price, hotel_code]  # Update available rooms
            self.username_entry.delete(0, tk.END)
            self.room_entry.delete(0, tk.END)

            # Menampilkan informasi hotel terupdate
            self.display_hotel_info()

            # Menampilkan kembali menu pemesanan (input)
            self.show_booking_menu()

            messagebox.showinfo(
                "Booking Berhasil",
                f"Booking berhasil!\n\nNama Pengguna: {username}\nHotel: {hotel_name}\nJumlah Kamar: {num_rooms}\nFasilitas Tambahan : {fasilitas}\nTotal Biaya: Rp{total_price}\nNomor Tiket: {user_ticket_number}"
            )

    def display_hotel_info(self):
        # Hapus semua widget sebelumnya agar bisa diupdate
        for widget in self.master.winfo_children():
            widget.destroy()
        

        # Tampilkan informasi hotel
        info_text = "Informasi Hotel:\n\n"
        for hotel_name, details in self.dict_hotel.items():
            available_rooms, room_price, hotel_code = details
            info_text += f"  ▶ Nama Hotel: {hotel_name} - Kode Hotel: {hotel_code}\n"
            info_text += f"      Jumlah Kamar Tersedia: {available_rooms}\n"
            info_text += f"      Harga Kamar: Rp{room_price}\n"

        info_text += f"\nHarga Fasilitas Tambahan per Kamar :\n"
        for fasilitas, harga in self.dict_fasilitas_tambahan.items():
            info_text += f"  ➥ {fasilitas}: Rp{harga}\n"

        info_text += "\n"

        info_label = tk.Label(
            self.master, text=info_text, justify='left', anchor='w', )
        info_label.place(x=10, y=200)

    def exit_app(self):
        # Menampilkan messagebox terimakasih sebelum keluar
        response = messagebox.showinfo(
            "Terima Kasih", "Terimakasih telah menggunakan aplikasi Paciloka.")
        if response == "ok":
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()