# l=eval(input("Enter a list"))

# print(l[::-1])
# input list
lst = [10, 11, 19, 13, 14, 15]

l = [] 

for i in lst:
	l.insert(len(l)-i,i)
print(l)
