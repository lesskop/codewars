# https://www.codewars.com/kata/525f50e3b73515a6db000b83

from typing import Union
from string import digits

IncorrectInputError = Exception("Enter 10 digits for the phone number")


def iterable_has_only_digits(n: Union[list, tuple]) -> bool:
    for char in n:
        if str(char) not in digits:
            return False
    return True


def create_phone_number(n: Union[list, tuple]) -> str:
    if iterable_has_only_digits(n) and len(n) == 10:
        return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
    else:
        raise IncorrectInputError


assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == '(123) 456-7890'
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Incorrect input
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 'b', 9, 0]))  # Incorrect input
