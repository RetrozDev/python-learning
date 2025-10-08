# c: Arithmetic and Logical Operators

# --- Arithmetic Operators ---
a: int = 10
b: int = 3

add = a + b       # Addition -> 13
sub = a - b       # Subtraction -> 7
mul = a * b       # Multiplication -> 30
div = a / b       # Division -> 3.333...
floordiv = a // b # Floor division (integer result) -> 3
mod = a % b       # Modulus (remainder) -> 1
power = a ** b    # Exponentiation -> 10³ = 1000

# --- Comparison Operators ---
equal = (a == b)      # Equal -> False
not_equal = (a != b)  # Not equal -> True
greater = (a > b)     # Greater than -> True
less = (a < b)        # Less than -> False
greater_eq = (a >= b) # Greater or equal -> True
less_eq = (a <= b)    # Less or equal -> False

# --- Logical Operators ---
x: bool = True
y: bool = False

and_op = x and y   # True if both are True -> False
or_op = x or y     # True if at least one is True -> True
not_op = not x     # Inverts the value -> False
