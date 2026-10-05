# Q17 — Find the Missing Number
# Now we're moving to a new array pattern.
# You are given an array containing numbers from 0 to n, with exactly one number missing.
# arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# n = len(arr)
# expectedSum = n*(n+1)//2
# actualSum = 0
# for j in arr:
#     actualSum += j
# missing = expectedSum - actualSum 
# print(missing)    
    
    
    
# Q18 — Find the Duplicate Number
# Now we move to a new array pattern: duplicate detection.

# arr = [1, 3, 4, 2, 2]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] == arr[j]:
#             print(arr[i])
    
     
# Q19 — Find the Second Largest Element
# arr = [10, 5, 20, 8, 20, 15]
# largest = float("-inf")
# sec = float('-inf')
# for i in range(len(arr)):
#     if arr[i] > largest :
#         sec = largest
#         largest = arr[i]
#     elif largest > arr[i] and arr[i] > sec:
#         sec = arr[i]    
# print(sec)        


# Q20 — Left Rotate an Array by 1 Position