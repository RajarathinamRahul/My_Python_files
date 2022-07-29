word = input("Enter the word: ")
#print(n[::-1])
length = len(word)
for i in range(length):
    ind = (length - 1)-i
    print(word[ind], end='')
