"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [numbers ** 2 for numbers in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

def filter_numbers(numbers, filter_type):
    if filter_type == ODD:
        return [num for num in numbers if num % 2 != 0]
    elif filter_type == EVEN:
        return [num for num in numbers if num % 2 == 0]
    elif filter_type == PRIME:
        return [num for num in numbers if is_prime(num)]
    else:
        return []
