# largest number 
# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# elif a == b:
#     print(a)
# else:
#     print(b)

#largest of three number
# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= c:
#     print(a)
# elif b > c and b > a:
#     print(b)
# else:
#     print(c)    

# n divisible by 3 and 5
# n = int(input())
# if n % 3 == 0 or n % 5 == 0:
#     print("Yes")
# else:
#     print("No")


#Grade calculator
# n = int(input())
# if n >= 90 and n <= 100:
#     print("A")
# elif n >= 80 and n < 90:
#     print("B")
# elif n >= 70 and n < 80:
#     print("C")
# elif n >= 60 and n < 70:
#     print("D")
# else:
#     print("F")


#Leap year
#conditon for leap year is (it should be divisible by 400) or (divisible by 4 and not divisible by 100)
# year = int(input())
# if (year % 400 == 0 )or( year % 4 ==  0 and year % 100 != 00):
#     print("It's a leap Year")
# else:
#     print("Not a leap year")


# print absolute value
# n = int(input())
# if n > 0:
#     print(n)
# elif n < 0:
#     print(n * -1)
# else:
#     print(0) 



#check divisiblity of number
# n = int(input())
# if n % 3 == 0 and n % 5 == 0:
#     print("Both")
# elif n % 3 == 0 and n % 5 != 0:
#     print("three")
# elif n % 3 != 0 and n % 5 == 0:
#     print("five")
# else:
#     print("Neither")



#Electricity Bill
# Now we're going to start using multiple conditions based on ranges, but in a more practical problem.
# An electricity company charges according to the number of units consumed:
# Units	Rate
# First 100 units	₹5/unit
# Next 100 units (101–200)	₹7/unit
# Above 200 units	₹10/unit

# bill = int(input())

# if bill <= 100:
#     print(bill*5)
# elif bill > 100 and bill <= 200:
#     print(100*5 + (bill-100)*7)
# else:
#     print(100*5 + 100*7 + (bill-200)*10)




##############  vowel check
n = input()
if n in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    print("Vowel")
elif n.isdigit():
    print("Number")
else:
    print("consonant") 