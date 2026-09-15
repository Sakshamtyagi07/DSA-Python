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
n = int(input())
positive = 0
negative = 0
zero = 0
for i in range(n):
    number = int(input()) 
    if number > 0:
        positive = positive + 1
    elif number < 0:
        negative = negative + 1
    else:
        zero = zero + 1
print(positive)
print(negative)
print(zero)