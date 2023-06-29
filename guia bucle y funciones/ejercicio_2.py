a=[]
b=[]
c=int(456)

for i in range(500,810,10):
    a.append(i)
    if i<800:
        b.append(c)
        c=c-2
print(a)
print(b)
print(sum(a))
print(sum(b))
print(sum(a)+sum(b))