# Q11 — Count Occurrences
# arr = [10, 25, 10, 40, 10, 15, 25]
# target =int(input())
# count = 0
# for i in range(len(arr)):
#     if target == arr[i]:
#         count = count + 1
# print(count)         


# Q12 — Reverse an Array
# Do not use .reverse().
# Do not use slicing [::-1].
# arr = [10, 20, 30, 40, 50]
# a = len(arr)
# for i in range(a-1,-1,-1):
#     print(arr[i])


# Q13 — Reverse the List In-Place
# arr = [10, 20, 30, 40, 50]
# n = len(arr)
# left = 0
# right = n-1
# for i in range(n//2):
#     arr[left],arr[right] =arr[right],arr[left]
#     left += 1
#     right -= 1

# print(arr)


# Q14 — Find the Second Largest Element
# arr = [10, 25, 7, 25, 40, 18, 30]
# largest = float("-inf")
# second =  float("-inf")
# for i in range(len(arr)):
#     if arr[i] > largest :
#         second = largest
#         largest = arr[i]
#     elif largest > arr[i] and arr[i] > second:
#          second = arr[i]
# print(second)


# Q15 — Move All Zeros to the End
# arr = [0, 1, 0, 3, 12] 
# pos = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[pos],arr[i]=arr[i],arr[pos]
#         pos +=1
# print(arr)

