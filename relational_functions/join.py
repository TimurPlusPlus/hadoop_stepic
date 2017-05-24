import sys

'''
Напишите reducer, реализующий объединение двух файлов (Join) по id пользователя.
Первый файл содержит 2 поля через табуляцию: id пользователя и запрос в поисковой системе.
Второй файл содержит id пользователя и URL, на который перешел пользователь в поисковой системе.
Mapper передает данные в reducer в виде key / value, где key - id пользователя, value состоит из 2 частей:
маркер файла-источника (query или url) и запрос или URL.
Каждая строка на выходе reducer должна содержать 3 поля, разделенных табуляцией: id пользователя, запрос, URL.
'''
def reducer():
    prev_id = None
    lst_url = []
    lst_query = []
    for line in sys.stdin:
        id, values = line.strip().split('\t')
        tag, value = values.split(':')
        if prev_id != id and prev_id:
            if lst_query and lst_url:
                for u in lst_url:
                    for q in lst_query:
                        print(prev_id + '\t' + q + '\t' + u)
            lst_url = []
            lst_query = []
        if tag == 'url':
            lst_url.append(value)
        else:
            lst_query.append(value)
        prev_id = id

    if lst_query and lst_url:
        for u in lst_url:
            for q in lst_query:
                print(prev_id + '\t' + q + '\t' + u)