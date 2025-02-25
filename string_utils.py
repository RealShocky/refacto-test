import re

def process_string(string, operation):
    """
    Perform various string operations.

    Args:
        string (str): The input string.
        operation (str): The operation to perform on the string.

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
        'count_vowels': lambda s: len(re.sub(r'[^aeiou]', '', s, flags=re.IGNORECASE)),
        'remove_spaces': lambda s: s.replace(' ', '')
    }

    try:
        operation_func = operations[operation]
    except KeyError:
        raise ValueError(f"Error: invalid operation '{operation}'")

    return operation_func(string)

def format_name(first_name, middle_name=None, last_name=None, include_middle=True):
    """
    Format a name with various options.

    Args:
        first_name (str): The first name.
        middle_name (str, optional): The middle name.
        last_name (str, optional): The last name.
        include_middle (bool, optional): Whether to include the middle name.

    Returns:
        str: The formatted name.

    Raises:
        ValueError: If the first or last name is missing.
    """
    if not first_name:
        raise ValueError("Error: first name required")
    if not last_name:
        raise ValueError("Error: last name required")

    name_parts = [first_name, last_name]
    if include_middle and middle_name:
        name_parts.insert(1, middle_name)

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
print(format_name("John", None, "Smith"))  # John Smith
print(format_name("John", "Michael", "Smith", include_middle=False))  # John Smith
try:
    print(format_name("", "Michael", "Smith"))
except ValueError as e:
    print(e)  # Error: first name required
try:
    print(format_name("John", "Michael", ""))
except ValueError as e:
    print(e)  # Error: last name required
import re


def format_name(first_name, middle_name=None, last_name=None, use_middle_initial=True):
    """
    Format a person's name based on the provided first, middle, and last names.

    Args:
        first_name (str): The person's first name.
        middle_name (str, optional): The person's middle name. Defaults to None.
        last_name (str, optional): The person's last name. Defaults to None.
        use_middle_initial (bool, optional): Whether to use the middle initial or full middle name. Defaults to True.

    Returns:
        str: The formatted name.

    Raises:
        ValueError: If the first_name or last_name is None or an empty string.
    """
    if not first_name or not first_name.strip():
        raise ValueError("First name is required.")
    if not last_name or not last_name.strip():
        raise ValueError("Last name is required.")

    first_name = first_name.strip().title()
    last_name = last_name.strip().title()

    if middle_name:
        middle_name = middle_name.strip().title()
        if use_middle_initial:
            middle_initial = re.sub(r'[^a-zA-Z]', '', middle_name)[0] + '.'
            formatted_name = f"{first_name} {middle_initial} {last_name}"
        else:
            formatted_name = f"{first_name} {middle_name} {last_name}"
    else:
        formatted_name = f"{first_name} {last_name}"

    return formatted_name


# Example usage
print(format_name("John", "Michael", "Smith"))  # John M. Smith
print(format_name("John", "Michael", "Smith", False))  # John Michael Smith
print(format_name("John", None, "Smith"))  # John Smith

try:
    print(format_name(None, "Michael", "Smith"))
except ValueError as e:
    print(f"Error: {e}")

try:
    print(format_name("John", "Michael", None))
except ValueError as e:
    print(f"Error: {e}")