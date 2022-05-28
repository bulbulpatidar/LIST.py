list = [6,1,3,5,6,3,1]
i=0
p=1
a=[]
while i<len(list):
    if list[i] not in a:
         a.append(list[i])
         p=p*a[i]
    i+=1
print(p)         



list = [6,1,3,5,6,3,1]
p=1
for i in list:
    p=p*i
print(p)

