ch=input("1 Create\n 2 Login")
if (ch=="1"):
    #create account
    user=input("username")
    cpass=input("password")
    rpass=input("Cpassword")
    if(cpass==rpass):
        string=""
        file=open('cre.txt','a')
        string+=f",{user}"
        string+=f",{rpass}"
        file.write(string)
        file.close()
elif(ch=="2"):
    file=open('cre.txt','r')
    temp=''
    for x in file.read():
        temp+=x
    temp=temp.split(',')
    mydict={}
    for x in range(1,len(temp),2):
        mydict[temp[x]]=temp[x+1]
    user=input("Enter username")
    cpass=input("Enter password")
    count=0
    for x in mydict.items():
        if(user==x[0] and cpass==x[1]):
            count+=1
    if(count==1):
        print("login success")
    else:
        print("failed")
        