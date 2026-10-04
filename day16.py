# # Slicing
# arr = [0,1,2,3,4,5,6,7,8,9]
# print(arr[:6])
# print(arr[:-1])
# print(arr[5:])
# print(arr[-1:-5])
# print(arr[0:7:3])




# List and array same he hota h python mai 
# arr = ["hat","pet","cat","mat"]
# for i in arr:
#     print(i,end="+")      #yha '''end''' denote kr rha h ki humrha loop next line mai nhi jayega same line hoga or jo humna uska andar diya hoga voh aa jayega.
#     if 'hat' in arr:
#         print("hat h bhyii")


# apple = [x**2 for x in range(10)]  #ya loop ke andar se comperhension hua h ismai humna list ke andar ke loop laga diya h.
# print(apple)
   
   
   


# Q16 — Move All Negative Numbers to One Side
# Rules
# Modify the array in-place
# Don't create a second list
# Don't use .sort()
# Use a loop
# Try for O(n) time and O(1) extra space


arr = [2, -3, 4, -1, 0, -5, 7]
pos=[]
for i in arr:
    if i < 0:
        pos.append(i)
        arr.pop(i)
    
        