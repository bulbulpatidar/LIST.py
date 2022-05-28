# l=[]
# list=int(input("enter the number"))
# i=1
# while i<=list:
#     i+=1
#     n=int(input("enter the element"))
#     l.append(n)
# print(l)
l=[3,3,2,3,3,4,5,6,4,4,5,5]
k=3
b=[]
i=0
while i<len(l):
    # n=l[i]
    j=0
    c=0
    while j<len(l):
        if l[i]==l[j]:
            c=c+1
        j+=1
    if c>=k:
        if l[i] not in b:

            b.append(l[i]) 
    i+=1
print(b)                   







