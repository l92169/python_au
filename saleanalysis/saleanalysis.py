from collections import defaultdict
import datetime
import random
import math
import matplotlib.pyplot as plt
from datetime import datetime as dt

N1, N2 = 3, 5
def generate_date_resource(data):
    x_data, y_data = [], []
    d = filter_data(data, 'resource', '{}'.format(N1),'exact')
    for i in range(len(d)):
        x_data.append(d[i]['date'])
        y_data.append(d[i]['count'])
    return (x_data, y_data)


def generate_date_staff_id(data):
    x_data, y_data = [], []
    d = filter_data(data, 'staff_id', '{}'.format(N1),'exact')
    for i in range(len(d)):
        x_data.append(d[i]['date'])
        y_data.append(d[i]['count'])
    return (x_data, y_data)

def drawing_resource(data):
    x, y = generate_date_resource(data)
    plt.plot(x,y, color = 'red', marker = "o")
    plt.title("Resource {}".format(N1))
    plt.xlabel("date")
    plt.ylabel("count")
    plt.show()

def drawing_staff_id(data):
    x, y = generate_date_staff_id(data)
    plt.plot(x,y, color = 'red', marker = "o")
    plt.title("staff_id {}".format(N2))
    plt.xlabel("date")
    plt.ylabel("count")
    plt.show()


def generator_file_with_staff_id():
    file = open('input.csv', "w+")
    file.write('date,resource,staff_id,count \n')
    for i in range(10):
        file.write("{}-{},{},{},{} \n".format(random.randint(2018, 2021),\
                                              random.randint(1, 12),\
                                              random.randint(1, 4),\
                                              random.randint(1, 10),\
                                              random.randint(0, 100)))
    file.close()


def generator_file_without_staff_id():
    file = open('input.csv', "w+")
    file.write('date,resource,count \n')
    for i in range(10):
        file.write("{}-{},{},{},{} \n".format(random.randint(2018, 2021),\
                                              random.randint(1, 12),\
                                              random.randint(0, 4),\
                                              random.randint(0, 100)))
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
    generator_file_with_staff_id()
    data = sort_key(list_dict('input.csv'), 'date')
    drawing_resource(data)
    drawing_staff_id(data)


if __name__ == '__main__':
    main()

