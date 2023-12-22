from tkinter import *
from tkinter import messagebox

# Kelas EAN13 berisi definisi konstanta dan metode untuk menghasilkan bit dan menghitung checksum
class EAN13:
    START, END, MIDDLE = '101', '101', '01010'
    ENCODING = {
        '0': 'llllllrrrrrr',
        '1': 'llglggrrrrrr',
        '2': 'llgglgrrrrrr',
        '3': 'llggglrrrrrr',
        '4': 'lgllggrrrrrr',
        '5': 'lggllgrrrrrr',
        '6': 'lgggllrrrrrr',
        '7': 'lglglgrrrrrr',
        '8': 'lglgglrrrrrr',
        '9': 'lgglglrrrrrr'
    }
    LCODE = {
        '0': '0001101',
        '1': '0011001',
        '2': '0010011',
        '3': '0111101',
        '4': '0100011',
        '5': '0110001',
        '6': '0101111',
        '7': '0111011',
        '8': '0110111',
        '9': '0001011'
    }
    GCODE = {
        '0': '0100111',
        '1': '0110011',
        '2': '0011011',
        '3': '0100001',
        '4': '0011101',
        '5': '0111001',
        '6': '0000101',
        '7': '0010001',
        '8': '0001001',
        '9': '0010111'
    }

    # Menghasilkan string bit berdasarkan digit dan tipe (l, g, r)
    def generate_bits(self, code, number):
        if code == 'l':
            return self.LCODE[number]
        elif code == 'g':
            return self.GCODE[number]
        elif code == 'r':
            return self.GCODE[number][::-1]

    # Menghitung checksum dari suatu kode EAN-13
    def generate_checksum(self, code):
        odd_sum = sum(int(i) for i in code[0::2])
        even_sum = sum(int(i) * 3 for i in code[1::2])
        total_sum = odd_sum + even_sum
        return str((10 - total_sum % 10) % 10)

    # Mendapatkan representasi encoding dari suatu digit
    def get_encoding(self, number):
        return self.ENCODING[number]

# Kelas Barcode yang merupakan turunan dari EAN13, berisi metode untuk menghasilkan barcode
class Barcode(EAN13):
    def __init__(self, code):
        first_digit = code[0]
        other_digits = code[1:] + self.generate_checksum(code)
        encoding = self.get_encoding(first_digit)
        bits = f"{self.START}{''.join(self.generate_bits(encoding[i], other_digits[i]) for i in range(6))}{self.MIDDLE}{''.join(self.generate_bits(encoding[i], other_digits[i]) for i in range(6, 12))}{self.END}"
        self.bits = bits
        self.code = code + self.generate_checksum(code)

    def get_code(self):
        return self.code

    def get_bits(self):
        return self.bits

# Kelas GUI untuk antarmuka pengguna
class GUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x570")
        self.master.title("EAN-13 [by Fauzan Putra Sanjaya]")
        self.master.configure(bg='#c6d3e3')
        
        # Input filename
        self.label_filename = Label(master, text="Save barcode to PS file [eg: EAN13.eps]:", bg='#c6d3e3', font=("Germania One", 13, "bold"))
        self.label_filename.pack(pady=(5,0))
        self.entry_filename = Entry(master, width=30)
        self.entry_filename.pack()
        
        # Input code
        self.label_code = Label(master, text="Enter code (first 12 decimal digits):", bg='#c6d3e3', font=("Germania One", 13, "bold"))
        self.label_code.pack()
        self.entry_code = Entry(master, width=30)
        self.entry_code.pack()
        
        # Button generate
        self.generate_button = Button(master, text="Generate Barcode", command=self.generate_barcode, font=("Germania One", 12, "bold"))
        self.generate_button.pack(pady=10)
        
        # Canvas
        self.display = Canvas(master, bg="white", height=400, width=450)
        self.display.pack()

    # Mendapatkan kode dari input pengguna
    def get_code(self):
        return self.entry_code.get()

    # Mendapatkan nama file dari input pengguna
    def get_filename(self):
        return self.entry_filename.get()
    
    # Mengosongkan teks pada entry fields
    def clear_text(self):
        self.entry_filename.delete(0, 'end')  
        self.entry_code.delete(0, 'end')

    # Metode untuk membangkitkan barcode dan menampilkannya di Canvas
    def generate_barcode(self):
        filename = self.entry_filename.get()
        code = self.entry_code.get()
        condition = 0

        if len(filename) == 0 or not filename[-4:] == ".eps" and not filename[-3:] == ".ps":
            messagebox.showerror("Error", "Please enter a valid filename input.")
            condition += 1
            self.clear_text()

        if len(code) != 12 or not code.isdigit():
            messagebox.showerror("Error", "Please enter a valid code input.")
            condition += 1
            self.clear_text()

        if condition == 0:
            self.create_barcode()
            self.display.update()
            self.display.postscript(file=self.get_filename(), colormode="color")
            messagebox.showinfo("Success", "Barcode generated and saved successfully.")
            self.clear_text()
    
    # Metode untuk membuat barcode dan menampilkan di Canvas
    def create_barcode(self):
        barcode = Barcode(self.get_code())
        bits = barcode.get_bits()
        code = barcode.get_code()
        self.display.delete("all")
        self.display.create_text(230, 50, fill='Black', font=('Arial', 18, 'bold'), text='EAN-13 Barcode:')

        # Mencetak barcode
        for index in range(95):
            if bits[index] == '1':
                fill_color = 'blue' if index in [0, 1, 2, 45, 46, 47, 48, 49, 92, 93, 94] else 'black'
                height = int(313) if fill_color == 'blue' else int(293)
                self.display.create_rectangle((int((33 + index * 4)), 90, int((37 + index * 4)), height), fill=fill_color, width=0)

        # Mencetak digit code dan checksum
        self.display.create_text(28, 326, font=('Arial', 21, 'bold'), text=code[0], fill="black")
        for index in range(1, 13):
            position = int((34 + index * 28)) if 1 <= index <= 6 else int((50 + index * 28))
            self.display.create_text(position, 326, font=('Arial', 21, 'bold'), text=f'{code[index]}', fill="black")
        self.display.create_text(230, 380, fill='#FFA500', font=('Arial', 21, 'bold'), text=f'Check Digit: {code[-1]}')

if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()