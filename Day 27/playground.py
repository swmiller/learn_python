def add(*args: int) -> int:
    """Accepts any number of integer arguments using *args and returns their sum."""
    return sum(args)


def add_kwargs(**kwargs: int) -> int:
    """Accepts any number of integer keyword arguments using **kwargs and returns their sum."""
    return sum(kwargs.values())


def func_name(**kwargs):
    # Check for required keys
    required_keys = {"one", "two"}
    missing_keys = required_keys - kwargs.keys()
    if missing_keys:
        raise ValueError(f"Missing required keyword(s): {', '.join(missing_keys)}")

    # Validate "one"
    one = kwargs["one"]
    if not isinstance(one, int):
        raise TypeError('"one" must be an integer.')
    if not (1 <= one <= 100):
        raise ValueError('"one" must be between 1 and 100 inclusive.')

    # Validate "two"
    two = kwargs["two"]
    if not isinstance(two, str):
        raise TypeError('"two" must be a string.')
    if two not in {"three", "four"}:
        raise ValueError('"two" must be either "three" or "four".')

    # If all validations pass
    print("All validations passed.")


# Any number of arguments
total_args = add(1, 2, 3, 4, 5)
print(total_args)

# Any number of keyword arguments
total_kwargs = add_kwargs(a=1, b=2, c=3, d=4, e=5)
print(total_kwargs)

try:
    # Example usage with missing required keys
    func_name(one=42)
except Exception as e:
    print(f"Error: {e}")

try:
    # Example usage with invalid type
    func_name(one="not an int", two="three")
except Exception as e:
    print(f"Error: {e}")

try:
    # Example usage with out-of-range value
    func_name(one=101, two="three")
except Exception as e:
    print(f"Error: {e}")

try:
    # Example usage with invalid value
    func_name(one=42, two="not three or four")
except Exception as e:
    print(f"Error: {e}")

try:
    # Example usage with all validations passed
    func_name(one=42, two="three")
except Exception as e:
    print(f"Error: {e}")