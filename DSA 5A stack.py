stack = []
N=int(input("enetr the no elements in stack:"))
print("enter the elements of Stack")
for i in range(N):
    J=int(input())
    stack.append(J)
print("Stack: ", stack)
topElement = stack[-1]
print("Peek: ", topElement)
popped = stack.pop()
print("Pop: ", popped)
print("Stack after Pop: ", stack)
pu="U"
push=stack.append(pu)
print("stack after pushed is", stack)
print("Size: ",len(stack))
