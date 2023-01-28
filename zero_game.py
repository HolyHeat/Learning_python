def calculate_numbers_list(numbers_list):
    return sum(numbers_list) / len(numbers_list)

number_list = []

ask_user_for_numbers = True

while ask_user_for_numbers != 0:
    user_input = float(input("Please write number : "))
    if user_input == 0.0:
        ask_user_for_numbers = False
        print("You win, congrats ! ")
    else:
        number_list.append(user_input)

print("The average sum of numbers you entered = " + str(calculate_numbers_list(number_list)))