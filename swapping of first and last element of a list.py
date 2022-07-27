l=[]
n=int(input("Enter number of elementts:"))
for i in range(0,n):
    a=int(input("enter number:"))
    l.append(a)
#l=[1,4,6,8]
l[0],l[-1]=l[-1],l[0]
print(l)
