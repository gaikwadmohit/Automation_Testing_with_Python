def func1(x1, x2, y1, y2):
    # For first line

    line1 = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    line1 = line1 ** 2
    print("Distance of the First line =  ", line1)
    return line1


def func2(x4, y4, x3, y3):
    # For second line

    line2 = ((x4 - x3) * (x4 - x3) + (y4 - y3) * (y4 - y3))
    line2 = line2 ** 2
    print("Distance of Second line =  ", line2)
    return line2


if __name__ == '__main__':
    print("Enter x1 & y1 values of First point")
    x1 = int(input("x1="))
    y1 = int(input("y1="))

    print("Enter x2 & y2 values of Second point")
    x2 = int(input("x2="))
    y2 = int(input("y2="))
    # func1()
    # func2()
    print("Enter x3 & y3 values of Third point")
    x3 = int(input("Enter x3  values of Third point"))
    y3 = int(input("Enter y3 values of Third point"))
    print("Enter x4 & y4 values of Fourth point")
    x4 = int(input("x4="))
    y4 = int(input("y4="))

    var = func1(x1, y1, y1, y2)
    var2 = func2(x4, y4, x3, y3)

    print("result = ", var == var2)
