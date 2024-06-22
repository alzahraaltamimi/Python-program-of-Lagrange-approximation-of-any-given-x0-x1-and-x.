import math

def f(x):
    return x**2 + 5*x - math.sqrt(abs(x))

def lagrange_approximation(x0, x1, x):
    # Check if x is between x0 and x1
    if x < min(x0, x1) or x > max(x0, x1):
        print("Error: x should be between x0 and x1.")
        return None

    # Calculate f0 and f1
    f0 = f(x0)
    f1 = f(x1)

    # Compute Lagrange interpolation
    L_x = ((x - x1) / (x0 - x1)) * f0 + ((x - x0) / (x1 - x0)) * f1

    # Construct Lagrange interpolation equation
    equation = f"L(x) = (({x} - {x1}) / ({x0} - {x1})) * f({x0}) + (({x} - {x0}) / ({x1} - {x0})) * f({x1})"

    return equation, L_x

# User input for x0, x1, and x
x0 = float(input("Enter the value of x0: "))
x1 = float(input("Enter the value of x1: "))
x = float(input("Enter the value of x for interpolation[Number should be between x0 and x1]: "))

# Calculate f0 and f1
f0 = f(x0)
f1 = f(x1)

print("\nWhen x0 =", x0, ", f0 =", f0)
print("When x1 =", x1, ", f1 =", f1)

# Compute Lagrange interpolation
equation, approximation = lagrange_approximation(x0, x1, x)

if equation is not None and approximation is not None:
    print("\nEquation L(x) where x=",x,":")
    print(equation)
    print("\nLagrange Approximation at x:")
    print(approximation)
