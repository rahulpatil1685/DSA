MAX = 5
stack = []
top = -1  # Here, top is a global variable.


# PUSH Operation
def push():
    global top

    # Without global top, Python treats top inside the function
    # as a local variable, causing an error when we try to use its previous value.
    if top == MAX - 1:
        print("Stack Overflow! Stack is Full.")
    else:
        item = int(input("Enter element to push: "))
        top = top + 1
        stack.append(item)
        print(item, "inserted into the stack.")


# POP Operation
def pop():
    global top

    if top == -1:
        print("Stack Underflow! Stack is Empty.")
    else:
        item = stack.pop()
        top = top - 1
        print(item, "deleted from the stack.")


# PEEK Operation
def peek():
    if top == -1:
        print("Stack is Empty.")
    else:
        print("Top element is:", stack[top])


# DISPLAY Operation
def display():
    if top == -1:
        print("Stack is Empty.")
    else:
        print("Stack elements are:")
        for i in range(top, -1, -1):
            print(stack[i])


# isEmpty Operation
def is_empty():
    if top == -1:
        print("Stack is Empty.")
    else:
        print("Stack is Not Empty.")


# isFull Operation
def is_full():
    if top == MAX - 1:
        print("Stack is Full.")
    else:
        print("Stack is Not Full.")
        print("Available space:", MAX - 1 - top)


# Main Menu
while True:
    print("\n========== STACK MENU ==========")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. isEmpty")
    print("6. isFull")
    print("7. EXIT")
    print("================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        is_empty()
    elif choice == 6:
        is_full()
    elif choice == 7:
        print("Program terminated.")
        break
    else:
        print("Invalid choice! Please try again")
