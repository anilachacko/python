class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)

a=int(input("length of rectangle1 : "))
b=int(input("breadth of rectangle1 : "))
c=int(input("length of rectangle2 : "))
d=int(input("breadth of rectangle2 : "))
rec1=rectangle(a,b)
rec2=rectangle(c,d)
print("\narea of rectangle1 : ",rec1.area())
print("\nperimeter of rectangle1 : ",rec1.perimeter())
print("\narea of rectangle2 : ",rec2.area())
print("\nperimeter of rectangle2 : ",rec2.perimeter())

if rec1.area()==rec2.area():
    print("\nThe two given rectangle have same area")
elif rec1.area() > rec2.area():
    print("\nrectangle1 is greater than rectangle2")
else:
    print("\nrectangle2 is greater than rectangle1")
