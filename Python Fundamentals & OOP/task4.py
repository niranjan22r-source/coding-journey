'''
1.Ask for a number and print whether it is positive, negative or zero.
2.Ask for a number and print whether it is even or odd.
3.Ask for the user’s age and print whether they can vote.
4.Grade calculator: ask for marks (0 to 100) and print grade A (90+), B (75–89), C (50–74) or Fail.
5.Ask for three numbers and print the largest.
6.Leap year checker: test with 2024, 1900, 2000 and 2023.
7.Ask for a number and print whether it’s divisible by both 3 and 5, only one of them, or neither.
8.Login system: the correct username is admin and the password is python123. Print “Login successful” only if both match.
9.Update your Day 3 calculator so that it doesn’t crash when dividing by zero.
10.electricity bill. Ask for units used. The first 100 units cost ₹2 each, the next 100 cost ₹3 each, and anything above 200 costs ₹5 each. Print the total bill. For example, 250 units = 100×2 + 100×3 + 50×5 = ₹750
'''

#1
num = int(input("Enter a number: "))
if num>0:
    print("Number is Positive")
elif num<0:
    print("Number is Negative")
else:
    print("Number is Zero")

#2
num = int(input("Enter a number: "))
if num%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#3
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You are Eligible to Vote")
else:
    print("You are Not Eligible to Vote")

#4
mark = int(input("Enter your Mark: "))
if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Fail")

#5
num1 = int(input("Enter no1: "))
num2 = int(input("Enter no2: "))
num3 = int(input("Enter no3: "))
if num1 >= num2 and num1 >= num3:
    print(f"Largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"Largest number is {num2}")
else:
    print(f"Largest number is {num3}")

#6
if (2024 % 4 == 0 and 2024 % 100 != 0) or (2024 % 400 == 0):
    print("2024 is Leap year")
else:
    print("2024 is Not a leap year")
if (1900 % 4 == 0 and 1900 % 100 != 0) or (1900 % 400 == 0):
    print("1900 is Leap year")
else:
    print("1900 is Not a leap year")
if (2000 % 4 == 0 and 2000 % 100 != 0) or (2000 % 400 == 0):
    print("2000 is Leap year")
else:
    print("2000 is Not a leap year")
if (2023 % 4 == 0 and 2023 % 100 != 0) or (2023 % 400 == 0):
    print("2023 is Leap year")
else:
    print("2023 is Not a leap year")

#7
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0 or num % 5 == 0:
    print("Divisible by only one of 3 and 5")
else:
    print("Divisible by neither 3 nor 5")

#8
username = input("Enter username: ")
password = input("Enter Password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("username or password is wrong!")

#9
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 == 0:
    print("Cannot Divide by Zero")
else:
    print("Division:", num1 / num2)
    print("Remainder:", num1 % num2)

#10
units = int(input("Enter electricity units used: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

print("Total electricity bill: ₹", bill)
