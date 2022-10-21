# https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheep(arr: list[bool]) -> int:
    return len([sheep for sheep in arr if sheep])


print(count_sheep([True, True, True, False,
                   True, True, True, True,
                   True, False, True, False,
                   True, False, False, True,
                   True, True, True, True,
                   False, False, True, True]))
