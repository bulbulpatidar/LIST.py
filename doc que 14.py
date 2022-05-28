a=[[3,5,5],[5,7],[8],[9,11],[13,15,17,16],[4,5,6,7,8,8,9]]
i=0
max=0
min=len(a[0])
n=[]
k=[]
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        n=a[i]
    if len(a[i])<min:
        min=len(a[i])  
        k=a[i]  
    i+=1
print(max,n) 
print(min,k)       


              
                  
