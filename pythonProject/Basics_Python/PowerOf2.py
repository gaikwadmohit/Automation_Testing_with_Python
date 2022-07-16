i = 1
power = int(input("enter to find power of 2 less than 32"))
for i in range(1, power):
	print("power of 2 is : ", i, " is ", 2 ** i)
print("---------------")
while power > 31:
	print("invalid input ")
	print("enter value less than 32")
	break
