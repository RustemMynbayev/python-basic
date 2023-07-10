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


def filter_odd_num(filter_numbers):
    i = 2
    while filter_numbers % i != 0:
        i += 1
    return i == filter_numbers


def filter_numbers(numbers_list, filter_types):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    >>> filter_numbers([2, 3, 4, 5], PRIME)
    <<< [2, 4]
    """
    if filter_types == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    if filter_types == EVEN:
        return [number for number in numbers_list if number % 2 == 0]
    if filter_types == PRIME:
        return [number for number in numbers_list if number % number == 0]
