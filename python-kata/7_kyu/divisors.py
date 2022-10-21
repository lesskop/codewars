# https://www.codewars.com/kata/542c0f198e077084c0000c2e

def divisors(num: int) -> int:
    return len([divisor for divisor in range(1, num + 1) if not num % divisor])


print(divisors(4))
print(divisors(5))
print(divisors(12))
print(divisors(30))
