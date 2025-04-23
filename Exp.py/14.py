#Program 11: Division with Exception Handling

 
# Name: Alzaid khan  DIV: E(ECS)
# UIN: 241S009  Roll no. 09

def safe_division():
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except ValueError:
        print("Error: Invalid input!")

safe_division()
