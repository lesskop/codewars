# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string: str) -> bool:
    stack = []

    for parenthesis in string:
        if parenthesis == '(':
            stack.append(parenthesis)
        elif parenthesis == ')':
            try:
                stack.pop()
            except IndexError:
                return False

    if not stack:
        return True

    return False


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))

