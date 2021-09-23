"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    list_num=[]
    for i in numbers:
        i**=2
        list_num.append(i)
    return list_num

power_numbers(1, 2, 4, 5, 7, 8, 10, 11)


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_odd(num):
     if(num % 2) != 0:
         return True
     else:
         return False

def filter_even(num):
    if(num % 2) == 0:
        return True
    else:
        return False

def filter_numbers(num, var):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """  
    if var == 'odd':
        odd_n = filter(filter_odd, num)
        return list(odd_n)
    elif var == 'even':
        even_n = filter(filter_even, num)
        return list(even_n)
    
filter_numbers([1, 2, 4, 5, 7, 8, 10, 11], ODD)




