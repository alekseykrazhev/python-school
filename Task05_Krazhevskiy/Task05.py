# Task5 of ISSoft python school by Aleksey Krazhevskiy

def partition(arr, l, r):
    """
    Function that partitions the array and returns q index
    """
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def k_min(arr: list, k: int) -> int:
    """
    Function that returns the k-th minimal element of the array
    """
    # exception handling
    try:
        int(k)
        arr[k-1]
    except ValueError:
        raise ValueError("[Exception] Not an integer")
    except IndexError:
        raise IndexError("[Exception] k is out of range")
    k = int(k)

    if len(arr) == 1:
        return arr[0]
    elif len(arr) < 1:
        raise IndexError("[Exception] Array is empty")

    if not all(isinstance(i, int) or isinstance(i, float)for i in arr) and not all(isinstance(i, str) for i in arr):
        raise TypeError(
            "[Exception] Type of elements in the array is not the same")

    # computing kth smallest element
    if k > 0:
        pos = partition(arr, 0, len(arr)-1)

        if pos == k-1:
            return arr[pos]
        elif pos > k-1:
            return k_min(arr[:pos], k)
        elif pos < k-1:
            return k_min(arr[pos+1:], k-pos-1)

    return 'Error while computing k-min'


if __name__ == '__main__':
    #arr = list(input('Enter array:').split())
    #k = input('Enter k:')

    arr1 = [10, True, False, 2, 9]
    k1 = 2

    arr2 = ['sdsdf', 1, True, 2, 8, 10]
    k2 = 3

    arr3 = [5, 6, 2, 3, 4.0, 8.0, 15, 1.0, 9, 10, 1]
    k3 = 8

    arr4 = [True, False, True, 0, 10.0]
    k4 = 2
    
    #print(f"[1] {k}-th minimal element is {k_min(arr, k)}")
    print(f"[2] {k1}-th minimal element is {k_min(arr1, k1)}")
    print(f"[4] {k3}-th minimal element is {k_min(arr3, k3)}")
    print(f"[5] {k4}-th minimal element is {k_min(arr4, k4)}")

    print(f"[3] {k2}-th minimal element is {k_min(arr2, k2)}")  # this one catches the exception
