input_data = input("enter the number string comma separated : ")


def calculate_sum(input_data):
    data_list = input_data.split(',')
    sum_numbers = 0
    for num in data_list:
        sum_numbers = sum_numbers + int(num)
    return sum_numbers


print(f"Sum of numbers: {calculate_sum(input_data)}")