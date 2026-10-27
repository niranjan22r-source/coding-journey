'''
1.Create a tuple of 5 numbers. Print the first item, the last item and the length.
2.Create a tuple with your name, age and city. Unpack it into 3 variables and print each.
3.Try changing an item in a tuple, and print the error message you get (don’t fix it, just observe it).
4.Ask for 5 numbers, store them in a tuple, and print the sum and the largest.
5.Remove duplicates from [5, 3, 5, 2, 3, 1] using a set and print the result.
6.Ask for a sentence and print the number of unique characters (ignore spaces).
7.Given a = {1, 2, 3, 4, 5} and b = {4, 5, 6, 7}, print the union, intersection, difference (a - b) and symmetric difference.
8.Given two lists of students (one for maths, one for science), print the students who take both, the students who take only maths, and the students who take at least one.
9.Find the duplicate numbers in [1, 4, 2, 4, 5, 2, 6].
10.Check whether a word has all unique letters. Test with python, hello and world.
11.Ask for two sentences and print the words that appear in both (ignore capital letters).
12.check whether two strings are anagrams using sorted() (like Day 8), and then check “do they use the same set of letters?” using sets. Explain the difference using aab and abb.
'''

#1
numbers = (10, 20, 30, 40, 50)

print("First item:", numbers[0])
print("Last item:", numbers[-1])
print("Length:", len(numbers))

#2
person = ("Ravi", 19, "Chennai")
name, age, city = person

print("Name:", name)
print("Age:", age)
print("City:", city)

#3
numbers = (10, 20, 30)
try:
    numbers[0] = 100
except Exception as e:
    print("Error:", e)

#4
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
numbers = tuple(numbers)

print("Tuple:", numbers)
print("Sum:", sum(numbers))
print("Largest:", max(numbers))

#5
numbers = [5, 3, 5, 2, 3, 1]
unique = set(numbers)

print("Without duplicates:", unique)

#6
sentence = input("Enter a sentence: ")
unique_chars = set(sentence.lower().replace(" ", ""))

print("Unique characters:", unique_chars)
print("Number of unique characters:", len(unique_chars))

#7
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric difference:", a ^ b)

#8
maths = {"Ravi", "Priya", "Amit", "Sneha"}
science = {"Priya", "Amit", "Rahul", "Kiran"}

print("Both subjects:", maths & science)
print("Only Maths:", maths - science)
print("At least one subject:", maths | science)

#9
numbers = [1, 4, 2, 4, 5, 2, 6]
seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", duplicates)

#10
words = ["python", "hello", "world"]

for word in words:
    letters = set(word)
    if len(letters) == len(word):
        print(word, "has all unique letters")
    else:
        print(word, "has repeated letters")

#11
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")
words1 = set(sentence1.lower().split())
words2 = set(sentence2.lower().split())

common_words = words1 & words2

print("Common words:", common_words)

#12
word1 = input("Enter the first word: ").lower().replace(" ", "")
word2 = input("Enter the second word: ").lower().replace(" ", "")

if sorted(word1) == sorted(word2):
    print("They are anagrams.")
else:
    print("They are not anagrams.")

if set(word1) == set(word2):
    print("They use the same set of letters.")
else:
    print("They do not use the same set of letters.")
