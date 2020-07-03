import random, string

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
number_of_pass = int(input("Enter a number of password to generate : "))
pass_size = int(input("Enter the max size of the passwords : "))

for passwd in range(0, number_of_pass):
    for size in range(pass_size):
        rand_char = random.randint(0, len(characters) -1)
        password = password + characters[rand_char]
    
    print(password)
    password = ""


