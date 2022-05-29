

def read_file(file_name):
    file = f"{file_name}.txt"
    with open(f'./Data Files/{file}', 'r') as f:
        data = f.read()
    return data

    


file_name = input("Enter a filename: ")

try:
    data = read_file(file_name)
    print(f"Successfully opened {file_name}\n")
except Exception:
    print("Sorry, I can't find this filename")