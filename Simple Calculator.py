num_1 = float(input("Enter the first number : "))
num_2 = float(input("Enter the second number : "))
oper = input("Enter the Operand : ")

if oper == '+' :
    result = num_1 + num_2 
    print("The Addition result is ", result) 
elif oper == '-' :
    result = num_1 - num_2 
    print("The Substraction result is ", result) 
elif oper == '*' :
    result = num_1 * num_2  
    print("The Multipilcation result is ", result)  
elif oper == '/' :
    result = num_1 / num_2    
    print("The Division result is ", result)  
elif oper == '**' :
    result = num_1 ** num_2
    print("The Exponential result is ", result) 
elif oper == '//' : 
    result = num_1 // num_2
    print("The Quotient is ", result) 
elif oper == '%' :
    result = num_1 % num_2
    print("The reminder is ", result)       

