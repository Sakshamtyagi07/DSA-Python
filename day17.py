# Q17 — Find the Missing Number
# Now we're moving to a new array pattern.
# You are given an array containing numbers from 0 to n, with exactly one number missing.
arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(arr)
expectedSum = n*(n+1)//2
actualSum = 0
for j in arr:
    actualSum += j
missing = expectedSum - actualSum 
print(missing)    
    
    