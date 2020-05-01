# Task 1 Calculator

def add(x,y):
	return(x+y)

def sub(x,y):
	return(x-y)

def multiply(x,y):
	return(x*y)

def divide(x,y):
	return(x/y)

print("Press 01 to Add\nPress 02 to Subtracte\nPress 03 to multiply\nPress 04 to divide")
choice = input("Enter Operation(1/2/3/4): ")
print(choice)
num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")

if choice == '1':
	result = add(num1,num2)
	print(result)
	conv = str(result)
	spl = conv.split(".")
	print(bin(spl[0]+"."+bin(x[1])))

elif choice == '2':
	result = sub(num1,num2)
	conv = str(result)
	spl = conv.split(".")
	print(bin(spl[0]+"."+bin(x[1])))

elif choice == '3':
	result = multiply(num1,num2)
	conv = str(result)
	spl = conv.split(".")
	print(bin(spl[0]+"."+bin(x[1])))

elif choice == '4':
	result = divide(num1,num2)
	conv = str(result)
	spl = conv.split(".")
	print(bin(spl[0]+"."+bin(x[1])))