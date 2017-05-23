import sys

'''
Напишите программу, которая реализует mapper для задачи WordCount в Hadoop Streaming
'''
def mapper():
    for line in sys.stdin:
        for word in line.strip().split(" "):
            if word: print(word+'\t1')

'''
Напишите программу, которая реализует reducer для задачи WordCount в Hadoop Streaming.
'''
def reducer():
    (prev_word, sum) = (None, 0)
    for line in sys.stdin:
        (word, count) = line.strip().split('\t')
        if prev_word and prev_word != word:
            print(prev_word + '\t' + str(sum))
            (prev_word, sum) = (word, 1)
        else:
            (prev_word, sum) = (word, sum + int(count))
    print(prev_word + '\t' + str(sum))

'''
Напишите программу, которая реализует In-mapper combining v.1 для задачи WordCount в Hadoop Streaming.
Sample Input:
aut Caesar aut nihil
aut aut
de mortuis aut bene aut nihil

Sample Output:
nihil	1
aut	2
Caesar	1
aut	2
nihil	1
aut	2
de	1
bene	1
mortuis	1
'''
def mapper_combine1():
    for line in sys.stdin:
        terms = dict()
        for t in line.strip().split(" "):
            terms.update({t: terms.get(t, 0) + 1})
        for i in terms:
            print(i + '\t' + str(terms[i]))

'''
Напишите программу, которая реализует In-mapper combining v.2 для задачи WordCount в Hadoop Streaming.
Sample Input:
aut Caesar aut nihil
aut aut
de mortuis aut bene aut nihil

Sample Output:
aut	6
mortuis	1
bene	1
Caesar	1
de	1
nihil	2
'''
def mapper_combine2():
    terms = dict()
    for line in sys.stdin:
        for term in line.strip().split(" "):
            terms.update({term: terms.get(term, 0) + 1})
    for t in terms:
        print(t + '\t' + str(terms[t]))