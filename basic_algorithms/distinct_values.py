import sys

'''
Distinct values:
Record 1: F=1, G={a,b}
Record 2: F=2, G={a,d,e}

G - categories
F - value

Result:
a->2 #F=1, F=2
b->1 #F=1
d->1 #F=2
e->  #F=2
'''


'''
Реализуйте mapper из фазы 1 задачи Distinct Values v1.
Mapper принимает на вход строку, содержащую значение и через табуляцию список групп, разделенных запятой.

Sample Input:
1	a,b
2	a,d,e
1	b
3	a,b

Sample Output:
1,a	1
1,b	1
2,a	1
2,d	1
2,e	1
1,b	1
3,a	1
3,b	1
'''
def mapper():
    for line in sys.stdin:
        value, category = line.strip().split('\t')
        category = category.split(",")
        for c in category:
            print(value + "," + c + "\t1")

'''
Реализуйте reducer из фазы 1 задачи Distinct Values v1.
Reducer принимает на вход данные, созданные mapper из предыдущей шага.
Sample Input:
1,a	1
1,b	1
1,b	1
2,a	1
2,d	1
2,e	1
3,a	1
3,b	1

Sample Output:
1,a
1,b
2,a
2,d
2,e
3,a
3,b
'''
def reducer():
    prev_line = ""
    for line in sys.stdin:
        if line != prev_line:
            ret = line.strip().split('\t')
            print(ret[0])
            prev_line = line

'''
Реализуйте mapper из фазы 2 задачи Distinct Values v1.
Mapper принимает на вход строку, содержащую значение и группу, разделенные запятой.
Sample Input:
1,a
2,a
3,a
1,b
3,b
2,d
2,e

Sample Output:
a	1
a	1
a	1
b	1
b	1
d	1
e	1
'''
def mapper2():
    for line in sys.stdin:
        tokens = line.strip().split(',')
        print(tokens[1] + "\t1")

'''
Реализуйте reducer из задачи Distinct Values v2.
Reducer принимает на вход строки, каждая из которых состоит из
разделенных табуляцией значения и названия группы.
'''
def reducer2():
    prev_line = ""
    values = dict()
    for line in sys.stdin:
        if line != prev_line:
            prev_line = line
            tokens = line.strip().split('\t')
            values.update({tokens[1]: values.get(tokens[1], 0) + 1})
    for (key, value) in values.items():
        print(key + '\t' + str(value))