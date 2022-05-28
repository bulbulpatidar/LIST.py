a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
i=0
b=[]
while i<len(a):
    if a[i]!=a[-1] and a[i]!=a[-2] and a[i]!=a[-3]:
        b.append(a[i])
    i+=1
print(b)


# a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=a[-1] and a[i]!=a[-2] and a[i]!=a[-3] and a[i]!=a[-4] and a[i]!=a[-5]:
#         b.append(a[i])
#     i+=1
# print(b)

