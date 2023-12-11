#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&']

print("Welcome to the SAN Password Generator!")
nr_letters = 12
nr_symbols = 2
nr_numbers = 4

password_list = []

for SAN in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for SAN in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for SAN in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)


random.shuffle(password_list)


password = ""
for SAN in password_list:
  password += SAN

print(f"Your password is: {password}")
