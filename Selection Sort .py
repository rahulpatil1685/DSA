n=int(input("Enter no of Employee :"))

salary = []
for i in range (n) :
   
    id = int(input(f"Enter {i+1} employee's salary :"))
   
    salary.append(id)
# Selection Sort
for i in range(n):
    SI= i

    for j in range(i + 1, n):
        if salary[j] < salary[SI]:
            SI = j

    # Swap salaries
    salary[i], salary[SI] = salary[SI], salary[i]

    # Swap employee names
   

# Display sorted employees
print("\nEmployees sorted by salary:")
for i in range(n):
    print(f"{i+1} Employee's salary =", salary[i])
