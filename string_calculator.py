import re

#Allow the add method to handle new lines between numbers
input_data = input("enter the number string : ")


def calculate_sum(input_data):
    data_list = [int(num) for num in re.findall(r'\d+', input_data.replace("\n", " "))]
    sum_numbers = 0
    for num in data_list:
        sum_numbers = sum_numbers + num
    return sum_numbers


print(f"Sum of numbers: {calculate_sum(input_data)}")