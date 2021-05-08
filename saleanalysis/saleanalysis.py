from collections import defaultdict
import datetime
from datetime import datetime as dt

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
    if key in ['resource', 'count']:
        return sorted(data, key=lambda x: int(x[key] if x[key] != '' else 0))
    if key == 'date':
        return sorted(data, key=lambda x: convert_date(x[key]) if x[key] != '' else datetime.datetime(1, 1, 1, 1, 1, 1, 1))
    if key == 'staff_id':
        return sorted(data, key=lambda x: x[key].strip())



def main():
    data = list_dict('input.csv')
    #print(data)
    #print(sort_key(data, 'date'))


if __name__ == '__main__':
    main()

