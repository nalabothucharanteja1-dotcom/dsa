class Stack:
  def __init__(self):
    self.stack = []
  def push(self, element):
    self.stack.append(element)
  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]
  def isEmpty(self):
    return len(self.stack) == 0
  def size(self):
    return len(self.stack)
myStack = Stack()
N=int(input("enetr the no elements in stack:"))
print("enter the elements of Stack")
for i in range(N):
    J=input()
    myStack.push(J)
print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())
print("popped element is:", myStack.pop())
