#Task 1
def read_file(file_name):
    try:
        file = f"{file_name}.txt"
        with open(f'./Data Files/{file}', 'r') as f:
            data = f.read()
        return data
    except Exception:
        pass


file_name = input("Enter a filename: ")

try:
    data = read_file(file_name)
    print(f"Successfully opened {file_name}\n")
except Exception:
    print("Sorry, I can't find this filename")


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


def check_valid(line):
    lst_values = line.split(",")
    if len(lst_values) > 26 or len(lst_values) < 26:
        result = "invalid"
    elif len(lst_values) == 26 and len(lst_values[0]) > 1:
        result = "valid"
    else:
        result = "invalid"
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
            "ID": ma_hs,
            "answer": line.split(",")[1:],
            "type": check 
        })
    df = pd.DataFrame(list_data)
    return df

report_df = report(file_name)
print(report_df)
total_line = count_check(file_name)
print("total line: ",total_line[0] + total_line[1])
print("total line invalid: ", total_line[1])

