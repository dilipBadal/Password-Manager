#Password Generator Project
import random


class Generate:
    def __init__(self):
        self.password = ""

    def generate(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(3, 5)
        nr_symbols = random.randint(2, 3)
        nr_numbers = random.randint(3, 4)

        password_list = []

        password_list += [random.choice(letters) for char in range(nr_letters)]
        password_list += [random.choice(symbols) for char in range(nr_symbols)]
        password_list += [random.choice(numbers) for char in range(nr_numbers)]

        random.shuffle(password_list)

        self.password = "".join(password_list)

    def clear(self):
        self.password = ""
