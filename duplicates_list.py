l=eval(input("Enter a list"))
unique_list=[]
duplicate_list=[]
count=0
for i in l:
    if i not in unique_list:
        unique_list.append(i)
    elif i not in duplicate_list:
        duplicate_list.append(i)
print(duplicate_list)

