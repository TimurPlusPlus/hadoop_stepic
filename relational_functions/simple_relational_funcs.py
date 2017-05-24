import sys

'''
Дан файл с логами переходов пользователей. Каждая строка состоит из 3 полей:
время перехода (unix timestamp), ID пользователя, URL, на который перешел пользователь.
Напишите mapper с помощью Hadoop Streaming, печатающий только те строки из файла,
которые соответствуют пользователю user10.
'''
def mapper():
    for line in sys.stdin:
        tokens = line.strip().split("\t")
        if tokens[1] == "user10":
            print(*tokens, sep='\t')

'''
Напишите reducer, который объединяет элементы из множества A и B.
На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)
Sample Input:
1	A
2	A
2	B
3	B

Sample Output:
1
2
3
'''
def union():
    prev_key = None
    for line in sys.stdin:
        tokens = line.strip().split('\t')
        if prev_key != tokens[0]:
            print(tokens[0])
            prev_key = tokens[0]

'''
Напишите reducer, который делает пересечение элементов из множества A и B.
На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)
'''
def intersection():
    prev_key = None
    for line in sys.stdin:
        tokens = line.strip().split('\t')
        if tokens[0] == prev_key:
            print(tokens[0])
        prev_key = tokens[0]

'''
Напишите reducer, который делает вычитание элементов множества B из множества A.
На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)
'''
def minus():
    prev_key = None
    for line in sys.stdin:
        tokens = line.strip().split('\t')
        if tokens[1] == 'A':
            if prev_key is not None:
                print(prev_key)
            prev_key = tokens[0]
        else:
            if prev_key is not None and prev_key != tokens[0]:
                print(prev_key)
            prev_key = None
    if prev_key is not None:
        print(prev_key)

'''
Напишите reducer, который реализует симметричную разность множеств A и B
(т.е. оставляет только те элементы, которые есть только в одном из множеств).
На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)
'''
def symmetric_difference():
    prev_key = None
    for line in sys.stdin:
        k, v = line.strip().split('\t')
        if prev_key is not None:
            if k != prev_key:
                print(prev_key)
                prev_key = k
            else:
                prev_key = None
        else:
            prev_key = k
    if prev_key is not None:
        print(prev_key)