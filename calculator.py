# This is a simple calculator that needs refactoring
# Adding a comment to trigger webhook
import math

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
    if op=='sqrt':
        # Calculate square root using Newton's method
        if a < 0:
            return 'Error: square root not defined for negative numbers'
        if a == 0:
            return 0
        x = a
        for _ in range(10):  # 10 iterations should be enough for most numbers
            x = (x + a/x) / 2
        return x
    if op=='abs':
        # Calculate absolute value
        return abs(a)  # ignore b for abs operation
    if op=='log':
        # Calculate natural logarithm (base e)
        if a <= 0:
            return 'Error: logarithm not defined for non-positive numbers'
        return math.log(a)  # ignore b for log operation
    if op=='exp':
        # Calculate exponential function (e^x)
        return math.exp(a)  # ignore b for exp operation
    if op=='sinh':
        # Calculate hyperbolic sine
        return math.sinh(a)  # ignore b for sinh operation
    if op=='cosh':
        # Calculate hyperbolic cosine
        return math.cosh(a)  # ignore b for cosh operation
    if op=='tanh':
        # Calculate hyperbolic tangent
        return math.tanh(a)  # ignore b for tanh operation
    if op=='atan':
        # Calculate arctangent
        return math.atan(a)  # ignore b for atan operation
    if op=='asin':
        # Calculate arcsine
        if abs(a) > 1:
            return 'Error: arcsine not defined for |x| > 1'
        return math.asin(a)  # ignore b for asin operation
    if op=='acos':
        # Calculate arccosine
        if abs(a) > 1:
            return 'Error: arccosine not defined for |x| > 1'
        return math.acos(a)  # ignore b for acos operation
    if op=='acoth':
        # Calculate hyperbolic arccotangent
        if abs(a) <= 1:
            return 'Error: hyperbolic arccotangent not defined for |x| <= 1'
        return 0.5 * math.log((a + 1)/(a - 1))  # ignore b for acoth operation
    if op=='asech':
        # Calculate hyperbolic arcsecant
        if a <= 0 or a > 1:
            return 'Error: hyperbolic arcsecant only defined for 0 < x <= 1'
        return math.log((1 + math.sqrt(1 - a*a))/a)  # ignore b for asech operation
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
print(f"Square root of 16: {calc(16,0,'sqrt')}")
print(f"Absolute value of -42: {calc(-42,0,'abs')}")
print(f"Natural log of 2.718: {calc(2.718,0,'log')}")
print(f"e^2: {calc(2,0,'exp')}")
print(f"sinh(1): {calc(1,0,'sinh')}")
print(f"cosh(1): {calc(1,0,'cosh')}")
print(f"tanh(1): {calc(1,0,'tanh')}")
print(f"atan(1): {calc(1,0,'atan')}")
print(f"asin(0.5): {calc(0.5,0,'asin')}")
print(f"acos(0.5): {calc(0.5,0,'acos')}")
print(f"acoth(2): {calc(2,0,'acoth')}")
print(f"asech(0.5): {calc(0.5,0,'asech')}")

# More examples with edge cases
print(f"Empty list: {process_numbers([],'add')}")
print(f"Division by zero: {calc(5,0,'div')}")
print(f"Invalid operation: {calc(5,2,'invalid')}")
print(f"Factorial of negative number: {calc(-1,0,'factorial')}")
print(f"GCD with zero: {calc(15,0,'gcd')}")
print(f"LCM with zero: {calc(15,0,'lcm')}")
print(f"Square root of negative number: {calc(-4,0,'sqrt')}")
print(f"Absolute value of zero: {calc(0,0,'abs')}")
print(f"Log of zero: {calc(0,0,'log')}")
print(f"Log of negative number: {calc(-1,0,'log')}")
print(f"e^0: {calc(0,0,'exp')}")
print(f"sinh(0): {calc(0,0,'sinh')}")
print(f"cosh(0): {calc(0,0,'cosh')}")
print(f"tanh(0): {calc(0,0,'tanh')}")
print(f"atan(0): {calc(0,0,'atan')}")
print(f"asin(2): {calc(2,0,'asin')}")  # Error case: |x| > 1
print(f"acos(2): {calc(2,0,'acos')}")  # Error case: |x| > 1
print(f"acoth(0.5): {calc(0.5,0,'acoth')}")  # Error case: |x| <= 1
print(f"asech(2): {calc(2,0,'asech')}")  # Error case: x > 1
print(f"asech(0): {calc(0,0,'asech')}")  # Error case: x <= 0