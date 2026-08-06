def binary_search(arr,key):
    high=len(arr)
    low=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[]
n=int(input("enter the no of elements in list:"))
for j in range(n):
      nums=int(input(f"enter the {j+1}th number:"))
      arr.append(nums)
if not arr==sorted(arr):
    print("list is not sorted")
key=int(input("enter the key to search:"))
print(binary_search(arr,key))
