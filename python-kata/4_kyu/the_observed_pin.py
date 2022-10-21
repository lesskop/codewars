# https://www.codewars.com/kata/5263c6999e0f40dee200059d

from itertools import product

ADJACENT = {
    '1': ['2', '4'],
    '2': ['1', '3', '5'],
    '3': ['2', '6'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'],
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['5', '7', '9', '0'],
    '9': ['6', '8'],
    '0': ['8']
}


def get_pins(pin: str) -> list[str]:
    possible_digits = [[digit] + ADJACENT[digit] for digit in pin]
    return [''.join(digit) for digit in list(product(*possible_digits))]


print(get_pins('10'))
print(get_pins('1357'))
