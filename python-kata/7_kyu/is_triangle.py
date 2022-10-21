# https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a: int, b: int, c: int) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)


print(is_triangle(1, 2, 2))
print(is_triangle(7, 2, 2))
