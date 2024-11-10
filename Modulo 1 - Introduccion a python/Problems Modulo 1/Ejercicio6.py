lista = [1,2,3,4,5,6,7,8,9,10]

c=1
i=1
while i<11:
    if c>10:
        break
    else:
        print(c*i)
    if(i==10):
        i=1
        c+=1
    else:
        i+=1
    