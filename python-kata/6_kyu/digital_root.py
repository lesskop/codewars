from typing import Callable


def digital_root(num: int) -> Callable | int:
    result = sum([int(digit) for digit in str(num)])
    if result > 9:
        return digital_root(result)
    return result


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
