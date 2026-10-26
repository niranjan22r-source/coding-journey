'''
1.Create a list of 5 numbers. Print the first item, the last item, and the first three items.
2.Ask the user for 5 numbers (using a loop and append) and print the list.
3.Print the sum, average, largest and smallest of that list, without using sum(), max() or min() (use loops).
4.Print the list reversed, and also sorted in descending order.
5.Ask for a number and print whether it’s in the list, and how many times it appears.
6.Separate the list into even and odd numbers.
7.Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 1] and keep the order.
8.Find the second largest number in a list. Make it work with duplicates, for example [10, 20, 20, 5] gives 10.
9.Ask for a sentence, split it into words, and print the longest word.
10.Create a list of 5 names and print each with its number, like 1. Ravi. (Hint: enumerate(names, start=1).)
11.Rotate a list by one position: [1, 2, 3, 4, 5] becomes [5, 1, 2, 3, 4]. (Hint: slicing.)
12.merge two sorted lists into one sorted list without using sort(). For example, [1, 3, 5] and [2, 4, 6] give [1, 2, 3, 4, 5, 6]. (Hint: compare the front items.)
'''

#1
numbers = [10, 20, 30, 40, 50]

print("First item:", numbers[0])
print("Last item:", numbers[-1])
print("First three items:", numbers[:3])

#2
numbers = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("Your list:", numbers)

#3
numbers = [10, 25, 5, 40, 20]
total = 0
largest = numbers[0]
smallest = numbers[0]

if len(numbers) == 0:
    print("List is Empty")
else:
    for num in numbers:
        total += num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    average = total / len(numbers)
    print("Sum:", total)
    print("Average:", average)
    print("Largest:", largest)
    print("Smallest:", smallest)

#4
numbers = [10, 40, 20, 50, 30]

print("Reversed:", numbers[::-1])
print("Descending order:", sorted(numbers, reverse=True))

#5
numbers = [10, 20, 30, 20, 40, 20]
target = int(input(f"Enter a number to search from list {numbers}: "))
count = 0

for num in numbers:
    if num == target:
        count += 1

if count > 0:
    print("Number found!")
    print("Occurrences:", count)
else:
    print("Number not found.")

#6
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

#7
numbers = [1, 2, 2, 3, 4, 4, 5, 1]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Without duplicates:", unique)

#8
numbers = [10, 20, 20, 5]

largest = None
second_largest = None

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num

    elif num != largest and (
        second_largest is None or num > second_largest
    ):
        second_largest = num

if second_largest is not None:
    print("Second largest:", second_largest)
else:
    print("No second-largest distinct number exists.")

#9
sentence = input("Enter a sentence: ").strip(".,!?")

words = sentence.split()

if len(words) > 0:
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("No words entered.")

#10
names = ["Ravi", "Amit", "Priya", "Rahul", "Sneha"]

for number, name in enumerate(names, start=1):
    print(f"{number}. {name}")

#11
numbers = [1, 2, 3, 4, 5]
rotated = numbers[-1:] + numbers[:-1]

print("Original:", numbers)
print("Rotated:", rotated)

#12
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged = []

i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1
while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged list:", merged)
