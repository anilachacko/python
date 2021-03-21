list1 = list(input("Enter the 1st number"))
list2 = list(input("Enter the 2nd number"))

#a. checking length

if(len(list1)==len(list2)):
    print("Lists are of same length")
else:
    print("Lists are not of same length")
list1=set(list1)
list2=set(list2)

if (list1)==(list2):
    print("Lists are of same sum")
else:
    print("Lists are not of same sum")

#c. whether any value occur in both
a=list1.intersection(list2)
print("common ele:",a)
