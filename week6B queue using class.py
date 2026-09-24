class queueex:
    def _init_(self):
        self.size=size
        self.queue=
        self.front= None
        self.rear =None
    def enqueue(self,x):
        new = Node(x)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next=new
            self.rear = new
        print(item, "inserted into the queue")
    def dequeue(self):
        if self.front is None:
            print("queue underflow")
        else:
            x = self.front.next
            self.front = self.front.next
            if self.front is None:
                self.rear = None
        print(f"{x} deleted from the queue:")

    def peek(self):
        if self.front is None:
            print("queue is empty")
        else:
            print("front element:", self.front.data)
    def display(self):
        if self.front is None:
            print("queue is empty:")
        else:
            print("the elements are:")
            temp =self.front
            while temp is not None:
                print(temp.data)
                temp=temp.next

size=int(input("enter the the size:"))
q=queueex(size)
while True:
    print("1.enqueue")
    print("2. dequeue")
    print("3. peek")
    print("4. display")
    print("5. exit")
    choice= int(input("enter your number"))
    if choice == 1:
        item = int(input("enter the element to enqueue"))
        q.enqueue(q,item)
    elif choice==2:
        q.dequeue()
    elif choice==3:
        q.peek()
    elif choice==4:
        q.display()
    elif choice ==5:
        print("loop is exited")
        break;
    else:
        print("number is not valid")
