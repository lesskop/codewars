# https://www.codewars.com/kata/5264d2b162488dc400000001/python

def spin_words(sentence: str) -> str:
    return " ".join(x[::-1] if len(x) >= 5 else x for x in sentence.split())


print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))
