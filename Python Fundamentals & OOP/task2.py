'''
1.Create variables for your name, age, height and whether you’re a student. Print each one and its type.
2.Ask for two numbers, add them, and print the sum. (Remember: convert with int().)
3.Ask for a number and print it multiplied by 10.
4.Ask for your name and birth year. Print your age (use 2026 as the current year).
5.Ask for the price and quantity of an item. Print the total price.
6.Ask for the length and width of a rectangle. Print the area and the perimeter.
7.Make two variables a = 10 and b = 20, and swap their values. Print them before and after.
8.Predict the output before running: print(10 / 2), print(type(10 / 2)), print(int(9.99)), print("2" + "3").
9.Ask for a temperature in Celsius and convert it to Fahrenheit using F = C * 9 / 5 + 32.
10.Ask for a student’s marks in 3 subjects and print the total and the average.
'''

#1
name = "Niranjan R"
age = 19
height = 164.5
student = True
print(name,type(name))
print(age,type(age))
print(height,type(height))
print(student,type(student))

#2
number1 = int(input("Enter no1: "))
number2 = int(input("Enter no2: "))
total = number1 + number2
print(total)

#3
number = int(input("Enter a number: "))
print(number*10)

#4
name = input("Enter Your Name: ")
birth_year = int(input("Birth Year: "))
present_age = 2026 - birth_year
print(f"{name}! your age is {present_age}")

#5
price = float(input("price: "))
quantity = float(input("quantity: "))
total_price = price * quantity
print(f"total price = {total_price}")

#6
length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area of the rectangle = {area}\nPerimeter of the rectangle = {perimeter}")

#7
a = 10
b = 20
print(f"Before Swapping: a = {a} b = {b}")
a , b = b , a
print(f"After Swapping: a = {a} b = {b}")

#8
print(10/2) #ans: 5.0
print(type(10 / 2)) #ans: <class: float>
print(int(9.99)) #ans: 9
print("2" + "3") #ans: 23

#9
temp = float(input("Enter the Temperature: "))
Fahrenheit = temp * 9 / 5 + 32
print(f"Fahrenheit = {Fahrenheit}")

#10
subject1 = int(input("Subject1 mark: "))
subject2 = int(input("Subject2 mark: "))
subject3 = int(input("Subject3 mark: "))
total = subject1 + subject2 + subject3
average = total / 3
print(f"Total: {total}\nAverage: {round(average, 2)}")
