import random

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

characters = ['@', '#', '$', '%', '&', '*', '?']

number_of_chars = int(input("Enter the length of the password: "))

if number_of_chars % 4 == 0:
    number_of_times = number_of_chars // 4


    def shuffle():
        upper = random.choice(upper_case)
        lower = random.choice(lower_case)
        numeric = random.choice(numbers)
        chars = random.choice(characters)

        random_elements_list = [upper, lower, numeric, chars]
        random.shuffle(random_elements_list)  # shuffled list

        return random_elements_list


    def answer():
        a = []
        b = []
        for i in range(number_of_times):
            a.append(shuffle())
        # return a

        for i in a:
            b.extend(i)
        x = ''.join(b)
        return x


    print(f'Your new {4 * number_of_times} digits password is: {answer()}')

else:
    # print("Enter a valid length of password, which is also a multiple of 4")
    quotient = number_of_chars // 4
    remainder = number_of_chars % 4

    upper1 = random.choice(upper_case)
    lower1 = random.choice(lower_case)
    numeric1 = random.choice(numbers)
    chars1 = random.choice(characters)

    random_elements_list1 = [upper1, lower1, numeric1, chars1]
    random.shuffle(random_elements_list1)  # shuffled list

    z = random.sample(random_elements_list1, remainder)


    def shuffle():
        upper = random.choice(upper_case)
        lower = random.choice(lower_case)
        numeric = random.choice(numbers)
        chars = random.choice(characters)

        random_elements_list = [upper, lower, numeric, chars]
        random.shuffle(random_elements_list)  # shuffled list

        # z = random.sample(random_elements_list, remainder)
        # print(f"{remainder} extra digits are: {z}")

        return random_elements_list


    def answer():
        a = []
        b = []

        for i in range(quotient):
            a.append(shuffle())
        # return a

        for i in a:
            b.extend(i)

        b += z
        x = ''.join(b)

        return x


    print(f'Your new {number_of_chars} digit password is: {answer()}')
