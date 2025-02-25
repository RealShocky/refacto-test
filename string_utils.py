import string

def process_string(s, op):
    """
    Performs various string operations on the input string 's' based on the operation 'op'.

    Args:
        s (str): The input string to be processed.
        op (str): The operation to be performed on the string.

    Returns:
        str: The processed string or an error message if the operation is invalid.
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
    Formats a name based on the provided first, middle, and last names.

    Args:
        first (str): The first name.
        middle (str, optional): The middle name. Defaults to None.
        last (str, optional): The last name. Defaults to None.
        include_middle (bool, optional): Whether to include the middle name in the formatted name. Defaults to True.

    Returns:
        str: The formatted name or an error message if the first or last name is missing.
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
    Format a person's name based on the provided parameters.

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
print(format_name("John", None, "Smith"))  # John Smith
try:
    print(format_name(None, "Michael", "Smith"))  # Error: first name required
except ValueError as e:
    print(e)
try:
    print(format_name("John", "Michael", None))  # Error: last name required
except ValueError as e:
    print(e)