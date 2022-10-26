def solution(number: int) -> int:
    return sum(num for num in range(number) if (num % 3 == 0) or (num % 5 == 0))


print(solution(10))
