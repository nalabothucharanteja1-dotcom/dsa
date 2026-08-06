def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=[]
n=int(input("enter the no of elements in list:"))
for j in range(n):
      nums=int(input(f"enter the {j+1}th number:"))
      arr.append(nums)
key=int(input("enter the key"))
print(linear_search(arr,key))
