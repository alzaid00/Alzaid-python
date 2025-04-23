#Program 8: Factorial of a Number

# Name: Alzaid khan  DIV: E(ECS)
# UIN: 241S009  Roll no. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

