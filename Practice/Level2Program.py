"""
Level 1 program for Practice

"""

# Program 1
# n = int(input())
# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(i)

# Program 2
# n = int(input())
# total_even_number = 0
# for i in range(2,n+1,2):
#     total_even_number += 1
# print(total_even_number)

# Program 3
# from functools import reduce
# n = int(input())
# ls = list(range(2,n+1,2))
# total = reduce(lambda x, y : x+y,ls)
# print(total)
# # OR we can do like this simply
# total = 0
# n = int(input())
# for i in range(2,n+1,2):
#     total += i
# print(total)

# Program 4
# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

# Program 5
# n = int(input())
# reversed = 0
# while n > 0:
#     remainder = n % 10
#     reversed = reversed*10+ remainder
#     n = n//10
# print(reversed)

# Program 6
# n = input()
# sum_of_digit = 0
# for i in n:
#     sum_of_digit += int(i)
# print(sum_of_digit)


# Program 7
# n = int(input())
# original = n
# reversed = 0
# while n>0:
#     remainder = n % 10
#     reversed = reversed*10 + remainder
#     n = n//10
# if reversed == original:
#     print("Palindrom")
# else:
#     print("not Palindrom")


# Program 8
# n = int(input())
# largest = 0
# while n>0:
#     remainder = n % 10
#     if remainder > largest:
#         largest = remainder
#     n = n//10
# print(largest)

# Program 10
# n = int(input())
# if n % 3 == 0 and n % 5 == 0 :
#     print(f"{n} is divisible by 3 and 5")
# else:
#     print(f"{n} is not divisible by 3 and 5")

# Program 11
# n = int(input())
# while n>0:
#     remainder = n % 10
#     n = n//10
# print(remainder)

# Program 12
# n = int(input())
# if n < 0:
#     print("No")
# else:
#     root = int(n ** 0.5)
#     if root * root == n:
#         print("Yes")
#     else:
#         print("No")

# Program 13
# n = int(input())
# product = 1
# while n >0:
#     remainder = n % 10
#     product *= remainder
#     n = n//10
# print(product)

# Program 14
# n = int(input())
# if n <= 0:
#     print("No")
# else:
#     while n > 1:
#         if n % 2 != 0:
#             print("No")
#             break
#         n = n // 2
#     else:
#         print("Yes")

# Program 15
# n = int(input())
# total = 0
# for i in range(3,n,3):
#     total += i
# print(total)

# Program 16
# n = int(input())
# minimum = int(str(n)[0])
# while n>0:
#     remainder = n % 10
#     if remainder < minimum:
#         minimum = remainder
#     n = n//10
# print(minimum)

# Program 17. #38572
# n = int(input())
# n = str(n)
# length = len(n)
# even_pos = 0
# odd_pos = 0
# i = 0
# while i<length:
#     if i % 2==0:
#         even_pos += int(n[i])
#     else:
#         odd_pos += int(n[i])
#     i += 1
# print(even_pos-odd_pos)

# Program 18
# n = int(input()) # 1 % 1
# numbers = []
# for i in range(1,n):
#     count = 0
#     for j in range(1,i+1): # 9%
#         if i % j == 0:
#             count += 1
#     if count == 3:
#         numbers.append(i)
# print(numbers)
"""
n = 40

4, 8, 12, 16,20,24,28,32,36,40
6,12,18,24,30,36
common = 4+8+12+16+18+20+24+28+32+36+40

"""
# Program 19
# n = int(input())
# s = set()
# for i in range(1,n):
#     if i % 4 == 0 or i % 6 == 0:
#         s.add(i)
# total = 0
# for i in s:
#     total += i
# print(total)

# Program 20
# n = int(input())
# for i in range(1,n):
#     if i%7 == 0:
#         print(i, end=" ")

# Program 21
# n = int(input())
# for i in range(1,n+1):
#     print(i*5, end=" ")

# Program 22. #
# n = int(input())
# i = 3
# while i < n:
#     remainder = i % 10
#     temp = i
#     if remainder == 3:
#         print(temp,end =" ")
#     i += 1

# Program 23
# n = int(input())
# for i in range(1,n):
#     temp = i
#     digit_sum = 0
#     while temp > 0:
#         digit_sum += temp % 10
#         temp  = temp // 10
#     if digit_sum == 5:
#         print(i, end =" ")

# Program 24
# n = int(input())
# for i in range(1,n):
#     temp = i
#     reversed = 0
#     while temp > 0:
#         remainder = temp % 10
#         reversed = reversed*10 + remainder
#         temp = temp // 10
#     if reversed == i:
#         print(i, end= " ")

# Program 25
# n = int(input())
# for i in range(1,n):
#     count = 0
#     temp = i
#     while temp != 0:
#         temp = temp // 10
#         count += 1
#     if count == 2:
#         print(i,end =" ")

# Program 26
# n = int(input())
# for i in range(1,n):
#     if i % 10 == 0:
#         print(i, end=" ")

# Program 27
# n = int(input())
# for i in range(1,n):
#     temp = i
#     if temp % 4 == 0:
#         last_digit = temp % 10
#         if last_digit == 6:
#             print(i, end=" ")









































