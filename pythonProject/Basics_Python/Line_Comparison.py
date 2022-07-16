

# For first  line
print("Enter x1 & y1 values of First point")
x1 = int(input())
y1 = int(input())

print("Enter x2 & y2 values of Second point")
x2 = int(input())
y2 = int(input())

line1 = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
line1=line1**2
print("Distance of the First line = ", line1)
