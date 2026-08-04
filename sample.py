j=int(input("Enter which method do you want to use Enter 1:binary , 2:linear  ="))

if j==1:
    l = []

    n = int(input("Enter number of elements "))

    for i in range(0, n):
     e = int(input("Enter a element "))
     l.append(e)

    l.sort()
    print(l)

    key = float(input("Enter the element you want to find "))

    low = 0
    high = len(l) - 1

    while low <= high:
     mid = int((low + high) / 2)

     if key == l[mid]:
        print("Found at postion ", mid + 1)

        break
        

     elif key < l[mid]:
        high = mid - 1

     elif key > l[mid]:
        low = mid + 1

    else:
      print("Element not present in list")

else:
  n=int(input("Enter the number of customer: "))
  Id =[]
  for i in range (n):
    id=int(input("Enter customer id: "))
    Id.append(id)
    
  key=int(input("Enter Account Id to Search: "))

  for i in range(len(Id)):
    if Id[i] == key:
        print("found at position: ",i+1);    
        break
  else:
    print("Not Found")
     