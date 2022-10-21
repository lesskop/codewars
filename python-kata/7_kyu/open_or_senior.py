# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(data: list[list[int]]) -> list[str]:
    return ['Senior' if age >= 55 and handicap > 7 else 'Open' for (age, handicap) in data]


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
print(open_or_senior([[16, 23], [73, 1], [56, 20], [1, -1]]))
