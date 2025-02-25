# This is a simple calculator that needs refactoring
# Adding a comment to trigger webhook
def calc(a,b,op):
    # This function does basic math operations
    if op=='add':
        x=a+b
        return x
    if op=='sub':
        x=a-b
        return x
    if op=='mul':
        x=a*b
        return x
    if op=='div':
        if b==0:
            return 'Error: division by zero'
        x=a/b
        return x
    if op=='square':
        x=a*a  # ignore b for square operation
        return x
    if op=='cube':
        x=a*a*a  # ignore b for cube operation
        return x
    if op=='power':
        x = a
        for _ in range(b-1):
            x = x * a
        return x
    if op=='factorial':
        if a < 0:
            return 'Error: factorial not defined for negative numbers'
        if a == 0:
            return 1
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result
    if op=='gcd':
        # Calculate Greatest Common Divisor using Euclidean algorithm
        while b:
            a, b = b, a % b
        return abs(a)
    if op=='lcm':
        # Calculate Least Common Multiple using GCD
        if a == 0 or b == 0:
            return 0
        gcd = calc(a, b, 'gcd')
        return abs(a * b) // gcd
    return 'Error: invalid operation'

def process_numbers(numbers_list,operation):
    # Process a list of numbers with the given operation
    if len(numbers_list)==0:
        return 'Error: empty list'
    result=numbers_list[0]
    for i in range(1,len(numbers_list)):
        result=calc(result,numbers_list[i],operation)
    return result

# Example usage
nums=[10,5,2]
print(f"Addition: {process_numbers(nums,'add')}")
print(f"Multiplication: {process_numbers(nums,'mul')}")
print(f"Division: {process_numbers(nums,'div')}")
print(f"Subtraction: {process_numbers(nums,'sub')}")
print(f"Square of 5: {calc(5,0,'square')}")
print(f"Cube of 3: {calc(3,0,'cube')}")
print(f"2 to the power of 3: {calc(2,3,'power')}")
print(f"Factorial of 5: {calc(5,0,'factorial')}")
print(f"GCD of 48 and 18: {calc(48,18,'gcd')}")
print(f"LCM of 15 and 20: {calc(15,20,'lcm')}")

# More examples with edge cases
print(f"Empty list: {process_numbers([],'add')}")
print(f"Division by zero: {calc(5,0,'div')}")
print(f"Invalid operation: {calc(5,2,'invalid')}")
print(f"Factorial of negative number: {calc(-1,0,'factorial')}")
print(f"GCD with zero: {calc(15,0,'gcd')}")
print(f"LCM with zero: {calc(15,0,'lcm')}")