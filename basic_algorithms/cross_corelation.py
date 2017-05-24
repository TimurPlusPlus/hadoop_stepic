import sys

'''
Cross corelation:
Есть множество кортежей объектов.
Для каждой пары объектов посчитать число кортежей, где они встречаются вместе.
Найти покупателей, покупающих один и тот же товар.
'''
'''
Реализуйте mapper для задачи Cross-Correlation, который для каждого кортежа создает все пары элементов, входящих в него.
Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных пробелом.
Mapper пишет данные в виде key / value, где key - пара объектов, разделенных запятой, value - единица.
Sample Input:
a b
a b a c

Sample Output:
a,b	1
b,a	1
a,b	1
a,c	1
b,a	1
b,a	1
b,c	1
a,b	1
a,c	1
c,a	1
c,b	1
c,a	1
'''
def mapper():
    for line in sys.stdin:
        tokens = line.strip().split(' ')
        for i in range(len(tokens)):
            for j in range(len(tokens)):
                if i != j and tokens[i] != tokens[j]:
                    print(tokens[i] + ',' + tokens[j] + '\t1')

'''
Реализуйте mapper для задачи Cross-Correlation, который для каждого объекта из кортежа создает stripe.
Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных пробелом.
Mapper пишет данные в виде key / value, где key - объект, value - соответствующий stripe (пример: a:1,b:2,c:3)
Sample Input:
a b
a b a c

Sample Output:
a	b:1
b	a:1
a	b:1,c:1
b	a:2,c:1
a	b:1,c:1
c	b:1,a:2
'''
def stripe_mapper():
    for line in sys.stdin:
        tokens = line.strip().split(' ')
        for i in range(len(tokens)):
            h = dict()
            for j in range(len(tokens)):
                if i != j and tokens[i] != tokens[j]:
                    h[tokens[j]] = h.get(tokens[j], 0) + 1
            s = tokens[i] + '\t'
            for (key, value) in h.items():
                s += key + ':' + str(value) + ','
            s = s[:len(s) - 1]
            print(s)