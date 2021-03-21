PI=3.14
def findArea(r): 
    return PI * (r*r)
def perimeter(r):
    return 2*PI*r
print("\nCIRCLE")  
num=int(input("Enter radius of circle:"))
print("Area of circle" , findArea(num))
print("Perimeter of circle" ,perimeter(num))

 
