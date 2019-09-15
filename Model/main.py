import turtle

print("Started python")
print("hello")

# playing with turtle

my_turtle = turtle.Turtle()


# for i in range(20):
#     my_turtle.forward(50)
#     my_turtle.left(144)
#
# my_turtle.forward(100)
#
# for i in range(20):
#     my_turtle.forward(i * 10)
#     my_turtle.left(144)
#
# my_turtle.forward(100)
#
# # for loop
# for i in range(20):
#     my_turtle.forward(50)
#     my_turtle.left(246)


# function
def square(lenght, angle):
    for i in range(4):
        my_turtle.forward(lenght)
        my_turtle.right(angle)


# for i in range(20):
#     my_turtle.forward(i * 20)
#     square(20, 19)

"rgsfsf"
email = "didahdaniel@yahoo.com"

# prints from start to end
print(email[:])

# value at index 9 not included
print(email[2:9])

print(email[:email.index('@')])
print(email[email.index('@') + 1:])
print(email[email.index('@') + 1:email.index('.')])
print(email.split('@'))
print(email[::-1])
details = [1, 2, 3, 4, 5]
print("details")
print(details)
details.append(2)
print(details)
print(details[::-1])

# se
my_turtle.speed(0)

# # making a circle out of squares
# # making a mountain out of a mole hill
# for i in range(300):
#     square(100, 90)
#     my_turtle.speed(i)
#     my_turtle.right(2)

# dictionaries
# like json/tree data structure/firebase database structure
phone_book = {
    'fundi': ['9876543-345', 'fundi@yahoo.com', 'fundi sacoo'],
    'qazi': ['45-345345-45', 'qazi@yahoo.com', 'fundi sacoo'],
    'fate': '23-4542-445'
}

print("dictionaries")
print('fundi ' + phone_book['fundi'][0])
print('fundi ' + phone_book['fundi'][1])

# conditions
hours_worked = 13009
if hours_worked > 40:
    print("pay over time")
    print('hours worked')
    print(hours_worked)
    print('pay over time ' + str(hours_worked - 40))
else:
    print("no pay")

# boolean operator
# and or not

# file
test_file = open("testFile.txt", "wb")

print(test_file.name)
print("Mode " + test_file.mode)

for i in range(21):
    test_file.write(bytes("Write " + str(i) + " \n", "UTF-8"))

test_file.close()


def sum_list(a_list):
    count = 0
    for number in a_list:
        count = count + number

    return count


print(sum_list([1, 2, 3, 4]))

number_count = 100
while number_count >= 0:
    print(number_count)
    if number_count == 0:
        print('Blast off!!!!!!!!')

    number_count -= 1


def square_it(num):
    return num * num


print(square_it(12))


def check_parity(num):
    if (num % 2) == 0:
        return 'even number'
    else:
        return 'odd number'


print(check_parity(115))
print(check_parity(1156))


def the_lenght(name):
    count = 0
    for _ in name:
        count = count + 1

    return count


print(the_lenght('gfdsg876rertjkfds'))


def last_number(string):
    return string[-1]


print(last_number('adgfds'))
print(last_number('adgfd6'))


def bigger_num(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def bigger_guy(num1, num2, num3):
    return bigger_num(num3, bigger_num(num1, num2))


print(bigger_num(45, 23))
print(bigger_guy(12, 53, 256))
print(bigger_guy(122, 53, 56))
print(bigger_guy(12, 253, 56))

# Tuples
height, weight, width = 5.9, 65, 20

print('The height is {} ,weight is {}, width is {}'.format(height, weight, width))

# sets
# sets contains no duplicates
# has no order and no index
countries = ['India', 'Kenya', 'Uganda', 'Tanzania', 'Kenya', 'Usa', 'Uk', 'USA', 'India']
countries_set = set(countries)
print(countries_set)
print(len(countries_set))
print(len(countries))
countries_set.add('Italy')  # adding to sets
print(countries_set)
countries_set.pop()  # removes random
print(countries_set)

# list comprehension
# making a list from a for loop
# x**2 means x squared
many_number = [x ** 2 for x in range(10)]
print(many_number)


# getting user input
# exception handling
def main():
    validInput = True
    while validInput:
        # get user input
        try:
            number = int(input('Enter a number\n'))
            print(number)
            validInput = False
        except ValueError:
            print('invalid input. Try again\n')
            # return without anything to exit a method
        except:
            print('unknown Exception')


# While loop runs main() until user want to exit from program
doAgain = True
while doAgain:
    asd = True
    while asd:
        # get user input
        try:
            number = int(input('Enter 1. to Continue\n 2.Exit the Program\n'))
            if number == 1:
                main()
            elif number == 2:
                doAgain = False
                print('Program Exiting')
            else:
                print('Invalid Choice. Try again\n')
            asd = False
        except:
            print('invalid input. Try again\n')
