# n = int(input())
# if n >= 0:
#     if n == 0:
#         print("Zero")
#     else:
#         print("Positive")
# else:
#     print("Negative")            



### print number from 1 to n

# n = int(input())
# for i in range(1,n+1):
#     print(i)



### print n to 1
# n = int(input())
# for i in range(n,0,-1):
#     print(i)


##  Sum from 1 to N
# n = int(input())
# a = 0
# for i in range(1,n+1):
#     a = a + i
# print(a)
      
      
# Count Even Numbers
# n = int(input())
# count = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         count = count + 1
# print(count)     
        
        
# Count Positive, Negative, and Zero
# n = int(input())
# positive = 0
# negative = 0
# zero = 0
# for i in range(n):
#     number = int(input()) 
#     if number > 0:
#         positive = positive + 1
#     elif number < 0:
#         negative = negative + 1
#     else:
#         zero = zero + 1
# print(positive)
# print(negative)
# print(zero)


#sum of even numbers
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         sum = sum + i
# print(sum)


#Assessment Q1
# Write a program that takes an integer n and prints:
# Positive Even if n is positive and even
# Positive Odd if n is positive and odd
# Negative Even if n is negative and even
# Negative Odd if n is negative and odd
# Zero if n is zero


# n = int(input())
# if n > 0:
#     if n % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")
# elif n < 0:
#     if n % 2 == 0:
#         print("Negative Even")
#     else:
#         print("Negative Odd")
# else:
#     print("Zero")                      



# Problem
# Take an integer n as input and calculate the sum of all odd numbers from 1 to n.

# n = int(input())
# s = 0
# for i in range(0,n+1):
#     if i % 2 != 0:
#         s = s + i
# print(s)        




# Problem
# First input an integer n.
# Then input n numbers.
# Count how many of those numbers are:
# Positive
# Negative
# Zero
# Finally print the three counts in that order


# n = int(input())
# p = 0
# m = 0
# z = 0
# for i in range(n):
#     num = int(input())
#     if num > 0:
#         p = p + 1
#     elif num < 0:
#         m = m + 1
#     else:
#         z = z + 1 
# print(p)
# print(m)
# print(z)                 



# Problem
# Input an integer n, then input n numbers.
# Find and print the largest number among them.

n = int(input())
largest = int(input())
for i in range(n - 1):
    num = int(input())
    if num > largest:
        largest = num
print(largest)



