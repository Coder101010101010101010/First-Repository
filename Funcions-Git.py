# 4.13.3: Greetings
# Joe Hill
# 2.5.19


name = input("What is your name: ")

def greeting():
    print ("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# Mr. Lange
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