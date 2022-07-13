num_1 = float(input("Enter the first number : "))
num_2 = float(input("Enter the second number : "))
num_3 = float(input("Enter the third number : "))

if (num_1 > num_2 and num_1 > num_3) :
    print("The Largest number is", num_1)
elif (num_2 > num_1 and num_2 > num_3) :
    print("The Largest number is", num_2)
elif (num_3 > num_1 and num_3 > num_2) :
    print("The Largest number is", num_3)
else:
    print("Enter a valid number.")