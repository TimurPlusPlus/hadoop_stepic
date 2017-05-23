import sys

'''
Реализуйте reducer в задаче подсчета среднего времени, проведенного пользователем на странице.
Mapper передает в reducer данные в виде key / value, где key - адрес страницы, value - число секунд,
проведенных пользователем на данной странице.
Среднее время на выходе приведите к целому числу.
'''
def reducer():
    prev_site = ""
    time, num = 0, 0

    for line in sys.stdin:
        site, cur_time = line.strip().split('\t')
        if site == prev_site or prev_site == "":
            time += int(cur_time)
            num += 1
        else:
            print(prev_site + "\t" + str(int(int(time) / num)))
            time = int(cur_time)
            num = 1
        prev_site = site
    print(prev_site + "\t" + str(int(int(time) / num)))

'''
Реализуйте Combiner в задаче подсчета среднего времени, проведенного пользователем на странице.
Mapper пишет данные в виде key / value, где key - адрес страницы, value - пара чисел, разделенных ";".
Первое - число секунд, проведенных пользователем на данной странице, второе равно 1.

Sample Input:
www.facebook.com	100;1
www.google.com	10;1
www.google.com	5;1
www.google.com	15;1
stepic.org	60;1
stepic.org	100;1

Sample Output:
www.facebook.com	100;1
www.google.com	30;3
stepic.org	160;2
'''
def combiner():
    prev_site = ""
    time, num = 0, 0

    for line in sys.stdin:
        site, cur_time = line.strip().split('\t')
        cur_time, n = cur_time.split(";")
        if site == prev_site or prev_site == "":
            time += int(cur_time)
            num += 1
        else:
            print(prev_site + "\t" + str(int(time)) + ";" + str(num))
            time = int(cur_time)
            num = 1
        prev_site = site
    print(prev_site + "\t" + str(int(time)) + ";" + str(num))