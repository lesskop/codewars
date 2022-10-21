# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic(value: int) -> bool:
    return value == sum(int(digit) ** len(str(value)) for digit in str(value))


print(narcissistic(153))
print(narcissistic(1652))
