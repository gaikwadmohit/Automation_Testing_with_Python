num=int(input("Enter Any Number :"))
condition=False
if num>1:
    for i in range(2,num):
        if num%i==0:
            condition=True

if condition:
    print(num ,": is not prime number")
else:
    print(num ,"is a prime number")

