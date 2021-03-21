def AreaOfRectangle(l, b):
    Area = l * b

    print(" Area of a Rectangle is:" ,Area)
def PerimeterofRect(l,b):
    Peri= 2*(l+b)
    print("Perimeter of Rectangle", Peri)
print("\nRECTANGLE")    
l= int(input('Enter the length of a Rectangle: '))
b = int(input('Enter the breadth of a Rectangle: '))

AreaOfRectangle(l, b)
PerimeterofRect(l,b)
