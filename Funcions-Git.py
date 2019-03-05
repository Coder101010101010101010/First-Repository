# 4.13.3: Greetings
# Joe Hill
# 2.5.19


name = input("What is your name: ")

def greeting():
    print ("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# 2.11.19
# Joe Hill


x = 10

def print_something():
     x = 3
     print('\n', x)

print('\n', x)
print_something()


# 4.13.6: Fuctions and Variables, part 3
# Joe Hill
# 2.18.19


def print_number(x):
    print('\n', x)

print_number(13)
print_number(23)


# 4.14.4: Name and Age
# Joe Hill
# 2.18.19


def name_and_age(name, age):
    print('\n','Hi, my name is', name, 'and I am', str(age), 'years old')

name_and_age('Bob', 25)
name_and_age('Man', '4,000,000,000')


# 4.14.5: Defualt Parameter Values
# Joe Hill
# 2.19.19


def print_two_numbers(x, y = 20):
    print('First number:', x)
    print('Second Number: ' + str(y))

print_two_numbers(34, 45)
print_two_numbers(78)


# 4.14.6: Print Sum
# Joe Hill
# 2.19.19


def print_sum(x, y):
    print(x + y)

print_sum(54,99)


# 4.16.4: Enter Name and Age using the Try and Except Rule
# Joe Hill
# 20.20.19

name = input('Enter your name: ')

age = -1

age = input('Enter your age: ')

try:
    age = int(input('Enter your age: '))
except ValueError:
    print('\n''That wasn\'t an integer for your age')

print('Name:',name)
print('Age:', age)


