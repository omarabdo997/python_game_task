import random

x = random.randint(1, 9)
y = random.randint(1, 9)
z = random.randint(1, 9)
answerlist = [x, y, z]


def check_pres_in_array(item, arry):
    for i in arry:
        if (item == i):
            return True
    else:
        return False


while (y == x):
    y = random.randint(1, 9)
while (z == x or z == y):
    z = random.randint(1, 9)
print("You need to enter 3 numbers from 1-9 in 3 slots in a certain order digits can not be repeated")
while (1):
    in1 = int(input("Enter first number : "))
    in2 = int(input("Enter second number : "))
    in3 = int(input("Enter third number : "))
    if (in1 == in2 or in1 == in3 or in2 == in3):
        print("Do not repeat numbers !")
    elif (in1 == 0 or in2 == 0 or in3 == 0):
        print("Zero is not included in the game!")
    elif (in1 >= 10 or in2 >= 10 or in3 >= 10):
        print("use numbers between 1 to 9 only!")
    elif (in1 == x and in2 == y and in3 == z):
        break
    elif (in1 == x or in2 == y or in3 == z):
        print("match")
    elif (check_pres_in_array(in1, answerlist) or check_pres_in_array(in2, answerlist) or check_pres_in_array(in3, answerlist)):
        print("close")
    else:
        print("nope")
print("Congratulations you won")
