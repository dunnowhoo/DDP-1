import sys

# Helper function: Print table headers
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

# Function to print the entire table content.
def print_table(filename):
    try:
        with open(filename, "r") as f:
            print_headers()
            for i, line in enumerate(f.readlines()):
                name, price, screensize, ram = line.strip().split("\t")
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(i, name, price, screensize, ram))
    except FileNotFoundError:
        print("Maaf, file input tidak ada")

# Function to search for a specific substring, Case insensitive.
def search_phone(filename, keyword):
    try:
        with open(filename, "r") as f:
            print_headers()
            data = [line.strip().split("\t") for line in f.readlines()]
            results = [row for row in data if keyword.lower() in row[0].lower()]
            for i, result in enumerate(results, start=1):
                name, price, screensize, ram = result
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(i, name, price, screensize, ram))
            print("Jumlah data hasil pencarian: ", len(results))
    except FileNotFoundError:
        print("Maaf, file input tidak ada")

# Function to get descriptive statistics for a specific column.
def desc_stat(filename, column):
    try:
        with open(filename, "r") as f:
            data = [line.strip().split("\t") for line in f.read().splitlines()]
            if column not in range(4):
                print("Kolom tidak valid")
                return
            values = [float(row[column]) for row in data]
            min_val = min(values)
            max_val = max(values)
            avg_val = sum(values) / len(values)
            print("Minimum: {:.2f}".format(min_val))
            print("Maksimum: {:.2f}".format(max_val))
            print("Rata-rata: {:.2f}".format(avg_val))
    except FileNotFoundError:
        print("Maaf, file input tidak ada")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

    # Call the necessary functions here.
    print_table(file_path)
    search_phone(file_path, key)
    desc_stat(file_path, column_num)
