l1 = [(2,5),(1,2),(4,4),(2,3),(2,1)]
#l1=[(2,34),(23,54),(1,2),(3,5),(6,10),(3,13),(7,1),(99,6)]

for i in range (len(l1)):
    for j in range(len(l1)):
        if j < len(l1)-1:
            if l1[j][1] > l1[j+1][1]:
                temp = l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp

print(l1)