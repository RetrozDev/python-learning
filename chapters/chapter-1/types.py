
# a: Variable types

# Text Type
username: str = "Retroz"  # string of characters

# Numeric Types
age: int = 22  # integer number
weight: float = 91.1  # floating-point number
z_number: complex = 3 + 4j  # complex number (real + imaginary part)

# Sequence Types
fruits: list = ["apple", "banana", "cherry"]  # ordered, changeable collection
coordinates: tuple = (10.5, 20.3) # ordered, unchangeable collection
numbers: range = range(1, 6)  # sequence of numbers from 1 to 5

# Mapping Type
user: dict = {"username": username, "age": age, "weight": weight}  # key-value pairs

# Set Types
unique_numbers: set = {1, 2, 3, 3}  # unordered collection of unique items
frozen_numbers: frozenset = frozenset({1, 2, 3})  # immutable set

# Boolean Type
is_active: bool = True  # true or false value

# Binary Types
data_bytes: bytes = b"Hello"  # immutable bytes sequence
data_bytearray: bytearray = bytearray(5)  # mutable bytes sequence
data_memoryview: memoryview = memoryview(b"Hello")  # memory view of bytes

# None Type
nothing: None = None  # represents the absence of a value
