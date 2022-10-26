from collections import Counter


def find_it(input_list: list) -> int:
    dict_count = Counter(input_list)
    for num, count in dict_count.items():
        if count % 2 != 0:
            return num


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
print(find_it([0, 1, 0, 1, 0]))
print(find_it([1, 1, 2]))
