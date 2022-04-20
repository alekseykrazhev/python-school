from functools import cmp_to_key


def compare(filename1, filename2):
    parts1 = filename1.split('.')
    parts2 = filename2.split('.')

    if parts1[-1] < parts2[-1]:
        return -1
    elif parts2[-1] < parts1[-1]:
        return 1

    if parts1[0] < parts2[0]:
        return -1
    elif parts2[0] < parts1[0]:
        return 1

    return 0


def sort_filenames(filenames):
    return sorted(filenames, key=cmp_to_key(compare))


if __name__ == '__main__':
    filenames = ['Task03_2.py', 'name.abc', 'Task03_3.py',
                 'file.ame.txt', 'Task03_1.py', 'file.cpp', 'a.a.a.b.e.z.cpp']

    print(sort_filenames(filenames))
