l=[1,2,3,4,1,2,4,56,5,1]
target=int(input("Enter the desired number"))
count=0
for i in l:
    if (target==i):
        count+=1
print(f"occurence of {target} is {count}")
