
#  Program 10: Simple Calculator Using Functions
 
# Name: Alzaid khan  DIV: E(ECS)
# UIN: 241S009  Roll no. 09

def addition():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Addition of {num1} + {num2} = {num1+num2}")

def subtraction():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Subtraction of {num1} - {num2} = {num1-num2}")

def multiplication():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Multiplication of {num1} x {num2} = {num1*num2}")

def division():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 == 0:
        print("Division not possible")
    else:
        print(f"Addition of {num1}/{num2} = {num1/num2}")

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multpy")
print("4.Divide")

choice = int(input("Enter choice 1/2/3/4: "))

if choice == 1:
    addition()
elif choice == 2:
    subtraction()
elif choice == 3:
    multiplication()
elif choice == 4:
    division()
else:
    print("Invalid input!")
