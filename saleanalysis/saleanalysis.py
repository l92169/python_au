from collections import defaultdict
import datetime
import random
import math
import matplotlib.pyplot as plt
from datetime import datetime as dt
year = 2020


def generate_date_resource(data, N1):
    x_data, y_data = [], []
    d = filter_data(data, 'resource', '{}'.format(N1),'exact')
    for i in range(len(d)):
        x_data.append(d[i]['date'])
        y_data.append(int(d[i]['count']))
    return (x_data, y_data)


def generate_date_staff_id(data, N2):
    x_data, y_data = [], []
    d = filter_data(data, 'staff_id', '{}'.format(N2),'exact')
    for i in range(len(d)):
        x_data.append(d[i]['date'])
        y_data.append(int(d[i]['count']))
    return (x_data, y_data)


def drawing_one_resource_(data, N1):
    x, y = generate_date_resource(data, N1)
    plt.plot(x,y, color = 'red', marker = "o")
    plt.title("Resource {}".format(N1))
    plt.xlabel("date")
    plt.ylabel("count")
    plt.show()


def drawing_all_resource_(data):
    for i in range(1,11):
        x, y = generate_date_resource(data)
        plt.plot(x,y, color = 'red', marker = "o")
        plt.title("Resource {}".format(i))
        plt.xlabel("date")
        plt.ylabel("count")
        plt.show()

def drawing_one_staff_id(data, N2):
    x, y = generate_date_staff_id(data, N2)
    plt.plot(x,y, color = 'red', marker = "o")
    plt.title("staff_id {}".format(N2))
    plt.xlabel("date")
    plt.ylabel("count")
    plt.show()


def drawing_all_staff_id(data):
    for i in range(1,10):
        x, y = generate_date_staff_id(data, i)
        plt.plot(x,y, color = 'red', marker = "o")
        plt.title("staff_id {}".format(i))
        plt.xlabel("date")
        plt.ylabel("count")
        plt.show()


def generator_file_with_staff_id():
    file = open('input1.csv', "w+")
    data = open_file('input.csv')
    file.write('date,resource,staff_id,count \n')
    for i in range(1, len(data)):
        d = 0
        summ = 0
        count_staff_id = int(data[i][2])
        while count_staff_id > summ:
            new_count_staff_id = random.randint(0, 100)
            summ = summ + new_count_staff_id
            if count_staff_id < summ:
                summ = summ - new_count_staff_id
                new_count_staff_id = count_staff_id - summ
                d = 1
            if count_staff_id > summ:
                file.write("{},{},{},{} \n".format(data[i][0],
                                                   data[i][1],
                                                   random.randint(1, 10),
                                                   new_count_staff_id))
            if d == 1:
                break
    file.close()


def generator_file_without_staff_id():
    file = open('input.csv', "w+")
    file.write('date,resource,count \n')
    for i in range(1,11):
        for j in range(1, 13):
            file.write("{}-{},{},{} \n".format(year, j, i, random.randint(0, 100)))
    file.close()

def open_file(input_file):
    with open(input_file) as d:
        return list(map(lambda x: x.strip().split(','), d.readlines()))


def list_dict(input_file):
    data = open_file(input_file)
    headers = data[0]
    return list(map(lambda x: dict(zip(headers, x)), data[1::]))


def convert_date(date):
    return dt.strptime(date, "%Y-%m")


def sort_key(data, key):
    if key in ['resource', 'count', 'staff_id']:
        return sorted(data, key=lambda x: int(x[key] if x[key] != '' else 0))
    if key == 'date':
        return sorted(data, key=lambda x: convert_date(x[key]) if x[key] != '' else datetime.datetime(1, 1, 1, 1, 1, 1, 1))


def filtration(data, x, value, arg):
    if data == 'date':
        arg_option = {'more': convert_date(x[data]) > convert_date(value) if x[data] != '' else None,
                      'less': convert_date(x[data]) < convert_date(value) if x[data] != '' else None,
                      'exact': convert_date(x[data]) == convert_date(value) if x[data] != '' else None}
        return arg_option[arg]
    if data in ['resource', 'count', 'staff_id']:
        arg_option = {'more': int(x[data]) > int(value) if x[data] != '' else None,
                      'less': int(x[data]) < int(value) if x[data] != '' else None,
                      'exact': int(x[data]) == int(value) if x[data] != '' else None}
        return arg_option[arg]


def filter_data(data, key, value, arg):
    return list(filter(lambda x: filtration(key, x, value, arg), data))


def main():
    generator_file_without_staff_id()
    generator_file_with_staff_id()
    print(list_dict('test.csv'))
    data1 = sort_key(list_dict('input.csv'), 'date')
    data2 = sort_key(list_dict('input1.csv'), 'date')
    drawing_one_resource_(data1,3)
    drawing_one_staff_id(data2,5)


if __name__ == '__main__':
    main()

