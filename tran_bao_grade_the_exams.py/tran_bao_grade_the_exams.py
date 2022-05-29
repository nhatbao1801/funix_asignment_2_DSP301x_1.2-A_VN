#Task 1
from unittest import result


def read_file(file_name):
    file = f"{file_name}.txt"
    with open(f'D:\Funix\Data Files\{file}', 'r') as f:
        data = f.read()
    return data


file_name = input("Enter a filename: ")

# try:
#     data = read_file(file_name)
#     print(f"Successfully opened {file_name}\n", data)
# except Exception:
#     print("Sorry, I can't find this filename")


#Task 2
def count_check(file_name):
    file = read_file(file_name)
    file = file.split("\n")
    valid = 0
    invalid = 0
    for line in file:
        check = check_valid(line) 
        if check == "valid":
            valid += 1
        else:
            invalid += 1
    return valid, invalid

print()




######
def check_valid(line):
    if ",," in line:
        result = "invalid"
    else:
        result = "valid"
    return result


import pandas as pd

def report(file_name):
    """Function print report
    """
    file = read_file(file_name)
    file = file.split("\n")

    list_data = []

    for line in file:
        #split line by ",": return ["ma_hs", "result1", "result2",...]
        ma_hs = line.split(",")[0]
        check = check_valid(line)
        
        list_data.append({
            "ma_hs": ma_hs,
            "type": check 
        })
    df = pd.DataFrame(list_data)
    return df

df = report(file_name)
print(df)
