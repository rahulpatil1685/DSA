# Student Management System using Singly Linked List

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # Add student
    def add_student(self, roll_no, name, marks):
        new_student = Student(roll_no, name, marks)

        if self.head is None:
            self.head = new_student
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_student

        print("Student added successfully!")

    # Display students
    def display_students(self):
        if self.head is None:
            print("No students found.")
            return

        temp = self.head

        print("\nStudent Details:")
        while temp is not None:
            print("Roll No:", temp.roll_no)
            print("Name:", temp.name)
            print("Marks:", temp.marks)
            print("------------------")

            temp = temp.next

    # Search student
    def search_student(self, roll_no):
        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("\nStudent Found!")
                print("Roll No:", temp.roll_no)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                return

            temp = temp.next

        print("Student not found.")

    # Delete student
    def delete_student(self, roll_no):
        if self.head is None:
            print("No students found.")
            return

        # If first student has the roll number
        if self.head.roll_no == roll_no:
            self.head = self.head.next
            print("Student deleted successfully!")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.roll_no == roll_no:
                temp.next = temp.next.next
                print("Student deleted successfully!")
                return

            temp = temp.next

        print("Student not found.")


# Main program
students = StudentList()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students.add_student(roll_no, name, marks)

    elif choice == "2":
        students.display_students()

    elif choice == "3":
        roll_no = int(input("Enter Roll No to search: "))
        students.search_student(roll_no)

    elif choice == "4":
        roll_no = int(input("Enter Roll No to delete: "))
        students.delete_student(roll_no)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
