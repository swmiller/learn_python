# Example 1: Built-in Namespace
# Python's built-in namespace contains functions like print, len, etc.
print("This is an example of the built-in namespace.")

# Example 2: Global Namespace
x = 10  # This variable is in the global namespace

def global_example():
    print(f"Accessing global variable x: {x}")

global_example()

# Example 3: Local Namespace
def local_example():
    y = 20  # This variable is in the local namespace of the function
    print(f"Accessing local variable y: {y}")

local_example()

# Example 4: Enclosing Namespace
def outer_function():
    z = 30  # This variable is in the enclosing namespace

    def inner_function():
        print(f"Accessing enclosing variable z: {z}")

    inner_function()

outer_function()

# Example 5: Variable Shadowing
a = 50  # Global variable

def shadowing_example():
    a = 100  # Local variable with the same name as the global variable
    print(f"Local variable a: {a}")

shadowing_example()
print(f"Global variable a: {a}")

# Example 6: Using the 'global' Keyword
b = 5

def modify_global():
    global b
    b = 15  # Modifies the global variable
    print(f"Modified global variable b: {b}")

modify_global()
print(f"Global variable b after modification: {b}")

# Example 7: Using the 'nonlocal' Keyword
def enclosing_function():
    c = 25

    def modify_nonlocal():
        nonlocal c
        c = 35  # Modifies the enclosing variable
        print(f"Modified enclosing variable c: {c}")

    modify_nonlocal()
    print(f"Enclosing variable c after modification: {c}")

enclosing_function()