import string

def process_string(s, op):
    """
    Perform various string operations on the given string.

    Args:
        s (str): The input string.
        op (str): The operation to perform on the string.

    Returns:
        str: The result of the operation, or an error message if the operation is invalid.
    """
    operations = {
        'upper': str.upper,
        'lower': str.lower,
        'capitalize': str.capitalize,
        'reverse': lambda s: s[::-1],
        'count_vowels': lambda s: sum(c.lower() in string.vowels for c in s),
        'remove_spaces': lambda s: s.replace(' ', '')
    }

    if op in operations:
        return operations[op](s)
    else:
        return 'Error: invalid operation'

def format_name(first, middle=None, last=None, include_middle=True):
    """
    Format a name with various options.

    Args:
        first (str): The first name.
        middle (str, optional): The middle name or initial.
        last (str, optional): The last name.
        include_middle (bool, optional): Whether to include the middle name or initial.

    Returns:
        str: The formatted name, or an error message if the first or last name is missing.
    """
    if not first:
        return 'Error: first name required'
    if not last:
        return 'Error: last name required'

    name = f"{first} {last}"

    if include_middle and middle:
        name = f"{first} {middle} {last}"

    return name

# Example usage
print(process_string("Hello World", 'upper'))  # HELLO WORLD
print(process_string("Hello World", 'lower'))  # hello world
print(process_string("hello world", 'capitalize'))  # Hello world
print(process_string("Hello", 'reverse'))  # olleH
print(process_string("Hello World", 'count_vowels'))  # 3
print(process_string("Hello World", 'remove_spaces'))  # HelloWorld
print(process_string("Hello", 'invalid'))  # Error: invalid operation

print(format_name("John", "Michael", "Smith"))  # John Michael Smith
print(format_name("John", None, "Smith"))  # John Smith
print(format_name("John", "Michael", "Smith", include_middle=False))  # John Smith
print(format_name("", "Michael", "Smith"))  # Error: first name required
print(format_name("John", "Michael", ""))  # Error: last name required
def format_name(first_name, middle_name=None, last_name=None, use_middle_initial=True):
    """
    Format a person's name based on the provided first, middle, and last names.

    Args:
        first_name (str): The person's first name.
        middle_name (str, optional): The person's middle name. Defaults to None.
        last_name (str, optional): The person's last name. Defaults to None.
        use_middle_initial (bool, optional): Whether to use the middle initial or the full middle name. Defaults to True.

    Returns:
        str: The formatted name.

    Raises:
        ValueError: If the first name or last name is not provided.
    """
    if not first_name:
        raise ValueError("Error: first name required")
    if not last_name:
        raise ValueError("Error: last name required")

    formatted_name = first_name + " "

    if middle_name:
        if use_middle_initial:
            formatted_name += f"{middle_name[0]}. "
        else:
            formatted_name += f"{middle_name} "

    formatted_name += last_name

    return formatted_name


# Example usage
print(format_name("John", "Michael", "Smith"))  # John M. Smith
print(format_name("John", "Michael", "Smith", False))  # John Michael Smith
print(format_name("John", None, "Smith"))  # John Smith

# Handling errors
try:
    print(format_name(None, "Michael", "Smith"))
except ValueError as e:
    print(e)  # Error: first name required

try:
    print(format_name("John", "Michael", None))
except ValueError as e:
    print(e)  # Error: last name required