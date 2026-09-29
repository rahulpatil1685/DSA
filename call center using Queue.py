# Call Center Management System using Queue

class CallCenter:
    def __init__(self):
        self.queue = []

    # Add customer to queue
    def add_customer(self, name, phone):
        customer = {
            "name": name,
            "phone": phone
        }

        self.queue.append(customer)
        print("Customer added to the queue.")

    # Handle first customer
    def handle_call(self):
        if len(self.queue) == 0:
            print("No customers waiting.")
        else:
            customer = self.queue.pop(0)

            print("\nHandling Call...")
            print("Customer Name:", customer["name"])
            print("Phone Number:", customer["phone"])
            print("Call handled successfully.")

    # Display waiting customers
    def display_queue(self):
        if len(self.queue) == 0:
            print("No customers are waiting.")
        else:
            print("\nWaiting Customers:")

            for i, customer in enumerate(self.queue, start=1):
                print(i, ".", customer["name"],
                      "-", customer["phone"])

    # Show number of waiting customers
    def waiting_count(self):
        print("Total waiting customers:", len(self.queue))


# Main program
call_center = CallCenter()

while True:
    print("\n===== CALL CENTER =====")
    print("1. Add Customer")
    print("2. Handle Call")
    print("3. Display Queue")
    print("4. Number of Waiting Customers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")

        call_center.add_customer(name, phone)

    elif choice == "2":
        call_center.handle_call()

    elif choice == "3":
        call_center.display_queue()

    elif choice == "4":
        call_center.waiting_count()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
