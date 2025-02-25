import re

def process_string(input_string, operation):
    """
    Perform various string operations.

    Args:
        input_string (str): The input string.
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
    except KeyError as e:
        raise ValueError(f"Error: invalid operation '{operation}'") from e

    return operation_func(input_string)

def format_name(first_name, last_name, middle_name=None, include_middle=True):
    """
    Format a name with various options.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.
        middle_name (str, optional): The middle name.
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
import re

def format_name(first_name, middle_name=None, last_name=None, include_middle=True):
    """
    Format a person's name based on the provided first, middle, and last names.

    Args:
        first_name (str): The person's first name.
        middle_name (str, optional): The person's middle name. Defaults to None.
        last_name (str, optional): The person's last name. Defaults to None.
        include_middle (bool, optional): Whether to include the middle name or initial. Defaults to True.

    Returns:
        str: The formatted name.

    Raises:
        ValueError: If the first_name or last_name is empty or None.
    """
    first_name = first_name.strip()
    last_name = last_name.strip()

    if not first_name:
        raise ValueError("Error: first name required")
    if not last_name:
        raise ValueError("Error: last name required")

    first_name = first_name.title()
    last_name = last_name.title()

    if middle_name:
        middle_name = middle_name.strip().title()
        if include_middle:
            middle_initial = re.sub(r'[^a-zA-Z]', '', middle_name)[0] + '.'
            return f"{first_name} {middle_initial} {last_name}"
        return f"{first_name} {middle_name} {last_name}"

    return f"{first_name} {last_name}"


def process_string(string, operation):
    """
    Perform the specified operation on the given string.

    Args:
        string (str): The input string.
        operation (str): The operation to perform on the string.

    Returns:
        str: The processed string.

    Raises:
        ValueError: If the operation is invalid.
    """
    operations = {
        'count_vowels': lambda s: sum(1 for char in s.lower() if char in 'aeiou'),
        'remove_spaces': lambda s: s.replace(' ', '')
    }

    if operation not in operations:
        raise ValueError(f"Error: invalid operation '{operation}'")

    return str(operations[operation](string))
def format_name(first_name, middle_name=None, last_name=None, use_initials=True):
    """
    Format a person's name based on the provided first, middle, and last names.

    Args:
        first_name (str): The person's first name.
        middle_name (str, optional): The person's middle name. Defaults to None.
        last_name (str, optional): The person's last name. Defaults to None.
        use_initials (bool, optional): Whether to use initials for the middle name. Defaults to True.

    Returns:
        str: The formatted name.

    Raises:
        ValueError: If the first_name or last_name is None.
    """
    if first_name is None or last_name is None:
        raise ValueError("First name and last name are required.")

    if middle_name:
        if use_initials:
            formatted_name = f"{first_name} {middle_name[0]}. {last_name}"
        else:
            formatted_name = f"{first_name} {middle_name} {last_name}"
    else:
        formatted_name = f"{first_name} {last_name}"

    return formatted_name


# Example usage
print(format_name("John", "Michael", "Smith"))
print(format_name("John", "Michael", "Smith", False))
print(format_name("John", None, "Smith"))

try:
    print(format_name(None, "Michael", "Smith"))
except ValueError as error:
    print(f"Error: {error}")

try:
    print(format_name("John", "Michael", None))
except ValueError as error:
    print(f"Error: {error}")