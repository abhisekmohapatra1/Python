name=input("Name").split()
demo =""

for x in range (len(name)):
    if(x%2==0):
        temp=name[x]
        demo+=temp[:len(temp)//2].upper()
        demo+=temp[-len(temp)//2:].lower()
    else:
        temp=name[x]
        demo+=temp[:len(temp)//2].lower()
        demo+=temp[-len(temp)//2:].upper()  
    demo+=" "
print(demo)
