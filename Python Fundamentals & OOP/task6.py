'''
1. Print a 5×5 square of stars.
2. Print a right-angled triangle of stars with 5 rows.
3. Print this number triangle:
```
1
1 2
1 2 3
1 2 3 4
```
4. Print this pattern (repeated numbers):
```
1
2 2
3 3 3
4 4 4 4
```
5. Print an **inverted** star triangle (5 stars on the first row, down to 1).
6. Print a pyramid of stars with 5 rows.
7. Print numbers from 1 to 20 but **stop** when you reach a number divisible by 7 (use `break`).
8. Print numbers from 1 to 20 but **skip** multiples of 3 (use `continue`).
9. Prime checker: ask for a number and print whether it's prime.
10. Print the multiplication tables from 1 to 5 using nested loops. Each row should show one table, like `1 2 3 ... 10`, then `2 4 6 ... 20`.
11. print all prime numbers between 1 and 50.
'''

#1
for i in range(5):
    for j in range(5):
        print("*",end = " ")
    print()

#2
for i in range(1, 6):
    print("* " * i)

#3
for i in range(1, 5):
    for j in range(1, i+1):
        print(j,end = " ")
    print()

#4
for i in range(1, 5):
    for j in range(1, i+1):
        print(i, end = " ")
    print()

#5
index = 0
for i in range(5, 0, -1):
    print(f"{' '*index}{'* ' * i}")
    index += 1

#6
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

#7
for i in range(1,21):
    if i%7 == 0:
        break
    print(i)

#8
for i in range(1,21):
    if i%3 == 0:
        continue
    print(i)

#9
n = int(input("Enter a number: "))

if n < 2:
    print(f"{n} is not prime.")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(f"{n} is prime." if is_prime else f"{n} is not prime.")

#10
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()

#11
for n in range(2, 51):
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)   
