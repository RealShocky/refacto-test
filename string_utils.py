# String utility functions that need refactoring

def process_string(s,op):
    # This function does various string operations
    # The code style and structure could be improved
    if op=='upper':
        x=s.upper()
        return x
    if op=='lower':
        x=s.lower()
        return x
    if op=='capitalize':
        x=s.capitalize()
        return x
    if op=='reverse':
        x=''
        i=len(s)-1
        while i>=0:
            x=x+s[i]
            i=i-1
        return x
    if op=='count_vowels':
        x=0
        for c in s:
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
                x=x+1
        return x
    if op=='remove_spaces':
        x=''
        for c in s:
            if c!=' ':
                x=x+c
        return x
    return 'Error: invalid operation'

def format_name(first,middle,last,include_middle=True):
    # Format a name with various options
    # This could be more elegant and handle edge cases better
    if first==None or first=='':
        return 'Error: first name required'
    if last==None or last=='':
        return 'Error: last name required'
    if include_middle==True:
        if middle!=None and middle!='':
            x=first+' '+middle+' '+last
        else:
            x=first+' '+last
    else:
        x=first+' '+last
    return x

# Example usage
print(process_string("Hello World",'upper'))  # HELLO WORLD
print(process_string("Hello World",'lower'))  # hello world
print(process_string("hello world",'capitalize'))  # Hello world
print(process_string("Hello",'reverse'))  # olleH
print(process_string("Hello World",'count_vowels'))  # 3
print(process_string("Hello World",'remove_spaces'))  # HelloWorld
print(process_string("Hello",'invalid'))  # Error: invalid operation

print(format_name("John","Michael","Smith"))  # John Michael Smith
print(format_name("John",None,"Smith"))  # John Smith
print(format_name("John","Michael","Smith",False))  # John Smith
print(format_name(None,"Michael","Smith"))  # Error: first name required
print(format_name("John","Michael",None))  # Error: last name required