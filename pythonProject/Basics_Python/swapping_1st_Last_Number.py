num=[10,20,30,40,42]
def swap(num):
    num[0],num[-1]=num[-1],num[0]
    return num
print(swap(num))