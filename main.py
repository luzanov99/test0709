from ast import While
from collections import Counter
#1
def simple_text(phrase :str):
    
    phrase = phrase.lower()
    words_list = phrase.split(' ')
    count = Counter(words_list)
    return count.most_common()[0]
#2
def sort_grades(value_list : list):
    f_list = []
    d_list = []
    c_list = []
    b_list = []
    a_list = []

    for element in value_list:
        if element == 'F':
            f_list.append('F')
        elif element == 'D':
            d_list.append('D')
        elif element == 'C':
            c_list.append('C')
        elif element == 'B':
            b_list.append('B')
        elif element == 'A':
            a_list.append('A')
    result = f_list + d_list + c_list + b_list + a_list
    #result = sorted(value_list, reverse=True)
    return result
#3
def is_anagram(word1:str, word2:str):
    word_list1 =  sorted(list(word1))
    word_list2 =  sorted(list(word2))
    return word_list1 == word_list2

#4
def sort_array(value_list):
    position_odd_number_list = []
    odd_number_list = []
    for i in range(0, len(value_list)):
        if value_list[i]%2 == 1:
            position_odd_number_list.append(i)
            odd_number_list.append(value_list[i])
    odd_number_list = sorted(odd_number_list)
    for i in range(0, len(odd_number_list)):
        value_list[position_odd_number_list[i]] = odd_number_list[i]
    return value_list     

#5
def roman_to_int(word:str):
    result = 0
    combination = dict(I=1, V=5, X=10)
    for i ,c in enumerate(word):
        if i+1<len(word) and combination[word[i]] < combination[word[i+1]]:
            result -= combination[word[i]]
        else:
            result += combination[word[i]]
                  
    return str(result)   

if __name__ == '__main__':
    print(simple_text('Am I want write code? Yeah! I like it'))
    print(simple_text('Hi! How are you? Hi! I am okay'))
    print(simple_text('test text test and test that again'))
    print(sort_grades(['A', 'B', 'C', 'C', 'F', 'A']))
    print(sort_grades(['B', 'C', 'C', 'F', 'A']))
    print(sort_grades([]))
    print(is_anagram('car', 'tar'))
    print(is_anagram('car', 'cart'))
    print(is_anagram('anagram', 'nagaram'))
    print(is_anagram('beluga', 'begula'))
    print(sort_array([3, 1]))
    print(sort_array([3, 2, -1, 4]))
    print(sort_array([5, 3, 2, 8, 1, 4]))
    print(roman_to_int('XXI'))
    print(roman_to_int('IV'))
    print(roman_to_int('I'))