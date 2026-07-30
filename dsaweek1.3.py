def emp(id):
    n=len(arr)
    i=0
    while i<=n-1:
        if arr[i]==id:
            print(f"{id} present at {i}th index of the list")
            return i
        else:
            i=i+1
    else:
        print("id of the employee not found in the list")
arr=[25001, 25002, 25003, 25004,25005,25006]
emp(25005)
