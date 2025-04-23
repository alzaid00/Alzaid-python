#Program 2: Gross Salary Calculation
def gross_salary():
    bs = float(input("Enter Basic Salary: "))
    da = 0.7 * bs
    ta = 0.3 * bs
    hra = 0.1 * bs
    gross = bs + da + ta + hra
    print(f"Gross Salary: {gross}")

gross_salary()
