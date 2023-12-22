import os
import time
import sys

#Fungsi untuk mencari atribut file
def file_attributes(content):
    # Inisialisasi variabel
    file_name = None
    provinsi = None
    klasifikasi = None
    sub_klasifikasi = None
    lembaga_peradilan = None
    attributes = content.split()

    # Untuk setiap atribut, pisahkan dengan '=' untuk mendapatkan nama atribut dan nilainya
    for attribute in attributes:
        name_value = attribute.split('=')
        if len(name_value) == 2:
            name = name_value[0].strip()
            value = name_value[1].strip('"')

            # Masukkan nilai ke variabel yang sesuai
            if name == 'id':
                file_name = value
            elif name == 'provinsi':
                provinsi = value
            elif name == 'klasifikasi':
                klasifikasi = value
            elif name == 'sub_klasifikasi':
                sub_klasifikasi = value
            elif name == 'lembaga_peradilan':
                lembaga_peradilan = value

    # Mencetak nilai dalam format yang diinginkan
    output = '{:<40} {:>15} {:>15} {:>30} {:>20}'.format(str(file_name[:40])+".xml", str(provinsi[:15]), str(klasifikasi[:15]), str(sub_klasifikasi[:30]), str(lembaga_peradilan[:20]))
    print(output)

#Fungsi untuk mencari file
def search_files(section, keyword1, operator=None, keyword2=None):
    # Mulai menghitung waktu
    start_time = time.time()
    files_found = []

    # Tentukan direktori tempat file berada
    directory = "D:/Coding/Python/Indonesia Law/indo-law-main/dataset"
    for file in os.listdir(directory):
        if file.endswith(".xml"):
            with open(os.path.join(directory, file), 'r') as f:
                content = f.read().lower().replace('\n', ' ')
            
            # Jika pengguna memilih bagian tertentu dari dokumen
            if section == "kepala_putusan" or section == "identitas" or section == "riwayat_penahanan" or section == "riwayat_perkara" or section == "riwayat_tuntutan" or section == "riwayat_dakwaan" or section == "fakta" or section == "fakta_hukum" or section == "pertimbangan_hukum" or section == "amar_putusan" or section == "penutup" or section == "putusan":
                section_start = content.find('<'+section+'>')
                section_end = content.find('</'+section+'>')
                # Cek apakah tag bagian ada dalam konten
                if section_start != -1 and section_end != -1:
                    # Jika ya, ambil teks di antara tag bagian
                    text_content = content[section_start+len(section)+2:section_end]
                else:
                    # Jika tidak, lewati file ini dan lanjutkan ke file berikutnya
                    continue
            elif section == "all":
                if ('<'+str(keyword1)+'>') in content :
                    content = content.replace('<'+str(keyword1)+'>', '')
                    content = content.replace('</'+str(keyword1)+'>', '')
                if ('<'+str(keyword2)+'>') in content :
                    content = content.replace('<'+str(keyword2)+'>', '')
                    content = content.replace('</'+str(keyword2)+'>', '')
                text_content = content
            else :
                print("Tidak ada section tersebut")
                sys.exit(1)


            # Cek apakah kata kunci ada dalam teks
            if operator is None:
                if keyword1 in text_content:
                    files_found.append(file)
                    file_attributes(content)
            elif operator.lower() == "and":
                if keyword1 in text_content and keyword2 in text_content:
                    files_found.append(file)
                    file_attributes(content)
            elif operator.lower() == "or":
                if keyword1 in text_content or keyword2 in text_content:
                    files_found.append(file)
                    file_attributes(content)
            elif operator.lower() == "andnot":
                if keyword1 in text_content and keyword2 not in text_content:
                    files_found.append(file)
                    file_attributes(content)
            else :
                print("Mode harus berupa AND, OR atau ANDNOT.")
                sys.exit(1)

    # Hitung waktu pencarian
    end_time = time.time()
    search_time = end_time - start_time

    return files_found, search_time

#Main Function
arg_count = len(sys.argv)

if arg_count == 3:
    section = sys.argv[1].lower()
    keyword1 = sys.argv[2].lower()
    files_found, search_time = search_files(section, keyword1)
elif arg_count == 5:
    section = sys.argv[1].lower()
    keyword1 = sys.argv[2].lower()
    operator = sys.argv[3].lower()
    keyword2 = sys.argv[4].lower()
    files_found, search_time = search_files(section, keyword1, operator, keyword2)
else:
    print("Argumen program tidak benar.")
    sys.exit(1)

total_files = len(files_found)

print()
print("Banyaknya dokumen yang ditemukan = ", total_files)
print("Total waktu pencarian = {:.3f}".format(search_time))