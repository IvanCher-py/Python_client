# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

s_1 = b'attribute'
s_2 = b'класс'
s_3 = b'функция'
s_4 = 'type'

#  File "c:/Users/Иван/Desktop/Python клиент_серверные/Lesson1_3.py", line 4
#    s_2 = b'класс'
^
# SyntaxError: bytes can only contain ASCII literal characters.
