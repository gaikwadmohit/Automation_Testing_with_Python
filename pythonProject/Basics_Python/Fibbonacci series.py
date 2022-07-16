def fibbonacci(num):
    num1=5
    num2=6
    series=0
    for i in range(num):
        print(series, end=' ')
        num1=num2
        num2=series
        series=num1+num2
num=int(input("Enter how many num needed in fibonacci series"))
fibbonacci(num)

