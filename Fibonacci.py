n=50
a,b=1,1
count = 0
while count<=n:
    if a <= n:
        print(a, end=' ')
    temp = a + b
    a=b
    b=temp
    count+=1
