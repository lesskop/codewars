# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

from itertools import groupby


def extract_ranges(input_list: list[int]) -> str:
    result = ''

    for _, grouper in groupby(enumerate(input_list), lambda i_x: i_x[0] - i_x[1]):
        range_list = [integer for _, integer in grouper]
        if len(range_list) > 2:
            result += f"{range_list[0]}-{range_list[-1]},"
        else:
            result += ','.join(map(str, range_list)) + ','

    return result.strip(',')


print(extract_ranges([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
print(extract_ranges([-1, 0, 2, 3, 5, 6, 7, 8, 10]))
