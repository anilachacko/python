from Graphics.circle import *
from Graphics.rectangle import *
from Graphics.dgraphics.cuboid import *
from Graphics.dgraphics.sphere import *


print("\nCUBOID")

l=int(input("Enter length:"))
w=int(input("Enter width:"))
h=int(input("Enter height:"))
print("Area of cuboid",CUArea(l,w,h))
print("Perimeter of cuboid",CUPerimeter(l,w,h))

print("\nSPHERE")
r=int(input("Enter radius of sphere:"))
print("Area of sphere", Sarea(r))
print("Perimeter of sphere", Sperimeter(r))


