w = input("Type your word : ")
temp1 = w[0]
temp2 = w[-1]
length = len(w)
result = w[-1]+w[1:length-1]+w[0]
print(result)
