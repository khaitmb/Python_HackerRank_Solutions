# Skills Used: defining a function, case, for loop, else-if function

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# FUNCTION DESCRIPTION
# swap_case function has the following parameters:
# - Input- string s: the string to modify
# - Returns- string: the modified string

# HACKERRANK ACCEPTED SOLUTION
def swap_case(s):
    new_string = ''
    for i in s:
        if i.isupper() == True:
            new_string += i.lower()
        elif i.islower() == True:
            new_string += i.upper()
        else:
            new_string += i
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
