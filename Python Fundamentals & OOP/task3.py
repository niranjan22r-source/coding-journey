'''
1.Predict the output before running: print(15 // 4), print(15 % 4), print(2 ** 5), print(10 + 2 * 5), print((10 + 2) * 5).
2.Build the calculator above, and give it your own formatting using f-strings.
3.Ask for a number and print whether it’s even or odd, as True or False. For example: print("Even:", n % 2 == 0).
4.Ask for a 4-digit number and print its last digit. (Hint: %.) Then print the number without its last digit. (Hint: //.)
5.Ask for the total minutes (for example 135) and print it as hours and minutes (2 hours 15 minutes).
6.Ask for a number and print its square and cube.
7.Ask for an amount in rupees and print the number of ₹500, ₹100 and ₹10 notes needed (use // and %). Example: 1260 gives 2 notes of ₹500, 2 of ₹100 and 6 of ₹10.
8.Ask for two numbers and print True or False for each of: a > b, a == b, a != b.
9.Ask for an age and print whether the person can vote (age >= 18) and whether they’re a teenager (13 <= age <= 19).
10.ask for the principal, rate and time, and print the simple interest using (P * R * T) / 100.
'''

#1
print(15 // 4) #3
print(15 % 4) #3
print(2 ** 5) #32
print(10 + 2 * 5) #20
print((10 + 2) * 5) #60

#2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Floor division: {num1 // num2}")
print(f"Remainder: {num1 % num2}")
print(f"Power: {num1 ** num2}")

#3
number = int(input("Enter a number: "))
print(f"odd: {number % 2 == 1}\neven: {number % 2 == 0}")

#4
num = int(input("Enter a Four Digit Number: "))
print("Last digit:", num % 10)
print("Without last digit:", num // 10)

#5
total_minutes = int(input("Enter a total minutes: "))
hour , minutes = total_minutes//60 , total_minutes % 60
print(f"{hour} hours {minutes} minutes")

#6
number = int(input("Enter a Number: "))
print(f"square of {number} = {number ** 2}\ncube of {number} = {number ** 3}")

#7
rupees = int(input("Enter the Amount: "))
amt500, bal = rupees // 500, rupees % 500
amt100, bal = bal // 100, bal % 100
amt50, bal = bal // 50, bal % 50
amt10 = bal // 10
print(f"{rupees} gives {amt500} notes of ₹500, {amt100} notes of ₹100, {amt50} notes of ₹50, {amt10} notes of ₹10")

#8
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 != num2)

#9
age = int(input("Enter your age: "))
print(f"person can vote: {age >= 18}\nteenager: {13 <= age <= 19}")

#10
principal = float(input("Principal: "))
rate = float(input("Rate: "))
time = float(input("Time: "))
print(f"Simple interest: {(principal * rate * time) / 100}")
