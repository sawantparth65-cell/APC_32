"""arr=[10,20,30,40,50,60,70,80]
target=int(input("Enter the target number: "))
low=0
high=len(arr)-1

found=False
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        print("Target found at index:", mid)
        found=True 
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1

if found==False:
      print("Target not found in the array.")
"""

"""fruits = ["apple", "banana","cherry","date","elderberry","mango"]
target=input("Enter the fruit to find: ")  
low=0
high=len(fruits)-1

found=False

while low<=high:
    mid=(low+high)//2
    if fruits[mid]==target:
        print("Target found at index:", mid)
        found=True 
        break
    elif fruits[mid]<target:
        low=mid+1
    else:
        high=mid-1

if found==False:
      print("Target not found in the array.")"""

arr=[10,10,15,20,20,30,50,50,60]
target=int(input("Enter the number to find: "))
low=0
high=len(arr)-1

first=-1

while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        first=mid
        high=mid-1 
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1

if first != -1:
    print("First occurrence of target found at index:", first)
else:
    print("Target not found in the array.")