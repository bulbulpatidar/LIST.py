n=[1,2,3,1,2,2]
i=0
l=[]
while i<len(n):
    if n[i] not in l:
        l.append(n[i])
    i+=1
print(l) 
 