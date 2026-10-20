'''Create a file called task1.py and do these in order:

1.Print Hello, World!
2.Print your full name, your city and your goal for learning Python, on 3 separate lines.
3.Print the result of 25 * 4 and 100 / 5.
4.Ask the user for their name and age, then print: Hello <name>, you are <age> years old.
5.Ask for the user’s favourite food and print <food> is delicious!.'''

#1
print("Hello World!")

#2
print("Niranjan R")
print("Thanjavur")
print("Improve my skills")

#3
print(25*4)
print(100/5)

#4
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
print(f"Hello {name}, you are {age} Years Old")

#5
food = input("Enter Your Favourite Food: ")
print(f"{food} is delicious!")
