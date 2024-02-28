l=eval(input("Enter the elements of the list:"))
min=l[0]
for i in l:
    if i<min:
        min=i
print("Min is :",min)