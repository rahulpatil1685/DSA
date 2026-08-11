n=int(input("Enter total number Employee "))
sal = []
for i in range(0,n):
    id = int(input(f"Enter {i+1} employee salary :"))
    sal.append(id)

#Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if sal[j] > sal[j + 1]:
            sal[j], sal[j + 1] = sal[j + 1], sal[j]

print("Sorted salaries:", sal)

# Top 5 highest salaries
print("Top 5 highest salaries:", sal[:-6:-1])
