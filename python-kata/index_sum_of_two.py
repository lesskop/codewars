"""
На вход подается список чисел и целевое число на отдельной строке.
Верните индексы двух чисел, которые в сумме дают целевое число.

Любые входные данные имеют только 1 решение и один и тот же элемент списка не нужно использовать дважды.

Индексы можно вернуть в любом порядке.

Sample Input:
2,7,11,15
9

Sample Output:
[0, 1]
"""

from itertools import combinations

input_list = input().split(',')
input_list = list(map(int, input_list))

target = int(input())

result = []

for x, y in combinations(input_list, 2):
    if x + y == target:
        start_index = input_list.index(x)
        result.append(start_index)
        result.append(input_list.index(y, start_index + 1))

print(result)
