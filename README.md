Задание №1

Условие:
Написать функцию, которая находит самые повторяющиеся слова в строке.

Пример:

simple_text('Am I want write code? Yeah! I like it') → I
simple_text('Hi! How are you? Hi! I am okay') → Hi
simple_text('test text test and test that again') → test


=======================================================================================
Задание №2

Условие:

Написать функцию, которая сортирует список с оценками на основе английской системы.
Всего 5 символов, в порядке убывания: A, B, C, D, F.

Примеры:

sort_grades(['A', 'B', 'C', 'C', 'F', 'A']) -> ['F', 'C', 'C', 'B', 'A', 'A']
sort_grades(['b', 'c', 'C', 'f', 'A']) -> ['F', 'C', 'C', 'B', 'A']
sort_grades([]) -> []


=======================================================================================
Задание №3

Условие:

Написать функцию, которая проверяет, являются ли две строки анаграммами?
На вход идут две строки, состоящие из символов английского алфавита.

Примеры:

is_anagram('car', 'tar') -> False
is_anagram('car', 'cart') -> False
is_anagram('anagram', 'nagaram') -> True
is_anagram('beluga', 'begula') -> True


=======================================================================================
Задание №4

Условие:

Написать функцию, которая сортирует список, но все четные числа должны остаться на своем месте.

Примеры:

sort_array([3, 1]) -> [1, 3]
sort_array([3, 2, -1, 4]) -> [-1, 2, 3, 4]
sort_array([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]


=======================================================================================
Задание №5

Условие:

Написать функцию которая, будет переводить римские символы в привычную нам десятичную систему.

Пример:

roman_to_int('XXI') -> 21
roman_to_int('IV') -> 4
roman_to_int('I') -> 1