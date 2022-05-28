#16
# s=[]
# i=1
# while i<=30:
#     s.append(i**2)
#     i+=1
# print(s) 
# print(s[:5])
# print(s[-5:])   


# 18
# list1=[5,6,7,8,9,10]
# count = 0
# for i in list1:
#    print(count,i)
#    count +=1

# 22
# s = ['a', 'b', 'c', 'd']
# str1 = ''.join(s)
# print(str1)

# s=["p","y","t","h","o","n"]
# i=0
# sum=""
# while i<len(s):
#     sum+=s[i]
#     i+=1
# print(sum)  
# 
# 23
# num =[10, 30, 4, -6]
# print(num.index(30))

# 24
# l1 = [[2,4,3],[1,5,6], [9], [7,9,0]]
# al=[]
# for x in l1:
#    al.extend(x)
# print(al)


# a=[2,3,45]
# b=["red","orange"]
# a.extend(b)
# print(a)

# import random

# list = ['1', '2', '3', '4', 'Red','Orange','Mango']

# print(random.choice(list))


# list1 = [10, 10, 0, 0, 10]
# list1.sort()
# list2 = [10, 10, 10, 0, 0]
# list2.sort()
# if list1==list2:
#      print('Identical')
# else:
#      print("not identical")


# a=[10,20,30,40,40,40,70,80,99]
# count=0
# for i in a:
#     if i>=40 and i<=100:
#        count+=1
# print(count)



# lst = ['X','Y','Z']
# lst1= [[]]
# for x in range(len(lst)):
#    count = x+1
# for y in range(count,len(lst)+1):
#    sub = lst[x:y]
# lst1.append(sub)
# count+=1
# print(lst1)
# print(lst[x:y])


# a = [1,2,3]
# c = 1
# for i in a:
#    c = i*c
#    i+=1
# print(c)


# a=['p', 'q']
# n=int(input("enter: "))
# b=[]
# for i in range(1,n+1):
#     for j in a:
#        b.append(j+str(i))
# print(b)

# list1 = [1,2,3,134,4,5,9]
# list2 = [2,5,7,134]
# m=[]
# for i in list1:
#     for j in list2:
#          if i==j:
#             m.append(i)
# print(m)            

# list = [11, 33, 50]
# join = ''
# for i in list:
#      join+=str(i)
# print(join)

# a=['be','have','do','say','get','make','go','know','take','see','come','think',
# 'look','want','give','use','find','tell','ask','work','seem','feel','leave','call','abc','ab']
# n=input("enter: ")
# b=[]
# count=0
# for i in a:
#    if i[0]==n:
#       b.append(i)

# print(b)


# list1=[]
# for i in range(1,11):
#    list1.append(list())
# print(list1)


# list1 = ['a','b','c','d','e','f']
# list2 = ['d','e','f','g','h']

# for x in list1:
#    if x not in list2:
#      print('missing value from list2 ',x)
# for y in list2:
#    if y not in list1:
#       print('Additional value from list2 ',y)

# color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
# ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]

# for i in color:
#     print(i)


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# b=[]
# c=[]
# d=[]
# for i in a:
#    if i<=5:
#       b.append(i)
#    elif i>=5 and i<=10:
#       c.append(i)
#    else:
#       d.append(i)
# e=b,c,d
# print(list(e))



# L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
# (7, 8), (9, 10)]
# p = []
# s = []
# for i in L:
#    s.extend(i[:])
#    s.sort()
# print(set(s))


# a= ['Red', 'Green', 'Black']

# c=[]
# for i in a:
#     for j in ("c",i):

#         c.append(j)

# print(c)


# a= [['Red'], ['Green'], ['Black']]
# for i in a:
#     print(i)



# color = ["Black", "Red", "Maroon", "Yellow"]
# code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# mylist = [{"color_name":color[i],"color_code":code[i]} for i in range(len(color))]
# print(mylist)

# i=0
# b=[]
# while i<=4:
#     j=0
#     s=[]
#     while j<2:
#         s.append(0)
#         j+=1
#     i+=1    
#     b.append(s) 
# print(b)       

# a=[1,3,5,8,9,10]
# i=0
# b=[]
# j=i+1
# while i<len(a) and j<len(a):
#     d=a[j]-a[i]
#     b.append(d)
#     j+=1
#     i+=1
# print(b)    




# l1 = ["red", "orange", "green", "blue", "white"]
# l2 = ["black", "yellow", "green", "blue"]
# nl = []
# for x in l1 :
#    if x not in l2 :
#      nl.append(x)
# print(nl)

# nl2 = []
# for x in l2 :
#     if x not in l1 :
#       nl2.append(x)
# print(nl2)


# color = ['red', 'green', 'orange']
# print('-'.join(color))
# print(''.join(color))

# lis1=[1, 3, 5, 7, 9, 10]
# lis2=[2, 4, 6, 8]
# print(lis1.pop())
# print(lis1)
# print(lis1+lis2)


# num1 = [1, 3, 5, 7, 9, 10]
# num2 = [2, 4, 6, 8]
# num1.pop()
# print(num1)
# num1.extend(num2)
# print(num1)

# l=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# print(max(l))


# # [10, 20, 30]
# # [40, 50, 60]
# # Expected output : [40, 50, 60, 10, 20, 30]
# a=[10, 20, 30]
# b=[40, 50, 60]
# b.extend(a)
# print(b)


# 69. Write a Python program to remove duplicates from a list of lists. Go to the editor
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

# a=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# i=0
# n=[]
# while i<len(a):
#     if a[i] not in n:
#         n.append(a[i])
#     i+=1
# print(n)        

# 70. Write a Python program to find the items starts with specific character from a given list. Go to the editor
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:
# []
# n=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# b=input("enter the charater:-")
# i=0
# l=[]
# while i<len(n):
#     j=0
#     while j<1:
#         if n[i][j]==b:
#             l.append(n[i])
#         j+=1 
#     i+=1       
# print(l)        


# 1. Write a Python program to check whether all dictionaries in a list are empty or not. Go to the editor
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
# l= [{},{},{},{5,6}]
# i=0
# c=0
# while i<len(l):
#     if l[i]=={}:
#         c+=1
#     i+=1
# if c==len(l):
#     print("true") 
# else:
#     print("false")  
# 
# 72. Write a Python program to flatten a given nested list structure. Go to the editor
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]         

# l=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# i=0
# k=[]
# while i<len(l):
#     if type(l[i])==list:
#         j=0
#         while j<len(l[i]):
#             k.append(l[i][j])
#             j+=1
#     else:
#         k.append(l[i])   
#     i+=1     
# print(k)        

# 73. Write a Python program to remove consecutive duplicates of a given list. Go to the editor
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# l=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# i=0
# m=[]
# while i<len(l):
#     if l[i] not in m:
#         m.append(l[i])
#     i+=1
# print(m)   
# 
# 
# 
# a=[1,1,2,3,4,4,5,1]
# k=int(input("enter the number:-"))
# a.remove(k)
# print(a)

# 80. Write a Python program to insert an element at a specified position into a given list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]


# l=[1, 1, 2, 3, 4, 4, 5, 1]
# n=int(input("enter the index number:-"))
# k=int(input("insert the number"))
# # l.insert(n,k)  
# # print(l)   
# i=0
# c=[]
# while i<len(l):
#     if i==n:
#         c.append(k)
#     c.append(l[i])
#     i+=1
# print(c)    
# 
# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. Go to the editor
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
# Click me to see the sample solution    


# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# i=0
# k=[]
# while i<len(l):
#     j=i+1
#     m=[]
#     while j<len(l):
#         z=[l[i],l[j]]
#         m.append(z)
#         j+=1
#     i+=1    
#     k.extend(m)
# print(k)    

# . Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list. Go to the editor
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result:
# 243

# a=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# i=0
# sum=1
# while i<len(a):
#     sum+=a[i]
#     i+=1
# print(int(sum)*len(a))    

# 84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space. Go to the editor
# Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# Minimum value: 4
# Maximum value: 22
# Result:
# 20 25 45 55 60 70 80 90 110
# l=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# i=0
# c=[]
# d=[]
# while i<len(l):
#     b=int(l[i])
#     c.append(b)
#     d.append(b*5)
#     i+=1
# print(d)
# c.sort()
# print(c)
# i=0
# max=0
# min=c[i]
# while i<len(c):
#     if c[i]>max:
#         max=c[i]
#     if c[i]<min:
#         min=c[i]
#     i+=1
# print(max)
# print(min)            

# 85. Write a Python program to create a multidimensional list (lists of lists) with zeros. Go to the editor
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]
# i=0
# l=[]
# while i<3:
#     j=0
#     c=[]
#     while j<2:
#         c.append(0)
#         j+=1
#     l.append(c)
#     i+=1
# print(l) 
# 
# 
# 86. Write a Python program to create a 3X3 grid with numbers. Go to the editor
# 3X3 grid with numbers:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]  
# 
# i=0
# l=[]
# while i<3:
#     j=1
#     m=[]
#     while j<=3:
#         m.append(j)
#         j+=1
#     l.append(m)
#     i+=1
# print(l)
# 
 
# 89. Write a Python program to Zip two given lists of lists. Go to the editor
# Original lists:
# [[1, 3], [5, 7], [9, 11]]
# [[2, 4], [6, 8], [10, 12, 14]]
# Zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
# l1=[[1, 3], [5, 7], [9, 11]]
# l2=[[2, 4], [6, 8], [10, 12, 14]]
# i=0
# while i<len(l1):
#     l1[i].extend(l2[i])
#     i+=1
# print(l1)    

# 88. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user. Go to the editor
# Input the size of the matrix: 3
# 2 3 4
# 4 5 6
# 3 4 7
# Sum of matrix primary diagonal:
# 14
# l=[[2,3,4],
# [4,5,6],
# [3,4,7]]
# i=0
# sum=0
# while i<len(l):
#     j=i 
#     while j<=i:
#         sum=sum+l[i][j]
#         j+=1
#     i+=1
# print(sum) 
# 
# 90. Write a Python program to count number of lists in a given list of lists. Go to the editor
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# Number of lists in said list of lists:
# 4
# Original list:
# [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# Number of lists in said list of lists:
# 3     
# l=[[1, 3], [5, 7], [9, 11], [13, 15, 17]] 
# l=[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]] 
# c=0
# while c<len(l):
#     c+=1
# print(c)    

# 92. Write a Python program to check if a nested list is a subset of another nested list. Go to the editor
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# [[1, 3], [13, 15, 17]]
# If the one of the said list is a subset of another.:
# True
# l=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# l1=[[1,3]]
# c=0
# for i in l:
#     for j in l1:
#         if i==j:
#             c+=1
# if c>=1:
#     print("true")
# else:
#     print("false")   
# 
# 93. Write a Python program to count the number of sublists contain a particular element. Go to the editor
# Original list:
# [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3  
# l=[[1, 3], [5, 7], [1, 11], [1, 15, 7]] 
# n=int(input("enter number:-"))
# i=0
# c=0
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         if l[i][j]==n:
#             c+=1
#         j+=1
#     i+=1
# print(c)             

# 95. Write a Python program to sort each sublist of strings in a given list of lists. Go to the editor
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# # Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
# a=[[2],  [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if len(a[j])>len(a[j+1]):
#             t=len(a[j])
#             len(a[j])==len(a[j+1])
#             len(a[j+1])==t
#         j+=1
#     i+=1        
# print("sorted list:-")
# print(a)  
# 
# 
  
# 97. Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range. Go to the editor
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contains an element outside the given range:
[[13, 14, 15, 17]]
# a=[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# for i in a:
#     if i[0]>=13 and i[-1]<=20:
#         print(i)  

# 99. Write a Python program to find the maximum and minimum values in a given heterogeneous list. Go to the editor
# Original list:
# ['Python', 3, 2, 4, 5, 'version']
# Maximum and Minimum values in the said list:
# (5, 2)

# 100. Write a Python program to extract common index elements from more than one given list. Go to the editor
# Original lists:
# [1, 1, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]
# a=[1, 1, 3, 4, 5, 6, 7]
# b=[0, 1, 2, 3, 4, 5, 7]
# c=[0, 1, 2, 3, 4, 5, 7]
# i=0
# l=[]
# while i<len(a):
#     if a[i]==b[i]==c[i]:
#         l.append(a[i])
#     i+=1
# print(l)        


# 101. Write a Python program to sort a given matrix in ascending order according to the sum of its rows. Go to the editor
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# l.sort()
# print(l)

# 102. Write a Python program to extract specified size of strings from a give list of string values. Go to the editor
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']
# l=['Python', 'list', 'exercises', 'practice', 'solution']
# n=int(input("enter the lenth:-"))
# i=0
# c=[]
# while i<len(l):
#     if len(l[i])==n:
#         c.append(l[i])
#     i+=1
# print(c)        

# 106. Write a Python program to count integer in a given mixed list. Go to the editor
# Original list:
# [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list:
# 6
# l=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# i=0
# c=0
# while i<len(l):
#     if type(l[i])==int:
#         c+=1
#     i+=1
# print(c)        


# 108. Write a Python program to extract a specified column from a given nested list. Go to the editor
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column:
# [1, 2, 1]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column:
# [3, -5, 1]
# a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# n=int(input("enter the number:-"))
# i=0
# m=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if j==n:
#             m.append(a[i][j])
#         j+=1
#     i+=1
# print(m)    
# 

# 110. Write a Python program to find the item with maximum occurrences in a given list. Go to the editor
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Item with maximum occurrences of the said list:
# 2        
# t1 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# l = len(t1)
# c = 0
# n = int(input("Enter the occ_numbre: "))
# for i in range(l):
#     if t1[i] == n :
#         c += 1
# print(c)
