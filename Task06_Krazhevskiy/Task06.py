# ISSoft Python School, Task 6 - Implement sorting of the json file by Aleksey Krazhevskiy

import csv
import json
from sortings import *
import time as t


def sort_json(file_name, field_name, sorting_algorithm):
    with open(file_name, 'r') as fin:
        data = json.load(fin)
    if sorting_algorithm == quick_sort_hoar:
        sorting_algorithm(data, 0, len(data) - 1, field_name)
        return data
    else:
        sorted_data = sorting_algorithm(data, field_name)
        return sorted_data


def sort_json_data(data_, sorting_algorithm, field_name):
    if sorting_algorithm == quick_sort_hoar:
        sorting_algorithm(data_, 0, len(data_) - 1, field_name)
        return data_
    else:
        sorted_data = sorting_algorithm(data_, field_name)
        return sorted_data


def get_statistics(sorting_method, data__):
    start = t.perf_counter()
    sort_json_data(data__, sorting_method, 'Marks')
    stop = t.perf_counter()
    return stop - start


def fill_statistics(sort_algorithms: list, _data):
    statistics_ = []
    for sorting in sort_algorithms:
        statistics_.append(get_statistics(sorting, _data.copy()))
    return statistics_


def write_statistics_csv(statistics_: list, file_name: str):
    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, ['BubbleSort', 'InsertionSort', 'ShellSort', 'SelectionSort', 'QuickSortH',
                                    'QuickSortR', 'MergeSort'])
        writer.writeheader()
        writer.writerow(
            {'BubbleSort': statistics_[0], 'InsertionSort': statistics_[1], 'ShellSort': statistics_[2],
             'SelectionSort': statistics_[3], 'QuickSortH': statistics_[4], 'QuickSortR': statistics_[5],
             'MergeSort': statistics_[6]})


def write_sorted_json(sorted_data: list, file_name: str):
    with open(file_name, 'w') as f:
        json.dump(sorted_data, f)


if __name__ == '__main__':
    sorted_ = sort_json('Input.json', 'Marks', bubble_sort)
    write_sorted_json(sorted_, 'Output.json')

    sort_algorithms_ = [bubble_sort, insertion_sort, shell_sort, selection_sort,
                        quick_sort_hoar, quick_sort_rand, merge_sort]

    with open('Input.json', 'r') as fin:
        data = json.load(fin)

    statistics = fill_statistics(sort_algorithms_, data)
    write_statistics_csv(statistics, 'Statistics.csv')

    print('Program finished')
