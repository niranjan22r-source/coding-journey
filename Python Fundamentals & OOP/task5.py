'''
1.Print numbers from 1 to 10 using for.
2.Print numbers from 10 down to 1.
3.Print all even numbers from 1 to 50.
4.Print the sum of numbers from 1 to 100.
5.Multiplication table: ask for a number and print its table up to 10.
6.Ask for a number n and print the sum of the first n natural numbers.
7.Factorial: ask for a number and print its factorial.
8.Sum of digits: ask for a number and print the sum of its digits.
9.Count the digits in a number (hint: use while and // 10).
10.Print the 4 leap-year results from Day 4 using one loop: for year in [2024, 1900, 2000, 2023]:.
11.reverse a number using while. For 1234, print 4321. (Hint: rev = rev * 10 + digit)
'''

#1
for i in range(1,11):
    print(i)

#2
for i in range(10,0,-1):
    print(i)

#3
for i in range(2,51,2):
    print(i)

#4
num = 0
for i in range(1,101):
    num += i
print(f"sum 0f 100 = {num}")

#5
num = int(input("Enter a Number for Table: "))
for i in range(1, 11):
    print(f"{i} x {num} = {i * num}")

#6
n = int(input("Enter a Number for Sum: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of {n} = {total}")

#7
num = int(input("Enter a Number for Factorial: "))
fact = 1
for i in range(num, 0,-1):
    fact *= i

print(f"Factorial of {num} = {fact}")

#8
num = int(input("Enter a Number for Sum of Digits: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of Digits:", total)

#9
num = int(input("Enter a Number for Count the Digits in a Number:"))
number = num
digit = 0
while num > 0:
    digit += 1
    num //= 10

print(f"{number} is a {digit} digit number")

#10

for year in [2024, 1900, 2000, 2023]:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is Leap year")
    else:
        print(f"{year} is Not a leap year")

#11

num = int(input("Enter a number for reverse: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
