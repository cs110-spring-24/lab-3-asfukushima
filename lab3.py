# write a program that prints out the numbers 1 to 1000.
count = 1
while count < 1001:
    print(count)
    count += 1
# write a program that prints out the odd numbers between 1 and 1000.
count = 1
while count < 1001:
    print(count)
    count += 2
# write a program that prints out the numbers between 0 and 1000 that are divisible by 3.
for count in range(1001):
    if count % 3 == 0:
        print(count)
# write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5.
for count in range(1001):
    if count % 3 == 0:
        print(count)
        # must use elif or lse the same multiples will come up twice. ex. 90
    elif count % 5 == 0:
        print(count)
#  Write a program that asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200.
num = int(input("please enter a number greater than 200: "))
# <==: "is equal to or less than"
if num <= 200:
    print("number should be greater than 200.")
else:
    print("numbers between 1 and", num, "that are divisible by 11 and 13")
    count = 1
    # while loop
    while count <= num:
        if count % 11 == 0 or count % 13 == 0:
            print(count)
        count += 1
# write a program that prints out each letter of a string line by line 
def printletters(string):
    for letter in string:
        print(letter)
input_string = "Hello World!"
print("Printing each letter of 'Hello World!' line by line:")
printletters(input_string)
# write a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long.
def printeverysecondletter(string):
    for i in range(1, len(string), 2):
        print(string[i])
    # ask the user to enter a string
user = input("Enter a string (more than 10 letters long): ")
    # check if the string is more than 10 letters long
if len(user) <= 10:
    print("Error: The string must be more than 10 letters long.")
else:
    print("Every second letter of the input string: ")
    printeverysecondletter(user)
# write a program that rolls 1000 dice and prints out the number of times each number was rolled.
import random
    # define 3 variables
def rolldice():
    return random.randint(1, 6)
def countrolls(numrolls):
    rollscount = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(numrolls):
        rollresult = rolldice()
        rollscount[rollresult] += 1
    return rollscount
def printrollcounts(rollscount):
    for number in range(1, 7):
        print(f"Number {number} was rolled {rollscount[number]} times.")
    # Roll 1000 dice
numrolls = 1000
rollscount = countrolls(numrolls)
    # Print the counts of each number rolled
print("Roll counts:")
printrollcounts(rollscount)
# write a program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not.
def prime(number):
    if number <= 1:
        return False  # 1 and numbers less than 1 are not prime
    for i in range(2, number):
        if number % i == 0:
            return False  # if the number is divisible by any number other than 1 and itself, it's not prime
    return True  # if none of the above conditions are met, the number is prime
    # get input from the user
user = int(input("Enter a number to check if it's prime: "))
    # Check if the number is prime and print the result
if prime(user):
    print(f"{user} is a prime number.")
else:
    print(f"{user} is not a prime number.")
# write a program that prints out the prime numbers less than 1000. 
    # function to check if a number is prime
def prime(number):
    if number <= 1:
        return False  # numbers less than or equal to 1 are not prime
    for i in range(2, number):
        if number % i == 0:
            return False  # if the number is divisible by any number other than 1 and itself, it's not prime
    return True  # if none of the above conditions are met, the number is prime
    # iterate through numbers less than 1000 and print the prime ones
print("Prime numbers less than 1000:")
for num in range(2, 1000):
    if prime(num):
        print(num, end=" ")  # Print the prime number
#idek anymore im sorry if ts doesn't work 
