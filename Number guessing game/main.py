# from Error import Error
import random


def guesser(a, b):
    try:
        num = int(input("Please input the number: "))
    except ValueError:
        num = int(input("Invalid number! Please input again: "))
    random_num = random.randint(a, b)
    while num != random_num:
        if num > random_num:
            print("Value too high")
        elif num < random_num:
            print("Value too low")
        num = int(input("Input again: "))
    print("Congratulations ! The correct number is : " + str(random_num))


print("Welcome! To The number guessing game ! ")
range_1, range_2 = input("Please input the range: ").split()
# print(range_1, range_2)
guesser(int(range_1), int(range_2))
