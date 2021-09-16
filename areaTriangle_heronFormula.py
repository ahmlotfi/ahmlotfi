import math
a = int(input("Enter the value of side a: "))
b = int(input("Enter the value of side b: "))
c = int(input("Enter the value of side c: "))
semiPerimeter = (a+b+c) / 2
area = math.sqrt(semiPerimeter * (semiPerimeter - a) * (semiPerimeter - b) * (semiPerimeter - c))
print("The area of your triangle is ", area)
