from task1 import file_name, read_file


#Task 2
def count_check(file_name):
    file = read_file(file_name)
    file = file.split("\n")
    valid = 0
    invalid = 0
    for line in file:
        check = check_valid(line)[0] 
        if check == "valid":
            valid += 1
        else:
            invalid += 1
    return valid, invalid


def check_valid(line):
    lst_values = line.split(",")
    if len(lst_values) > 26 or len(lst_values) < 26:
        result = "invalid"
        error = "does not contain exactly 26 values"
    elif len(lst_values) == 26 and len(lst_values[0]) > 1:
        result = "valid"
        error = None
    else:
        result = "invalid"
        error = "unknown error"
    return result, error


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
        check = check_valid(line)[0]
        error = check_valid(line)[1]
        list_data.append({
            "ID": ma_hs,
            "answer": line.split(",")[1:],
            "type": check,
            "error": error 
        })
    df = pd.DataFrame(list_data)
    return df

report_df = report(file_name)
print(report_df)
total_line = count_check(file_name)
print("total line: ",total_line[0] + total_line[1])
print("total line valid: ", total_line[0])
print("total line invalid: ", total_line[1])