numbers = [1,2,3,4,5,6,7,8,9]
even = 0
odd =0
length = len(numbers)
for i in range (length):
    if numbers[i]%2 == 0:
        even+=1
    else:
        odd+=1
print("Number of even numbers: ",even)
print("Number of Odd numbers : ",odd)