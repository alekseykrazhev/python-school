# module for sorting algorithms

def get_field_to_sort(field_name: str, arr):
    """
    get field to sort by
    """
    if field_name == "Marks":
        sum_ = sum(arr[field_name])
        return sum_ / len(arr[field_name])
    return arr[field_name]


def bubble_sort(arr, field_name: str) -> list:
    """
    bubble sort algorithm
    """
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if get_field_to_sort(field_name, arr[j]) > get_field_to_sort(field_name, arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr, field_name):
    """
    insertion sort algorithm
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and get_field_to_sort(field_name, arr[j]) < get_field_to_sort(field_name, arr[j-1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def shell_sort(arr, field_name):
    """
    Shell sort algorithm
    """
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            while j >= gap and get_field_to_sort(field_name, arr[j]) < get_field_to_sort(field_name, arr[j - gap]):
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap //= 2
    return arr


def selection_sort(arr, field_name):
    """
    selection sort algorithm
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if get_field_to_sort(field_name, arr[j]) < get_field_to_sort(field_name, arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(arr, field_name):
    """
    merge sort algorithm
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], field_name)
    right = merge_sort(arr[mid:], field_name)
    return merge(left, right, field_name)


def merge(left, right, field_name):
    """
    merge two sorted arrays
    """
    result = []
    while len(left) > 0 and len(right) > 0:
        if get_field_to_sort(field_name, left[0]) < get_field_to_sort(field_name, right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


def partition(arr, lo, hi, field_name):
    pivot = get_field_to_sort(field_name, arr[(lo + hi) // 2])
    i = lo
    j = hi
    while True:
        while get_field_to_sort(field_name, arr[i]) < pivot:
            i += 1
        while get_field_to_sort(field_name, arr[j]) > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_hoar(arr, lo, hi, field_name):
    """
    Quick sort algorithm using Hoar decomposition
    """
    if lo < hi:
        p = partition(arr, lo, hi, field_name)
        quick_sort_hoar(arr, lo, p, field_name)
        quick_sort_hoar(arr, p + 1, hi, field_name)


def quick_sort_rand(arr, field_name):
    """
    quick sort algorithm using random pivot value
    """
    import random

    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = get_field_to_sort(field_name, arr[pivot_index])
    left = [i for i in arr if get_field_to_sort(field_name, i) < pivot]
    mid = [i for i in arr if get_field_to_sort(field_name, i) == pivot]
    right = [i for i in arr if get_field_to_sort(field_name, i) > pivot]
    return quick_sort_rand(left, field_name) + mid + quick_sort_rand(right, field_name)
