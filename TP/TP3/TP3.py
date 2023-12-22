import matplotlib.pyplot as plt

def get_type(a_str):
  try:
    int(a_str)
    return "int"
  except:
    try:
      float(a_str)
      return "float"
    except:
      return "str"
    
def read_csv(file_name, delimiter = ','):
  try:
        #Membuka file
        with open(file_name, 'r') as file:
          # Inisialisasi List
          lines = []
          data = []
          header = []
          tipe_data = []
          for line in file.readlines() :
            lines.append(line.strip())

            if len(lines)== 1 and lines[0] == '' :
                data.append(None)
                raise Exception ("Tabel tidak boleh kosong.")

          # Mengambil header file
          header = lines[0].strip().split(delimiter)

          #Inisialisasi tipe data dengan string
          tipe_data.extend([""] * len(header))

          # Mengambil data tiap baris
          for idx, line in enumerate(lines[1:]):
              baris = line.strip().split(delimiter)
              data.append(baris)

              if len(baris) != len(header):
                  raise Exception(f"Banyaknya kolom pada baris {idx + 2} tidak konsisten.")

              # Update tipe_data
              for i, value in enumerate(baris):
                  tipe = get_type(value)
                  if idx == 0 :
                    if tipe == 'str' :
                      tipe_data[i] = 'str'
                    elif tipe == 'int' :
                      tipe_data[i] = 'int'
                    elif tipe == 'float' :
                      tipe_data[i] = 'float'
                  else :
                    if tipe == 'str':
                      tipe_data[i] = 'str'
                    elif tipe == 'int':
                      if tipe_data[i] == 'int' :
                        tipe_data[i] = 'int'
                      elif tipe_data[i] == 'float' :
                        tipe_data[i] = 'float'
                      elif tipe_data[i] == 'str' :
                        tipe_data[i] == 'str'
                    elif tipe == 'float':
                      if tipe_data[i] == 'float' :
                        tipe_data[i] = 'float'
                      elif tipe_data[i] == 'str' :
                        tipe_data[i] == 'str'
                      elif tipe_data[i] == 'int' :
                        tipe_data[i] = 'float'
          #Casting tipe data sesuai denga list tipe_data
          for value in data :
            for i in range (len(header)) :
              if tipe_data[i] == 'float' :
                value[i] = float(value[i]) 
              elif tipe_data[i] == 'str' :
                  value[i] = str(value[i])
              elif tipe_data[i] == 'int' :
                value[i] = int(value[i])

  except FileNotFoundError:
      raise Exception(f"File '{file_name}' not found.")

  return data, header, tipe_data

def to_list(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
    
    mengembalikan bagian list of lists of items atau tabel data
    pada dataframe. Gunakan fungsi ini kedepannya jika ada keperluan
    untuk akses bagian data/tabel pada dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of lists of items
  """
  return dataframe[0]

def get_column_names(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[1] adalah berisi list of column names. Gunakan fungsi ini
    kedepannya jika ada keperluan untuk akses daftar nama kolom pada
    sebuah dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of column names
  """
  return dataframe[1]
  
def get_column_types(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[2] adalah berisi daftar tipe data dari
    setiap kolom tabel. Hanya ada tiga jenis tipe data,
    yaitu "str", "int", dan "float"
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of type names
  """
  return dataframe[2]

def head(dataframe, top_n = 10):
  """
  
    -- DIBUKA KE PESERTA --
  
    top_n baris pertama pada tabel!
  
    Mengembalikan string yang merupakan representasi tabel
    (top_n baris pertama) dengan format:
    
     kolom_1|     kolom_2|     kolom_3|     ...
    ------------------------------------------- 
    value_11|    value_12|    value_13|     ...
    value_21|    value_22|    value_23|     ...
    ...         ...         ...
    
    Space setiap kolom dibatasi hanya 15 karakter dan right-justified.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    top_n (int): n, untuk penampilan top-n baris saja
    
    return (string): representasi string dari penampilan tabel.
    
    Jangan pakai print()! tetapi return string!
  """
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
  for baris in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{col:>15}" for col in baris]) + "\n"
  return out_str
  
def info(dataframe):
  """
    Mengembalikan string yang merupakan representasi informasi
    dataframe dalam format:
    
    Total Baris = xxxxx baris
    
    Kolom          Tipe
    ------------------------------
    kolom_1        tipe_1
    kolom_2        tipe_2
    ...
    
    Space untuk kolom dan tipe adalah 15 karakter, left-justified
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    
    return (string): representasi string dari info dataframe    
  """
  total_baris = len(to_list(dataframe))
  cols = get_column_names(dataframe)
  col_type = get_column_types(dataframe)
  out_str = f"Total Baris = {total_baris} baris\n\n"
  out_str += "Kolom" + " "*10 + "Tipe" + " "*11 + "\n"
  out_str += "-"*30 + "\n"
  for i, col in enumerate(cols) :
    out_str += col + " "*(15- len(col)) + col_type[i] + "\n"
  return out_str

def satisfy_cond(value1, condition, value2):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    value1 (tipe apapun yang comparable): nilai pertama
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value2 (tipe apapun yang comparable): nilai kedua
    
    return (boolean): hasil perbandingan value1 dan value2
    
  """
  if condition == "<":
    return value1 < value2
  elif condition == "<=":
    return value1 <= value2
  elif condition == ">":
    return value1 > value2
  elif condition == ">=":
    return value1 >= value2
  elif condition == "!=":
    return value1 != value2
  elif condition == "==":
    return value1 == value2
  else:
    raise Exception(f"Operator {condition} tidak dikenal.")

def select_rows(dataframe, col_name, condition, value):
  """
  Mengembalikan dataframe baru dimana baris-baris sudah
  dipilih hanya yang nilai col_name memenuhi 'condition'
  terkait 'value' tertentu.
  
  Gunakan/Call fungsi satisfy_cond(value1, condition, value2) yang
  sudah didefinisikan sebelumnya!
  
  contoh:
    select_rows(dataframe, "umur", "<=", 50) akan mengembalikan
    dataframe baru dengan setiap baris memenuhi syarat merupakan
    item dengan kolom umur <= 50 tahun.
    
  Exceptions:
    1. jika col_name tidak ditemukan,
    
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
        
    2. jika condition bukan salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    
        raise Exception(f"Operator {condition} tidak dikenal.")
  
  parameter:
  dataframe (list, list, list): sebuah dataframe
  col_name (string): nama kolom sebagai basis untuk selection
  condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
  value (tipe apapun): nilai untuk basis perbandingan pada col_name
  
  return (list, list, list): dataframe baru hasil selection atau filtering
  
  """
  # Copy header,data, dan tipe_data
  header = get_column_names(dataframe)[:]
  data = to_list(dataframe)[:]
  tipe_data = get_column_types(dataframe)[:]

  #Indeks kolom yang digunakan
  idx = get_column_names(dataframe).index(col_name)

  #Jika kolom tidak ada
  if col_name not in header :
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  #Ekstrak filtered data sesuai dengan condition
  filtered_data = [baris for baris in data if satisfy_cond(baris[idx], condition, value)]
 
  return filtered_data, header, tipe_data
  
def select_cols(dataframe, selected_cols):
  """
    Mengembalikan dataframe baru dimana kolom-kolom sudah
    dipilih hanya yang terdapat pada 'selected_cols' saja.
    
    contoh:
    select_cols(dataframe, ["umur", "nama"]) akan mengembalikan
    dataframe baru yang hanya terdiri dari kolom "umur" dan "nama".
    
    Exceptions:
      1. jika ada nama kolom pada selected_cols yang tidak
         ditemukan, 
         
           raise Exception(f"Kolom {selected_col} tidak ditemukan.")
           
      2. jika select_cols adalah list kosong [],
      
           raise Exception("Parameter selected_cols tidak boleh kosong.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    selected_cols (list): list of strings, atau list yang berisi
                          daftar nama kolom
                          
    return (list, list, list): dataframe baru hasil selection pada
                               kolom, yaitu hanya mengandung kolom-
                               kolom pada selected_cols saja.
    
  """
  #Mendapatkan header,data,dan tipe_data
  header = get_column_names(dataframe)[:]
  data = to_list(dataframe)[:]
  tipe_data = get_column_types(dataframe)[:]

  #Inisiasi List
  new_data = []
  new_header = []
  new_tipe_data = []


  for i, col in enumerate(selected_cols) :
    if col in header :
      new_header.append(col)
      idx = header.index(col)
      cond = True
      for j, value in enumerate(data) :
        #Cek apakah kolom kosong
        if value[idx] == "" :
          cond = False
          break
        else :
          #Jika data untuk kolom pertama, buat list dalam list
          if i == 0 :
            new_data.append([value[idx]])
          #Selain itu, masukkan data sesuai dengan kolom
          else :
            new_data[j].append(value[idx])

      new_tipe_data.append(tipe_data[idx])
      if not cond :
         #Jika kolom kosong
         raise Exception(f"Parameter {col} tidak boleh kosong.")

    else :
      #Jika kolom tidak ditemukan
      raise Exception(f"Kolom {col} tidak ditemukan.")

  return new_data, new_header, new_tipe_data

def count(dataframe, col_name):
  """
    mengembalikan dictionary yang berisi frequency count dari
    setiap nilai unik pada kolom col_name.
    
    Tipe nilai pada col_name harus string !
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah numerik (int atau float),
      
           raise Exception(f"Kolom {col_name} harus bertipe string.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")

    Peserta bisa menggunakan Set untuk mengerjakan fungsi ini.
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (dict): dictionary yang berisi informasi frequency count
                   dari setiap nilai unik.
  """
  # Copy Header,data
  header = get_column_names(dataframe)[:]
  data = to_list(dataframe)[:]
  variable = []
  #Inisiasi set untuk variable
  variable_set = set()
  #Inisiasi dictionary count
  variable_count = {}
  col_type = get_type(col_name)
  #Mendapatkan index kolom
  idx = header.index(col_name)
  if col_name in header :
    if col_type != 'str' :
      #Jika kolom bukan tipe string
      raise Exception(f"Kolom {col_name} harus bertipe string.") 
    if dataframe[0] == "" :
      #Jika tabel kosong
      raise Exception("Tabel kosong.")
    for value in data :
      variable.append(value[idx])
      variable_set.add(value[idx])
    
    for value in variable_set :
      #Masukkan ke dictionary {value : jumlah}
      variable_count[value] = variable.count(value)

  else :
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  return variable_count

def mean_col(dataframe, col_name):
  """
    Mengembalikan nilai rata-rata nilai pada kolom 'col_name'
    di dataframe.
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah string,
      
           raise Exception(f"Kolom {col_name} bukan bertipe numerik.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (float): nilai rataan
  """
  # Mendapatkan header,data,dan tipe_data
  header = get_column_names(dataframe)[:]
  data = to_list(dataframe)[:]
  tipe_data = get_column_types(dataframe)[:]
  #Inisiasi total data
  total = 0
  #Definisi banyak data
  num_data = len(to_list(dataframe))
  #Mendapatkan index kolom
  idx = header.index(col_name)

  if col_name in header :
    if tipe_data[idx] != 'str' :
      #Jika tabel kosong
      if len(data) == 0 :
        raise Exception("Tabel kosong.")
      else :
        for value in data :
          #Menjumlahkan data
          total += value[idx]
        #Menghitung mean
        mean = total/num_data
        return mean
      
    else :
      #Jika kolom bukan bertipe nuer
      raise Exception(f"Kolom {col_name} bukan bertipe numerik.")

  else :
    raise Exception(f"Kolom {col_name} tidak ditemukan.")

def show_scatter_plot(x, y, x_label, y_label):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    x (list): list of numerical values, tidak boleh string
    y (list): list of numerical values, tidak boleh string
    x_label (string): label pada sumbu x
    y_label (string): label pada sumbu y
    
    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.
    
    Apa itu scatter plot?
    https://chartio.com/learn/charts/what-is-a-scatter-plot/
  """
  plt.scatter(x, y)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()
  
def scatter(dataframe, col_name_x, col_name_y):
  """
    fungsi ini akan menampilkan scatter plot antara kolom col_name_x
    dan col_name_y pada dataframe.
    
    pastikan nilai-nilai pada col_name_x dan col_name_y adalah angka!
    
    Exceptions:
      1. jika col_name_x tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
           
      2. jika col_name_y tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
           
      3. jika col_name_x BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
           
      4. jika col_name_y BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name_x (string): nama kolom yang nilai-nilainya diplot pada axis x
    col_name_y (string): nama kolom yang nilai-nilainya diplot pada axis y
    
    Call fungsi show_scatter_plot(x, y) ketika mendefinisikan fungsi
    ini!
    
    return None
  """
  # Mendapatkan header,data,dan tipe_data
  header = get_column_names(dataframe)[:]
  data = to_list(dataframe)[:]
  tipe_data = get_column_types(dataframe)[:]

  #Mendapatkan index untuk kolom x dan kolom y
  idx_x = header.index(col_name_x)
  idx_y = header.index(col_name_y)

  #Inisiasi list value x dan y
  x = [] 
  y = []

  #Exception jika kolom tidak ditemukan
  if col_name_x not in header :
    raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
  if col_name_y not in header :
    raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
  #Exception jika kolom bukan bertipe numerik
  if tipe_data[idx_x] == 'str':
    raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
  if tipe_data[idx_y] == 'str':
    raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
  
  #Mendapatkan nilai dari x dan y
  for value in data :
    x.append(value[idx_x])
    y.append(value[idx_y])

  #Mendapatkan label x dan y
  x_label = col_name_x
  y_label = col_name_y
  
  show_scatter_plot(x, y, x_label, y_label)
  return None

def show_pie_chart(sizes, labels, explode = None):
    """
    Menampilkan pie chart berdasarkan ukuran dan label yang diberikan.
    
    Parameters:
    sizes (list): List nilai untuk masing-masing sektor pie.
    labels (list): List label untuk masing-masing sektor pie.
    
    Returns:
    None, tapi menampilkan pie chart.
    """
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode = explode)
    plt.axis('equal')
    plt.show()

def pie_chart(dataframe, col_name, explode=None):
    """
    Menampilkan pie chart berdasarkan data dari kolom yang diberikan pada dataframe.
    
    Parameters:
    dataframe (list, list, list): Sebuah dataframe.
    col_name (string): Nama kolom yang akan diplot sebagai pie chart.
    explode (list, optional): List yang menentukan seberapa jauh sektor pie ditarik keluar.
    
    Exceptions:
      1. Jika col_name tidak ditemukan, raise Exception.

    Returns:
    None, tapi menampilkan pie chart.
    """
    #Mendapatkan header
    header = get_column_names(dataframe)[:]

    #Jika kolom tidak ditemukan
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    
    #Membuat dictionary berisi {labels : value}
    dict = count(dataframe,col_name)

    #Mendapatkan value dan label untuk pie chart
    values = list(dict.values())
    labels = list(dict.keys())
    
    #Memanggil fungsi untuk show pie chart
    show_pie_chart(values, labels, explode)
    return None

def drop_column(dataframe, dropped_col):
    """
    Mengembalikan dataframe baru tanpa kolom yang dihapus.

    Parameters:
    dataframe (list, list, list): Sebuah dataframe.
    dropped_col (string): Nama kolom yang akan dihapus.

    Returns:
    list, list, list: DataFrame baru tanpa kolom yang dihapus.
    """
    #Mendapatkan header, data, dan tipe_data
    header = get_column_names(dataframe)[:]
    data = to_list(dataframe)[:]
    tipe_data = get_column_types(dataframe)[:]

    #Jika kolom tidak ditemukan
    if dropped_col not in header:
        raise Exception(f"Kolom {dropped_col} tidak ditemukan.")
    
    #Mendapatkan index kolom
    idx = header.index(dropped_col)
    #Menghapus Header kolom
    header.pop(idx)
    #Menghapus tipe data kolom
    tipe_data.pop(idx)
    #Menghapus data dari kolom
    for baris in data :
      baris.pop(idx)

    return data, header, tipe_data

if __name__ == "__main__":
    dataframe = read_csv("abalone.csv")
    new = drop_column(dataframe, "Sex")
    print(head(new))