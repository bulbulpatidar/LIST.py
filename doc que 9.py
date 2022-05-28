l=[]
n=int(input("enter number of element"))
i=1
while i<=n:
    i+=1
    e=int(input("enter the element"))
    l.append(e)
print(l) 
i=0
max=0
max2=0
max3=0
while i<len(l):
    if l[i]>max:
        max=l[i]
    i+=1  
i=0
while i<len(l):
    if l[i]>max2 and l[i]!=max:
        max2=l[i]
    i+=1
i=0
while i<len(l):
    if l[i]>max3 and l[i]!=max2 and l[i] !=max:
        max3=l[i]  
    i+=1     
print("maximum ",max)
print("second maximum",max2)
print("tird maximum",max3)    



