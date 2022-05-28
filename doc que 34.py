list=[34.67, 12, -94.89, "Python", 0, "C#"]
i=0
l=[]
while i<len(list):
    if type(list[i])==int:
        l.append(list[i])
    i+=1
print(l)        

    

