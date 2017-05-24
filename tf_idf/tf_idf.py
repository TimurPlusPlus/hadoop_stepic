import sys
import string

'''
Реализуйте mapper первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
Формат входных данных следующий: каждая строка содержит номер документа и строку из него,
разделенные ":". Ключ выходных данных является составным: он содержит слово документа и его номер, разделенные "#".
Слово в документе - последовательность символов (букв или цифр),
не содержащая пробельных символов и знаков пунктуации.
'''
def mapper1():
    for line in sys.stdin:
        doc, text = line.strip().split(":", 1)
        for punct in string.punctuation:
            text = text.replace(punct, ' ')
        text = text.split()
        for i in text:
            print(i + '#' + str(doc) + '\t1')

'''
Реализуйте reducer первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
Ключ входных данных составной: он содержит слово и номер документа через "#".
Ключом в выходных данных является слово, а значение состоит из двух элементов,
разделенных табуляцией: номер документа и tf (сколько раз данное слово встретилось в данном документе).
'''
def reducer2():
    prev_key = None
    sum = 0
    for line in sys.stdin:
        tokens = line.strip().split('\t')
        if tokens[0] != prev_key and prev_key:
            prev_key = prev_key.split('#')
            print(prev_key[0] + '\t' + prev_key[1] + '\t' + str(sum))
            sum = 1
        else:
            sum += 1
        prev_key = tokens[0]
    prev_key = prev_key.split('#')
    print(prev_key[0] + '\t' + prev_key[1] + '\t' + str(sum))

'''
Реализуйте mapper ﻿второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
Во входных данных ключом является слово, а значение состоит из номера документа и tf, разделенных табуляцией.
Значение в выходных данных - это тройка: номер документа, tf и единица, разделенные ";".
'''
def mapper2():
    for line in sys.stdin:
        tokens = line.strip().split('\t')
        print(tokens[0] + '\t' + str(tokens[1]) + ';' + str(tokens[2]) + ';1')

'''
Реализуйте reducer второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
Входные данные: ключ - слово, значение - тройка: номер документа, tf слова в документе и 1 (разделены ';').
Выходные данные: ключ - пара: слово, номер документа (разделены '#'), значение - пара:
tf слова в документе, n - количество документов с данным словом (разделены табуляцией).
'''
def reducer2():
    prev_word = None
    docs = []
    tfs = []
    n = 0
    for line in sys.stdin:
        word, numbers = line.strip().split('\t')
        numbers = numbers.split(';')
        if word != prev_word and prev_word:
            for i in range(len(tfs)):
                print(prev_word + '#' + docs[i] + '\t' + tfs[i] + '\t' + str(n))
            tfs = []
            docs = []
            n = 0
        prev_word = word
        tfs.append(numbers[1])
        docs.append(numbers[0])
        n += 1
    for i in range(len(tfs)):
        print(prev_word + '#' + docs[i] + '\t' + tfs[i] + '\t' + str(n))