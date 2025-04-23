# Program 9: Prime Number Check Using Function


# Name: Alzaid khan  DIV: E(ECS)
# UIN: 241S009  Roll no. 09


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number: "))

# Check and display result
if is_prime(num):
    print(num, "is a Prime Number.")
else:
    print(num, "is Not a Prime Number.")
