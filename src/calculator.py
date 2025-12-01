def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x,y,z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    """
    total_sum = x + y + z
    return total_sum

def fun5(x, y):
    """Division of two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def fun6(x, y):
    """Power operation: x raised to power y."""
    return x ** y

def fun7(x):
    """Square root of a number."""
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return x ** 0.5

def fun8(x, y):
    """Modulo operation: remainder of x divided by y."""
    if y == 0:
        raise ValueError("Cannot perform modulo with zero divisor")
    return x % y


f1_op = fun1(2, 3)
f2_op = fun2(2, 3)
f3_op = fun3(2, 3)
f4_op = fun4(f1_op, f2_op, f3_op)

print(f"fun1(2, 3) = {f1_op}")
print(f"fun2(2, 3) = {f2_op}")
print(f"fun3(2, 3) = {f3_op}")
print(f"fun4({f1_op}, {f2_op}, {f3_op}) = {f4_op}")

# Test new advanced functions
print("\n--- Advanced Functions ---")
print(f"fun5(10, 2) [Division] = {fun5(10, 2)}")
print(f"fun6(2, 3) [Power] = {fun6(2, 3)}")
print(f"fun7(16) [Square Root] = {fun7(16)}")
print(f"fun8(10, 3) [Modulo] = {fun8(10, 3)}")

