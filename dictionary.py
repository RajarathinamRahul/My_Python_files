d = {}

for i in range(97,123):
    #d.update({chr(i):i}) #updates dictionary with correspoding character and its ASCII value.
    d[chr(i)]=i   #both line 4 & 5 returns same 
print(d)
