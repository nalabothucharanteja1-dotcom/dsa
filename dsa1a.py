def count_down(i):
    if i>=0:
        print(f"{i}")
        count_down(i-1)
count_down(10)
print("rocket launched")
