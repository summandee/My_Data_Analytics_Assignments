##  Q3. Write a program to explore below variables

## a) Print their memory address (to check if python assigns same address of different variables having same element)
## b) Find memory size and append them in a list, use this list to find data type having least memory size
## c) Print final name of data type which has lowest memory
##  Result will help a programmer to decide which variable is storing less memory and variable locations


## a) Print their memory address (to check if python assigns same address of different variables having same element)
# Variables with the same value
a = 100
b = 100
c = "hello"
d = "hello"

# Print memory addresses
print(f"Memory address of a (100): {id(a)}")
print(f"Memory address of b (100): {id(b)}")
print(f"Memory address of c ('hello'): {id(c)}")
print(f"Memory address of d ('hello'): {id(d)}")

#extra variables to explore different values
e = 200
f = 200

print(f"Memory address of e (200): {id(e)}")
print(f"Memory address of f (200): {id(f)}")


# ****************************************************
## b) Find memory size and append them in a list, use this list to find data type having least memory size
## c) Print final name of data type which has lowest memory
import sys
# Define various variables of different data types
variables = [
    100,                            # Integer
    3.14,                           # Float
    "hello",                        # String
    [1, 2, 3],                     # List
    (1, 2, 3),                     # Tuple
    {"key": "value"},              # Dictionary
    True,                           # Boolean
    None                            # NoneType
]

# List to store memory sizes
memory_sizes = []

# Calculate memory size for each variable and store it in the list
for variable in variables:
    size = sys.getsizeof(variable)
    memory_sizes.append(size)
    print(f"Variable: {variable}, Type: {type(variable).__name__}, Size: {size} bytes")

# Find the data type with the least memory size
min_size_index = memory_sizes.index(min(memory_sizes))
least_memory_variable = variables[min_size_index]
least_memory_size = memory_sizes[min_size_index]

print(f"\nVariable with least memory size: {least_memory_variable} ({type(least_memory_variable).__name__})")
print(f"Memory size: {least_memory_size} bytes")
## Output:
# Variable: 100, Type: int, Size: 28 bytes
# Variable: 3.14, Type: float, Size: 24 bytes
# Variable: hello, Type: str, Size: 54 bytes
# Variable: [1, 2, 3], Type: list, Size: 64 bytes
# Variable: (1, 2, 3), Type: tuple, Size: 56 bytes
# Variable: {'key': 'value'}, Type: dict, Size: 64 bytes
# Variable: True, Type: bool, Size: 28 bytes
# Variable: None, Type: NoneType, Size: 16 bytes

# Variable with least memory size: None (<class 'NoneType'>)
# Memory size: 16 bytes