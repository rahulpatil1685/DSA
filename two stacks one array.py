class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, value):
        if self.top1 + 1 == self.top2:
            print("Stack Overflow")
        else:
            self.top1 += 1
            self.arr[self.top1] = value

    def push2(self, value):
        if self.top1 + 1 == self.top2:
            print("Stack Overflow")
        else:
            self.top2 -= 1
            self.arr[self.top2] = value

    def pop1(self):
        if self.top1 == -1:
            print("Stack 1 is empty")
        else:
            value = self.arr[self.top1]
            self.top1 -= 1
            print("Popped from Stack 1:", value)

    def pop2(self):
        if self.top2 == self.size:
            print("Stack 2 is empty")
        else:
            value = self.arr[self.top2]
            self.top2 += 1
            print("Popped from Stack 2:", value)

    def display(self):
        print("Array:", self.arr)


# Taking input
size = int(input("Enter array size: "))

stacks = TwoStacks(size)

n1 = int(input("How many elements in Stack 1? "))
for i in range(n1):
    value = int(input("Enter element for Stack 1: "))
    stacks.push1(value)

n2 = int(input("How many elements in Stack 2? "))
for i in range(n2):
    value = int(input("Enter element for Stack 2: "))
    stacks.push2(value)

stacks.display()

# Pop operations
stacks.pop1()
stacks.pop2()

stacks.display()
