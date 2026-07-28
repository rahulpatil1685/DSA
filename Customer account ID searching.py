n=int(input("Enter the number of customer"))
Id =[]
for i in range (n):
    id=int(input("Enter customer id"))
    Id.append(id)
    
key=int(input("Enter Account Id to Search"))

for i in range(len(Id)):
    if Id[i] == key:
        print("found at position",i+1);    
        break
else:
    print("Not Found")
    
    