# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9

def input_is_valid(input_list: list[int]) -> bool:
    for num in input_list:
        if num > 9:
            return False
    return True


def up_array(input_list: list[int]) -> list[int] | None:
    if not input_is_valid(input_list):
        return None

    input_num = int(''.join(map(str, input_list)))
    result = [int(digit) for digit in str(input_num + 1)]

    if input_list[0] == 0:
        result.insert(0, 0)

    return result


print(up_array([4, 3, 2, 5]))
print(up_array([1, 2, 3, 9]))
print(up_array([9, 9, 9, 9]))
print(up_array([0, 1, 3, 7]))
