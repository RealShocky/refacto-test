# This is a simple calculator that needs refactoring
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

# More examples with edge cases
print(f"Empty list: {process_numbers([],'add')}")
print(f"Division by zero: {calc(5,0,'div')}")
print(f"Invalid operation: {calc(5,2,'power')}")