import string

def process_string(s, op):
    """
    Perform various string operations on the input string.

    Args:
        s (str): The input string.
        op (str): The operation to perform on the string.

    Returns:
        str: The result of the operation.

    Raises:
        ValueError: If the operation is invalid.
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
        raise ValueError(f"Error: invalid operation '{op}'")

def format_name(first, middle=None, last=None, include_middle=True):
    """
    Format a name with various options.

    Args:
        first (str): The first name.
        middle (str, optional): The middle name or initial.
        last (str, optional): The last name.
        include_middle (bool, optional): Whether to include the middle name/initial.

    Returns:
        str: The formatted name.

    Raises:
        ValueError: If the first or last name is missing.
    """
    if not first:
        raise ValueError("Error: first name required")
    if not last:
        raise ValueError("Error: last name required")

    name_parts = [first, last]
    if include_middle and middle:
        name_parts.insert(1, middle)

    return ' '.join(name_parts)

# Example usage
print(process_string("Hello World", 'upper'))  # HELLO WORLD
print(process_string("Hello World", 'lower'))  # hello world
print(process_string("hello world", 'capitalize'))  # Hello world
print(process_string("Hello", 'reverse'))  # olleH
print(process_string("Hello World", 'count_vowels'))  # 3
print(process_string("Hello World", 'remove_spaces'))  # HelloWorld
try:
    print(process_string("Hello", 'invalid'))
except ValueError as e:
    print(e)  # Error: invalid operation 'invalid'

print(format_name("John", "Michael", "Smith"))  # John Michael Smith
print(format_name("John", None, "Smith", include_middle=False))  # John Smith
try:
    print(format_name("", "Michael", "Smith"))
except ValueError as e:
    print(e)  # Error: first name required
try:
    print(format_name("John", "Michael", ""))
except ValueError as e:
    print(e)  # Error: last name required
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
        ValueError: If the first_name or last_name is not provided.
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
try:
    print(format_name(None, "Michael", "Smith"))  # Error: first name required
except ValueError as e:
    print(e)
try:
    print(format_name("John", "Michael", None))  # Error: last name required
except ValueError as e:
    print(e)