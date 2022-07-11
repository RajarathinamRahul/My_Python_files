num_1 = int(input("Enter a number :"))
flag = False

if num_1 > 1:
    for i in range(2, num_1) :
        #result = num_1 % i
        if (num_1 % i) == 0 :
           # print(num_1,"is not a prime number.")
            flag = True
            break
#else :
   # print(num_1,"is not a prime number.")   

if flag:
    print( num_1,"is not a prime number") 
elif (num_1 == 2):
    print("2 is a prime number")
else :
    print( num_1,"is a prime number")
