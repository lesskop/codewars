# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word: str, words: list[str]) -> list[str | None]:
    return [item for item in words if sorted(item) == sorted(word)]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy', 'lacer']))
