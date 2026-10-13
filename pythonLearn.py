# here i will study and write ,jo bhi mai youtube se padh or seekh rha hu.
#  yha pr tuple se likhna start karuga baki already day wise mention hua h
# tuple same h as list bss ya immutable hoti h which means data can't be change in this and we use parantheis
 
# loop in python question
# Question 1 count positive number
# num = [1,-2,3,-4,5,6,-7,-8,9,10]
# count = 0
# for i in num:
#     if i >=0:
#         count +=1
# print("ans1:",count)    



# # Question 2 sum of even numbers for given number n
# number = int(input())
# total = 0
# for i in range(1,number+1):    # yha number + 1 isliya kiya h kyuki we that number also to be added
#     if i%2 == 0:
#         total = total + i
# print("ans2:",total)    







# Question 3  print the multiplication  for the given number till (like table mai jaisa hota h) but skip 5 itreation
num = 3
# for i in range(1,11):
#     if i != 5:
#         print(i*3,end = ",")

# #  and we also use continue to check the itreation
# num = 3
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i*3)    



# Question 4 reverse a string using a loop
# word = "python"
# final = ""
# for char in word:
#     final = char + final
# print(final)
    
    


# Question 5 find the first none repeated character
# apple = "teeter"
# for char in apple:
#     if apple.count(char) == 1:
#         print(char)
#         break





#Question 6 compute a factorial of a number using loop
# n = int(input())
# factorial = 1
# while n >0:
#     factorial = factorial * n
#     n = n - 1
# print(factorial)






#Question 7 validate input ,number should be between 1 to 10
# while True:
#     n = int(input())
#     if n > 0 and  n < 11:
#         print( "is a valid number")
#         break






#Question 8 check whether the number is prime or not
# n = int(input())
# for i in range(2,n):
#     if n % i == 0:
#         print("Not a Prime Number")
#         break
#     else:
#         print("Is a prime number")
#         break    





#Question 9 check in the list every element should be uniques otherwise exit the loop and print that element
