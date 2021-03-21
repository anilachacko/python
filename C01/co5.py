list=[]
n=int(input("Enter the limit"))
print("Enter", n, "number")
for i in range(n):
    a=int(input())
    list.append(a)
    
for i in range(0,len(list)):
    if(list[i]>100):
        list[i]="over"
print(list)
