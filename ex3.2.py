def calculate_numbers_list(numbers_list):
    return sum(numbers_list) / len(numbers_list)

number_list = []

for i in range (5):
    number_list.append(float(input("Please write number : ")))
    i += 1


print(calculate_numbers_list(number_list))
# def calculate_average(average):
# print(calculate_numbers_list(numbers_list))