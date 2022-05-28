# a=[4,6,2,0,2,0,4]
# l=[]
# b=[]
# for i in a:
#     if i==0:
#         l.append(i)
#     else:
#         b.append(i)
# print(b+l)

# a=[0,5,6,7,0,7,0,8]
# l=[]
# b=[]
# i=0
# while i<len(a):
#     if a[i]==0:
#         l.append(a[i])
#     else:
#         b.append(a[i])  
#     i+=1
# print(b+l)     

# 
# l=[]
# n=int(input("enter the num"))
# i=1
# while i<=n:
#     i+=1
#     e=int(input("enter the element"))
#     l.append(e)
# print(l)    


# a=[2,4,6,[5,4],[5,7]]
# i=0
# # l=[]
# sum=0
# while i<len(a):
#     if type(a[i])==int:
#         # l.append(a[i])
#         sum+=a[i]
#     i+=1
# # print(l)    
# print(sum)  

# l=[20,10,20,30,10,40,50]
# op=[]
# for i in l:
#     if l.count(i)==1:
#         op.append(i)
# print(op) 




# l=[[3,4,5,6,7,8],[1,2,3,4,],[3,4,5]]
# i=0
# maxl=0
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         if len(l[i])>(maxl):
#            maxl=len(l[i])
#            print(l[i])
        
#         j+=1
#     i+=1
# print(maxl) 

# l=[3,2,4,5,6,11,12,8]
# n=int(input("enter the number ; "))
# i=0
# c=[]
# d=[]
# while i<len(l):
#     if l[i]>n:
#         if l[i]%2==0:
#             c.append(l[i])
#         else:
#             d.append(l[i])    
#     i+=1
# print(c) 
# print(d)    


# # # 
# # # 
# # 
# a=[2,4,3,2,1,4,3,6]
# i=0
# count=0
# l=[]
# while i<len(a):
    
#     if a[i]%2==0:
#        l.append(a[i])
#        count=count+1
#     i+=1
# print(l)    
# print(count)       
       

# a=["b","l","a","c","k"]
# i=0
# sum=""
# while i<len(a):
#     sum+=a[i]
#     i+=1
# print(sum)   



# l=["abcd1234"]

# i=0
# while i<len(l):
#      print(l[i][::-1])
#      i+=1


# b=[23,45,36,89]
# i=0
# k=[]
# while i<len(b):
#     c=b[i]%10
#     b[i]=b[i]//10
#     k.append(c+b[i])
#     i+=1
# print(k)   

# # # 



# l=[[3,4,5],[5,6,7],[6,4,5]]
# i=0
# b=[]
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         a=l[i][j]
#         b.append(a)
#         j+=1
#     i+=1
# print(b)        


# l=[2,2,4,5,6,2,3,4,5,6,7]
# op=[]
# for i in l:
#     if l.count(i)==1:
#         op.append(i)
# print(op)
# # 
# # 
# 

  
# l=[2,2,4,5,6,2,3,4,5,6,4]
# i=0
# op=[]
# while i<len(l):
#     if l.count(l[i])==1:
#         op.append(l[i])
#     i+=1
# print(op) 


# number=[1,9,2,3,10,5,6,13]
# i=0
# a=number[i]
# list=[]
# while (i<len(number)):
#     b=number[i]
#     # print(b)
#     if b>a:
#         a=b
#         # print(a)
#     i+=1
#     list.append(a)
# print(list)


    
       
            

    








    
      




# a=["dd30","ss40","aa60"] 
# i=0
# b=[]
# while i<len(a):
#     j=0
#     c=" "
#     while j<len(a[i]):
#         if a[i][j]>="0" and a[i][j]<="9":
#             c+=a[i][j]
#         j+=1
#     b.append((c))
#     i+=1
# print(b)
      





# a=[100,1000,1900,1200,1300]
# i=0
# l=[]
# while i<len(a):
#     j=0
#     c=""
#     k=str(a[i])
#     while j<len(k):
#         if k[j]!="0":
#             c=c+k[j]
#         j+=1
#     l.append(int(c))    
#     i+=1
# print(l)  



    
    
    
#

# a=[10,20,30,40,50]
# b=[100,200,300,400,500]
# i=0
# c=1
# while i<len(a):
#     l=a[i],b[-c]
#     print(l) 
#     i+=1
#     c+=1
#     # print(l)

# l=[1,2,3,4,5,6,7,8,8,9]  
# i=0
# b=[]
# while i<len(l)-1:
#     c=str(l[i])+str(l[i+1])
#     b.append(c)
#     i+=2
# print(b)    

# l=[[1,2,7],[4,5,6],[8,9,10]]
# i=0
# a=[]
# while i<len(l):
#     j=0
#     max=0
#     while j<len(l[i]):
#         if l[i][j]>max:
#             max=l[i][j]
#             j+=1
#     i+=1
#     print(max,end=" ") 
#     # a.append(max)    


#
   
# l=input("enter the name")
# # l="monika" 
# i=0
# while i<len(l):
#     j=0
#     while j<=i:
#         print(l[i],end=" ")
#         j+=1
#     print()
#     i+=1  
# # 



# l=["12", "shubh", "76", "teju","60"]
# # o/p= ["12","76"]
# i=0
# m=[]
# while i<len(l):
#     if l[i]>="0" and l[i]<="9":
#         m.append(l[i])
#     i+=1
# print(m)  


# l=["12", "shubh", "76", "teju","60"]
# # o/p= ["12","76"]
# i=0
# m=[]
# while i<len(l):
#     if l[i]>="a" and l[i]<="z":
#         m.append(l[i])
#     i+=1
# print(m)  
                

# l=[2,3,7,8,12,6]
# i=0
# max=0
# min=l[0]
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#     if l[i]<min:
#          min=l[i] 
#     i+=1
# print(max)
# print(min)
# print(max+min) 


# l=[2,3,4,5,6,7,5]
# n=int(input("enter the number"))
# i=0
# sum=0
# while i<len(l):
#     if l[i]<n:
#         sum+=l[i]
#     i+=1
# print(sum)  

# n=[2,3,4,5,6,8,9] 
# b=int(input("enter the number : "))
# for i in n:
#     if i<=b:
#        k=b-i
#        print(k)

 
# n=[3,4,5,6,7,3,2]
# b=int(input("enter the number"))
# i=0
# while i<len(n):
#     if n[i]<=b:
#        k= b-n[i]
#        print(k)
#     i+=1
# print(k)    


# l=[-1,2,-3,4,-5,-6,7] 
# i=0
# count=0
# count1=0
# b=[]
# c=[]
# while i<len(l):
#     if l[i]>=0:
#         k=1
#         b.append(k)
#         count+=1
#     elif l[i]<0:
#         n=0
#         c.append(n)
#         count1+=1
#     i+=1
# print(b,count)
# print(c,count1)   

# 
# n=int(input("enter the no :"))
# l=[2,4,5,7,8,3,5]
# i=0
# k=n
# while i<len(l):
#     if l[i]<n:
#         # print(l[i])
#         k=k-l[i]
#     i+=1
# print(k)




# a=[6,2,3,4,6,7,8]
# b=(a[6:]+a[:6])
# # print(b)

# b.pop(1)
# # print(b)
# b.append(6)
# print(b)


# 
# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
         
# l=['abca', 'xyx', 'aba', '1221']
# c=0
# for i in l:
#     # if len(i)>1 and i[0]==i[-1]:
#     if i[0]==i[-1]:

#         c+=1
# print(c)





# ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# l=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# del l[0]
# del l[3:6]
# print(l)





# def last(n): return n[-1]

# def sort(tuples):
#   return sorted(tuples, key=last)

# print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))






# l="The quick brown fox jumps over the lazy dog"
# m=[]
# txt=l.split(" ")
# # print(txt)
# n=int(input("enter the number"))
# for i in txt:
#     if len(i)>n:
#         m.append(i)
# print(m)        




# l1=[1,2,3,4,5]
# l2=[6,7,8,9]
# c=0
# c2=0
# for i in l1:
#     for j in l2:
#         if i==j:
#             c+=1
#         # else:
#             # c2+=1 
# if c>=1:
#     print("True") 
# else:
#     print("false")   

# 
# # write a Python program to generate a 3*4*6 3D array whose each element is *.
# array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
# print(array)

            
# Write a Python program to print the numbers of a specified list after removing even numbers from it.
# num = [7,8,12,5,6,4,]
# l=[]
# for i in num:
#     if i%2!=0:
#         l.append(i)
# print(l)





# Write a Python program to shuffle and print a specified list.
# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)


# l=[1,2,3,4,5,6,7,8,9,10]
# m=[]
# i=0
# c=""
# while i<len(l):
#     if l[i]==3 or l[i]==6:
#         m.append(l[i])
#     if l[i]==8 or l[i]==9 or l[i]==10:
#         c+=str(l[i])   


#     i+=1
# m.append(int(c))       
# print(m) 



# # Write a Python program to generate all permutations of a list in Python.
# n=eval(input("enter the number:-"))
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         k=0
#         while k<len(n):
#             if i!=j and i!=k and j!=k:
#                 print(n[i],n[j],n[k])
#             k+=1
#         j+=1 
#     i+=1           

# l1 = [1, 3, 5, 7, 9]
# l2=[1, 2, 4, 6, 7,8]
# m=[] 
# for x in l1:
#     if x not in l2:
#         m.append(x) 
# for y in l2:
#     if y not in l1:
#         m.append(y) 
# print(m)                             
        


# l=[1,2,[3,4],[5,6]] 
# i=0
# s=0
# while i<len(l):
#     if type(l[i])==list:  
#         j=0
#         while j<len(l[i]):
#             s+=l[i][j]
#             j+=1
#     else:
#         s+=l[i]
#     i+=1
# print(s)                
            
# l=[1,2,3]
# l1=[3,2,1]
# i=0
# multi=1
# while i<len(l):
#     multi*=l[i]*l1[i]
#     i+=1
# print(multi)   


# l=[2,4,7,[8,9,7],4,3,9]
# i=0
# a=[]
# b=[]
# sumE=0
# sumO=0
# while i<len(l):
#     if type(l[i])==int:
#         if l[i]%2==0:
#             a.append(l[i])
#             sumE+=l[i]
#         else:    
#             b.append(l[i])
#             sumO+=l[i]
#     else:
#         j=0
#         while j<len(l[i]):
#             if l[i][j]%2==0:
#                 a.append(l[i][j])
#                 sumE+=l[i][j]
#             else:
#                 b.append(l[i][j]) 
#                 sumO+=l[i][j] 
#             j+=1              
#     i+=1
# print("even num sum",a,sumE)
# print("odd num sum",b,sumO) 



# a=[1,2,3,4,5,6]
# i=0
# l=[]
# while i<len(a):
#     # k=a[i]
#     l.append(a[i])
#     i+=1
#     print(l)    


# l=["monkey","monk","monday"]
# i=0
# c=0
# while i<len(l):
#     if "mon" in l[i]:
#         # print("mon")
#         c+=1
#     i+=1 
# if c==len(l):
#     print("mon")   


# l=[1,2,3,4,5,6,7,8,9,10]
# b=l[2:6:3]
# c=l[7:11]
# print(b+c)







# l=[4,5,1,9,7,3,4]
# # op=[4,2,4,0,0,1,0]
# i=0
# l1=[]
# while(i<len(l)):
#     maximum=l[i]
#     count=0
#     j=(i+1)
#     while(j<len(l)):
#         if l[j]>=maximum:
#             count+=1
#         j+=1
#     l1.append(count)
#     i+=1
# print(l1)




# l=[123,1496,12,4,512]
# i=0
# l1=[]
# while(i<len(l)):
#     n=l[i]
#     sum=0
#     while(n>0):
#         s=n%10
#         n=n//10
#         sum+=s
#     l1.append(sum)
#     i+=1
# print(l1)


# # l=["sakshi","rajyhjhj","sonali","preeti"]
# # l.sort()
# i=0
# max=0
# while i<len(l):
#     if len(l[i])>max:
#         max=len(l[i])
#         n=l[i]
#         print(n)
#     i+=1
# print(max) 

# a=[9,10,15,6,4,12]
# i=0
# max=0
# max2=0
# max3=0
# min1=a[0]
# min2=a[0]
# min3=a[0]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[j]>max:
#             max=a[j]
#         if a[j]>max2 and a[j]!=max:
#             max2=a[j]  
#         if a[j]>max3 and a[j]!=max2 and a[j]!=max: 
#             max3=a[j] 
#         if a[j]<min1:
#             min1=a[j]  
#         if a[j]<min2 and a[j]!=min1:
#             min2=a[j]      
#         j+=1        
#     i+=1
# print(max)
# print(max2) 
# print(max3)
# print(min1) 
# print(min2)     



# a=[0,1,2,3,4,5]
# h=[]
# i=0
# while i<len(a):
#     j=i+1
#     while j<len(a):
#         h.append(a[j])
#         h.append(a[i])
#         j=j+2
#         i=i+2
# print(h)





# l=[2,7,11,15,17]
# i=0
# h=[]
# while i<len(l):
#     j=i+1
#     while j<len(l):
#         if l[i]+l[j]==9:
#             # print(i,j)
#             h.append(i)
#             h.append(j)
#         j+=1
#     i+=1
# print(h)        

# a=[49,56,78]
# i=1
# count=0
# while i<len(a):
#     count=count+1
#     i=i+1
#     b=int(count/2)
# print((a[b]))


   


# a="my name is poojaa "
# b=a.split()
# # print(b)
# print(len(b[-1]))
# print(b[:-1])


# a="my name is bulbul"
# # b=[]
# # b.append(a)
# i=0
# while i<len(a):
#     if i==11:
#         print(len(a[i:]))
#     i+=1    

# l=[2,3,4,5,6,7]
# i=0
# while i<len(l):
#     if i%2==0:
#         a=1
#         while a<=10:
#             print(l[i]*a)
#             a+=1
#     i+=1    




# l=[1,1,2,3,4,4]
# i=0
# m=[]
# c=0
# while i <len(l):
#     if l[i] not in m:
#         m.append(l[i])
#     i+=1
# i=0
# k=[]
# while i<len(m):
#     j=0
#     c=0
#     while j<len(l):
#         if m[i]==l[j]:
#             c+=1
#         j+=1
#     if c>1:
#         k.append([c,m[i]])
#     else:
#         k.append(m[i])
#     i+=1
# print(k)                    


# m=[4,5,[4,[4,3],9,[2,4]]]
# i=0
# b=[]
# while i<len(m):
#     if type(m[i])==list:
#         j=0
#         while j<len(m[i]):
#                b.append(m[i][j])
#                j+=1
#     else:
#         b.append(m[i])
#     i+=1
# print(b)
# i=0
# c=[] 
# while i<len(b):
#     if type(b[i])==list:
#         j=0
#         while j<len(b[i]):
#             c.append(b[i][j])
#             j+=1
#     else:
#         c.append(b[i])
#     i+=1
# print(c)     

# 
# l=[0,1,0,1,1,0,0]
# i=0
# k=[]
# while i<len(l):
#     j=0
#     c=0
#     b=l[:i]
#     while j<len(b):
#         if l[j]==0:
#             c+=1
#         j+=1
#         # print(c)
#     k.append(c) 
#     i+=1
# print(k)          


# l=[[5,3,4],[4,6,7],[8,6,5]]
# i=0
# b=[]
# c=[]
# d=[]
# k=[]
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#        if j==0:
#           b.append(l[i][j])
#        elif j==1:
#            c.append(l[i][j]) 
#        elif j==2:
#            d.append(l[i][j])
#        j+=1
#     i+=1
# k.append(b)
# k.append(c)
# k.append(d)
# print(k)    

# a=[[1,2],[2,3],[3,2,3,4]]
# i=0
# l=[]
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a[i]):
#         c+=1
#         j+=1
#     l.append(c)    
#     i+=1
# print(l) 
# # 
# 
# a="priti"
# b=len(a)
# i=0
# m=[]
# while i<len(a):
#     k=a[i]*b
#     m.append(k)
#     i+=1
# print(m)    


           


# a=[2,3,4,5,6,10,12]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             t=a[j]
#             a[j]==a[j+1]
#             a[j+1]=t
#         j+=1
#     i+=1
# print(a)  
# 
# a=["priti","bulbul","patidar"]
# b=a[::-1]  
# # print(b) 
# i=0
# l=[]
# while i<len(b):
#     k=b[i][::-1]
#     l.append(k)

#     i+=1     
# print(l)



# i=1
# a=[]
# b=[]
# while i<=4:
#     name=input("enter the name:-")
#     room=int(input("enter the room number:-"))
#     a.append(name)
#     b.append(room)
#     print(name,"-",room)
#     i+=1
# print(a)
# print(b)    




# l=["bulbul",5,6,5.5,6.2,True,"sheetal"]
# n=eval(input("enter the :-"))
# i=0
# b=[]
# while i<len(l):
#     if type(l[i])==type(n):
#         b.append(l[i])
#     i+=1
# print(b)    
# 
# 
# l=[[2,1],2,3,[2,4],5,[2,7]]
# i=0
# b=[]
# while i<len(l):
#     if type(l[i])==list:
#         j=1
#         while j>=0:
#             b.append(l[i][1]) 
#             j=j-1
#     else:
#         b.append(l[i])
#     i+=1
# print(b)                  




