class Queue:
    def __init__(self):
        self.queue = []

    # 1. Enqueue - Add an element
    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to the queue.")

    # 2. Dequeue - Remove the front element
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            item = self.queue.pop(0)
            print(item, "removed from the queue.")

    # 3. Peek / Front - View the first element
    def front(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[0])

    # 4. Rear - View the last element
    def rear(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Rear element:", self.queue[-1])

    # 5. Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # 6. Size - Number of elements
    def size(self):
        print("Queue size:", len(self.queue))

    # 7. Display all elements
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:", self.queue)


# Menu-driven program
q = Queue()

while True:
    print("\n--- QUEUE OPERATIONS ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Rear")
    print("5. Check Empty")
    print("6. Size")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        q.enqueue(item)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.front()

    elif choice == 4:
        q.rear()

    elif choice == 5:
        if q.is_empty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == 6:
        q.size()

    elif choice == 7:
        q.display()

    elif choice == 8:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
