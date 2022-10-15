# https://www.codewars.com/kata/5208f99aee097e6552000148

def break_camel_case(s: str) -> str:
    return ''.join(' ' + c if c.isupper() else c for c in s)


print(break_camel_case('testBreakCamelCaseFunction'))
print(break_camel_case('camelCasing'))
print(break_camel_case('identifier'))
print(break_camel_case(''))
