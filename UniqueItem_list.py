l=eval(input("Enter a list :"))
count=0
l1=[]
for i in l:
    if i not in l1:
        count+=1
        l1.append(i)
print("The unique items in the list are:",count,"they are",l1)