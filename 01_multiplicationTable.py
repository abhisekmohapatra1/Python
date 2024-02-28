# num=(int(input("Enter a number")))
# print("Multiplication table of",num,"is :")
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

for i in range(0,100):
    num=i
    if(num>1):
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)