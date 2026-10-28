'''
1.Create a dictionary with your name, age, city and course. Print each value using its key.
2.Add a new key email, change the age, and delete the city. Print the dictionary after each step.
3.Ask for a key and print its value from your dictionary. If the key doesn’t exist, print “Key not found”. Do it with get() and also with in.
4.Create a dictionary of 5 subjects and marks. Print the total, the average, the highest-scoring subject and the lowest-scoring subject.
5.Print each subject and its marks as maths: 90, using items().
6.Count how many times each character appears in a word typed by the user.
7.Word-frequency counter: ask for a sentence and print the frequency of each word, ignoring case. Then print the most common word.
8.Create a dictionary of squares: for 1 to 5, the keys are the numbers and the values are their squares. {1: 1, 2: 4, ...}.
9.Build a simple phone book: keep asking the user to add a contact, search a contact or quit, using a while loop and a dictionary.
10.Given names = ["Ravi", "Anu", "Kiran"] and marks = [85, 92, 78], build a dictionary with zip() and print the name of the topper.
11.Given a list of words, group them by their first letter. ["apple", "bat", "ant", "ball"] gives {'a': ['apple', 'ant'], 'b': ['bat', 'ball']}.
12.given a list of numbers and a target, find two numbers that add up to the target using a dictionary. For example, [2, 7, 11, 15] with target 9 gives 2 and 7. (Hint: for each number, check if target - number has been seen. This is the famous Two Sum problem.)
'''

#1
person = {
    "name": "Ravi",
    "age": 19,
    "city": "Chennai",
    "course": "Python"
}

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Course:", person["course"])

#2
person = {
    "name": "Ravi",
    "age": 19,
    "city": "Chennai",
    "course": "Python"
}

person["email"] = "ravi@example.com"
print("After adding email:", person)
person["age"] = 20
print("After changing age:", person)

del person["city"]
print("After deleting city:", person)

#3
person = {
    "name": "Ravi",
    "age": 19,
    "city": "Chennai"
}

key = input("Enter a key to search: ")

#1..Using get()
value = person.get(key)

if value is not None:
    print("Value:", value)
else:
    print("Key not found")

#2.. Using in
if key in person:
    print("Value:", person[key])
else:
    print("Key not found")

#4
marks = {
    "Maths": 90,
    "Science": 85,
    "English": 78,
    "Computer": 95,
    "History": 80
}
total = 0
highest_subject = None
lowest_subject = None

for subject, mark in marks.items():
    total += mark
    if highest_subject is None or mark > marks[highest_subject]:
        highest_subject = subject

    if lowest_subject is None or mark < marks[lowest_subject]:
        lowest_subject = subject

average = total / len(marks)
print("Total:", total)
print("Average:", average)
print("Highest-scoring subject:", highest_subject, marks[highest_subject])
print("Lowest-scoring subject:", lowest_subject, marks[lowest_subject])

#5
marks = {
    "Maths": 90,
    "Science": 85,
    "English": 78,
    "Computer": 95,
    "History": 80
}

for subject, mark in marks.items():
    print(f"{subject}: {mark}")

#6
word = input("Enter a word: ").lower()
frequency = {}

for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)

#7
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequencies:")

for word, count in frequency.items():
    print(f"{word}: {count}")

if frequency:
    most_common = max(frequency, key=frequency.get)
    print("Most common word:", most_common)
    print("Count:", frequency[most_common])
else:
    print("No words entered.")

#8
squares = {num: num ** 2 for num in range(1, 6)}

print(squares)

#9
phone_book = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()

        phone_book[name.lower()] = phone
        print("Contact saved!")

    elif choice == "2":
        name = input("Enter name to search: ").strip().lower()

        if name in phone_book:
            print("Phone number:", phone_book[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        print("Exiting phone book.")
        break

    else:
        print("Invalid choice. Try again.")

#10
names = ["Ravi", "Anu", "Kiran"]
marks = [85, 92, 78]
student_marks = dict(zip(names, marks))

print("Student marks:", student_marks)

topper = max(student_marks, key=student_marks.get)

print("Topper:", topper)
print("Marks:", student_marks[topper])

#11
words = ["apple", "bat", "ant", "ball"]
groups = {}

for word in words:
    first_letter = word[0]

    if first_letter not in groups:
        groups[first_letter] = []

    groups[first_letter].append(word)

print(groups)

#12
numbers = [2, 7, 11, 15]
target = 9
seen = {}

for num in numbers:
    needed = target - num

    if needed in seen:
        print("Numbers:", needed, "and", num)
        print("Sum:", needed + num)
        break
    seen[num] = True
else:
    print("No pair found.")
