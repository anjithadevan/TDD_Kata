import re

#Support different delimiters
input_data = input("enter the number string : ")


def calculate_sum(input_data):
    data_list = [int(num) for num in re.findall(r'-?\d+', input_data)]

    # Filter negative numbers
    negative_num = [num for num in data_list if num < 0]
    if negative_num:
        negative_numbers = ', '.join(str(n) for n in negative_num)
        raise ValueError(f"Negative numbers not allowed: {negative_numbers}")
    
    sum_numbers = 0
    for num in data_list:
        sum_numbers = sum_numbers + num
    return sum_numbers

try:
    print(f"Sum of numbers: {calculate_sum(input_data)}")
except ValueError as e:
    print(e) 