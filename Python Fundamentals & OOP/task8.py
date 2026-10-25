'''
1.Ask for a word and print its first character, last character and length.
2.Print a word reversed, using slicing.
3.Palindrome checker: test with madam, level, python and Racecar. (Hint: handle upper and lower case.)
4.Vowel counter: ask for a sentence and print the number of vowels and consonants. (Count only letters. Hint: isalpha().)
5.Ask for a full name (for example niranjan r) and print it in title case, in //uppercase, and the number of characters without spaces.
6.Ask for a sentence and print the number of words.
7.Ask for a sentence and replace every space with a hyphen.
8.Ask for a string and print every second character.
9.Ask for a string and print how many times a letter that the user chooses appears in it.
10.Ask for a word and print the word with its first and last characters swapped.
11.ask for a sentence and print it with each word reversed, but with the word order the same. For example, hello world becomes olleh dlrow. (Hint: split(), slicing, join().)
12.check whether two words are anagrams (same letters in a different order, like listen and silent). (Hint: sorted().)
'''

#1
word = input("Enter a word: ")
if word == "":
    print("invalid input")
else:
    print(f"first character:{word[0]} , last character:{word[-1]} , word's length:{len(word)}")

#2
    print(f"reversed string:{word[::-1]}")

#3
for w in ["madam", "level", "python", "Racecar"]:
    w = w.lower()
    print(w, "->", "Palindrome" if w == w[::-1] else "Not a palindrome")

#4
text = input("Enter a sentence: ").lower()
vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

#5
name = input("Enter your full name: ")
print(name.title())
print(name.upper())
print(len(name.replace(" ", "")))

#6
sentence = input("Enter a sentence(counts number of words): ")
print(f"number of words in {sentence} is {len(sentence.split())}")

#7
sentence1 = input("Enter a sentence(for replace every space with a hyphen): ")
print(sentence1.replace(" ","-"))

#8
string = input("Enter a word(print every second character): ")
print(string[1::2])

#9
text1 = input("Enter a string: ").lower()
letter = input("Enter a letter to count: ").lower()
count = 0

for ch in text1:
    if ch == letter:
        count += 1
print(f"The letter appears {count} times")

#10
word2 = input("Enter a word(first and last characters swap): ")
if len(word2) < 2:
    print(word2)
else:
    print(word2[-1] + word2[1:-1] + word2[0])
#11
words = input("Enter a sentence: ").split()
for i in range(len(words)):
    words[i] = words[i][::-1]
print(" ".join(words))

#12
word3_1 = "".join(input("Enter word1: ").lower().split())
word3_2 = "".join(input("Enter word2: ").lower().split())

if sorted(word3_1) == sorted(word3_2):
    print("It is Anagrams")
else:
    print("It is not Anagrams")
