# https://www.codewars.com/kata/587731fda577b3d1b0001196

def camel_case(string: str) -> str:
    # return ''.join(word.capitalize() for word in string.split(' '))
    return string.title().replace(" ", "")


print(camel_case("hello case"))
print(camel_case("camel case word"))
print(camel_case("test camel case function written in python"))
