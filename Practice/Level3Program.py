"""
# Problem 1
Task:
Print all numbers less than n that satisfy both conditions:
- The number is divisible by 3
- The sum of its digits is even

Input:
50

Output:
6 15 24 33 39 42 48

"""
# n = int(input())
# for i in range(1,n):
#     s = 0
#     temp = i
#     while temp != 0:
#         remainder = temp % 10
#         s = s + remainder
#         temp = temp // 10
#     if s % 2 == 0 and i % 3 == 0:
#         print(i)

"""
Problem 2
You are given a number n.
Task:
Print all numbers less than n that satisfy:
- The number is a palindrome
- The sum of its digits is greater than 10

Input:
200

Output:
55 66 77 88 99 181 191

"""
# n = int(input())
# for i in range(1,n):
#     s = 0
#     temp = i
#     num = 0
#     while temp != 0:
#         remainder = temp % 10
#         num = num * 10 + remainder
#         temp = temp // 10
#         s = s + remainder
#     if s > 10 and num == i:
#         print(i,end=" ")

"""
# Problem 3

You are given a number n.
Task:
Print all numbers less than n that satisfy:
The number is divisible by both 4 and 6
The product of its digits is even

Input:
100

Output:
12, 24, 36, 48, 60, 72, 84, 96

"""
# n = int(input())
# for i in range(1,n):
#     product = 1
#     temp = i
#     while temp != 0:
#         remainder = temp % 10
#         product *= remainder
#         temp = temp // 10

#     if product % 2 == 0 and (i % 4 == 0 and i % 6 == 0):
#         print(i, end=" ")

"""
# Problem 4

You are given a string containing space-separated numbers.
Task:
Create a list of integers from the string and print only the even numbers.

Input:
10 15 20 33 40 55 60

Ouput:
10 20 40 60
"""

# ls = list(map(str,input().split()))
# for i in ls:
#     if int(i) % 2 == 0:
#         print(i,end = " ")

"""
# Problem 5

You are given a string of space-separated numbers.
Task:
Create a list of integers and print the square of each number.

Input:
2 3 4 5

Output:
4 9 16 25
"""
# ls = input().split()
# for i in ls:
#     print(int(i)*int(i),end= " ")

"""
# Problem 6
You are given a string of words (space-separated).
Task:
- Create a dictionary where:
key = word
value = length of the word
Then print the dictionary.

Input:
apple bat cat elephant

Output:
{'apple': 5, 'bat': 3, 'cat': 3, 'elephant': 8}

"""
# string = input()
# d = {}
# for i in string.split():
#     d[i] = len(i)
# print(d)

"""
# Problem 7
You are given a string of words (space-separated).
Task:
- Create a dictionary that stores the frequency of each word.

Input:
apple bat apple cat bat apple

Output:
{'apple': 3, 'bat': 2, 'cat': 1}

"""
# string = input()
# d = {}
# for i in string.split():
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

"""
# Problem 8
You are given a string of space-separated numbers.
Task:
- Print the unique numbers (remove duplicates), preserving no specific order.

Input:
1 2 3 2 4 1 5 3

Output:
1 2 3 4 5

"""
# n = input().split()
# s = sorted(set(n))
# print(" ".join(s))

"""
# Problem 9
You are given a string of words.
Task:
Print only the words that appear more than once.

Input:
apple bat apple cat bat apple

Output:
apple bat

"""

# string = input()
# d = {}
# for i in string.split():
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# for k, v in d.items():
#     if v > 1:
#         print(k,end=" ")

"""
# Problem 10
You are given a string of space-separated numbers.
Task:
Create a list of numbers greater than 10 and print them.

Input:
5 12 7 18 3 25 10 11

Output:
12 18 25 11

"""
# n = input()
# for i in n.split():
#     if int(i) > 10:
#         print(i, end =" ")

"""
# Problem 11
You are given a string of space-separated integers.
Task
Create a list of even numbers greater than 10, then print them in the same order.

Input:
3 12 5 20 8 11 14 7 22 10

Output:
12 20 14 22

"""

# n = input()
# for i in n.split():
#     if int(i) > 10 and int(i) % 2 == 0:
#         print(i, end =" ")

"""
# Problem 12
You are given a string of space-separated integers.
Task
Print numbers whose digit sum is greater than 10.
Input:
59 12 99 101 8 44

Output:
59 99

"""
# n = input().split()
# for i in n:
#     digit_sum = 0
#     temp = int(i)
#     while temp !=0 :
#         remainder = temp % 10
#         digit_sum += remainder
#         temp = temp // 10

#     if digit_sum> 10:
#         print(i, end=" ")

"""
# Problem 13
Print numbers which are palindrome.

Input:
121 34 7 99 10 404 23

Output:
121 7 99 404

"""
# n = input().split()
# for i in n:
#     rev = 0
#     temp = int(i)
#     while temp != 0:
#         remainder = temp % 10
#         rev = rev*10 + remainder
#         temp = temp //10

#     if int(i) == rev:
#         print(i, end=" ")

"""
# Problem 14
Task
Print numbers whose first digit is equal to last digit.

Input:
123 454 78 9 101 20 44

Output:
454 9 101 44

"""
# n = input().split()
# for i in n:
#     temp = int(i)
#     last = temp % 10
#     first = temp
#     while first >= 10:
#         first = first // 10
#     if first == last:
#         print(i, end=" ")

"""
# Problem 15

You are given a string of space-separated integers.
Task
Print numbers whose sum of first and last digit is even.

Input:
123 456 89 7 40 91 222

Output:
123 456 7 40 91 222

"""
# n = input().split()
# for i in n:
#     temp = int(i)
#     last = temp % 10
#     first = temp
#     while first >= 10:
#         first = first // 10
#     if (first + last) % 2 == 0:
#         print(i, end=" ")


"""
# Problem 16
Task
Print numbers whose product of digits is greater than 20.

Input:
123 59 222 39 7 84

Output:
59 39 84

"""

# n = input().split()
# for i in n:
#     product = 1
#     temp = int(i)
#     while temp != 0:
#         remainder = temp % 10
#         product = product * remainder
#         temp = temp // 10

#     if product > 20:
#         print(i, end=" ")

"""
# Problem 17

Print numbers which contain at least one even digit.

Input:
135 246 579 82 7 111

Output:
246 82

"""
# n = input().split()
# for i in n:
#     temp = int(i)
#     count = 0
#     while temp != 0:
#         remainder = temp % 10
#         temp = temp // 10
#         if remainder % 2 == 0:
#             count = 1
#             break
#     if count == 1:
#         print(i, end=" ")


"""
# Problem 18
Task
Print numbers whose digits are in strictly increasing order (left to right).
Input:
123 135 124 7 89 321

Output:
123 135 124 7 89

"""
# n = input().split()
# for i in n:
#     temp = int(i)
#     ls = []
#     while temp != 0:
#         remainder = temp % 10
#         temp = temp // 10
#         ls.append(remainder)

#     valid = 1
#     for j in range(len(ls)-2,-1,-1):
#         if ls[j] <= ls[j+1]:
#             valid = 0
#             break
#     if valid == 1:
#         print(i,end=" ")

"""
# Problem 19
You are given a string of space-separated numbers.
Task:
Print only the odd numbers.

Input:
10 15 22 33 40 55 60 71

Output:
15 33 55 71

"""
# n = input().split()
# for i in n:
#     temp = int(i)
#     if temp % 2 != 0:
#         print(i, end=" ")

"""
# Problem 20

You are given a string of space-separated numbers.
Task:
Convert them into integers and print each number increased by 1.

Input:
1 4 7 10

Output:
2 5 8 11

"""
# n = input().split()
# for i in n:
#     temp = int(i)
#     temp += 1
#     print(temp, end=" ")

"""
# problem 21
You are given a string.
Task:
Count and print the number of vowels (a, e, i, o, u) in the string.

Input:
programming

Output:
3

"""

# n = input()
# count = 0
# for i in n:
#     l = i.lower()
#     if l in "aeiou":
#         count += 1
# print(count,end=" ")

"""
# Problem 22

You are given a string.
Task:
Print only the consonants from the string (ignore spaces).
Input:
hello world

Output:
hllwrld

"""
# n = input().split()
# string = ""
# for i in n:
#     i = i.lower()
#     for j in i:
#         if j not in "aeiou":
#             string += j

# print(string)

#.OR

# n = input()
# string = ""
# for i in n:
#     if i.lower() not in "aeiou" and i.isalpha():
#         string += i

# print(string)

"""
# Problem 23
You are given a string.
Task:
Print all unique characters (remove duplicates).

Input:
programming

Output:
p r o g a m i n

"""
# when we don't want order
# n = input()
# unique = set(n.lower())
# print("".join(unique))

# if order persits
# n = input()
# unique = []
# for i in n.lower():
#     if i not in unique:
#         unique.append(i)
# print("".join(unique))

"""
# Problem 24
You are given a string.
Task:
Count the frequency of each character (ignore spaces).

Input:
hello world

Output:
{'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}

"""

# n = input()
# d = {}

# for ch in n.lower():
#     if ch.isalpha():
#         if ch not in d:
#             d[ch] = 1
#         else:
#             d[ch] += 1
# print(d)

"""
# Problem 25
You are given a sentence.
Task:
Print only the words whose length is greater than 4.

Input:
python code is very powerful and simple

Output:
python powerful simple

"""
# n = input()
# for i in n.split():
#     if len(i) > 4:
#         print(i, end=" ")

"""
# Problem 26
You are given space-separated numbers.
Task:
Store them in a tuple of integers
Print the sum of all numbers

Input:
3 5 7 2

Output:
17

"""
# n = tuple(input().split())
# s = 0
# for i in n:
#     i = int(i)
#     s += i
# print(s)

# OR
# from functools import reduce
# n = tuple(input().split())
# s = reduce(lambda x, y : int(x)+int(y), n)
# print(s)

"""
# Problem 27
You are given space-separated numbers.
Task:
Store them in a tuple of integers
Print only numbers divisible by 5

input:
10 12 15 18 25 7

Output:
10 15 25

"""
# n = tuple(map(int,input().split()))
# filtered = list(filter(lambda x: x% 5 == 0, n))
# print(filtered)

# n = tuple(map(int,input().split()))
# for i in n:
#     if i % 5 ==0:
#         print(i,end=" ")

"""
# Problem 28
You are given space-separated numbers.
Task:
Print only the numbers that appear exactly once (remove duplicates completely).

Input:

index- 0 1 2 3 4 5 6 7 8
items- 1 2 2 3 4 4 5 6 6 7 9 4 3

Output:
1 3 5

"""
# n = list(map(int, input().split()))
# d = {}

# for x in n:
#     if x not in d:
#         d[x] = 1
#     else:
#         d[x] += 1

# for x in d:
#     if d[x] == 1:
#         print(x, end=" ")

"""
PROBLEM 29 (LIST + DICT, similar but twist)
TASK
Print numbers that appear more than once (duplicates only).

Input:
1 2 2 3 4 4 5 6 6

Output:
2 4 6

"""

# n = map(int,input().split())
# d = {}
# for i in n:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# for k,v in d.items():
#     if v>1:
#         print(k, end=" ")



























