areaSquare=lambda length : length * length

areaRect=lambda length,width : length * width

l=int(input("Enter Length Value to calcualte area of Square: "))

print("Area of Square:",areaSquare(l))

l=int(input("\n Enter Length Value to calcualte area of Rectangle:"))

w=int(input("Enter Width Value to calcualte area of Rectangle: "))

print("Area of Rectangle:",areaRect(l,w))

