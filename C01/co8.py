sr= input("Enter the string : ")
first_char = sr[0]
sr = sr.replace(first_char,"$")
sr = first_char+sr[1:]
print(sr)
