

def split_to_lists(elements):
    count = 0
    frequency = []
    max_frequency = 0
    ans = []
    elements_no_repeats = []
    for i in elements:
        if i not in elements_no_repeats:
            elements_no_repeats.append(i)
    
    for i in elements_no_repeats:
        for j in elements:
            if i == j:
                count += 1
        frequency.append(count)
        if count > max_frequency:
            max_frequency = count
        count = 0
    
    #elements_with_frequency = list(zip(elements_no_repeats, frequency))

    for i in range(max_frequency):
        ans1 = []
        for j in elements:
            if frequency[elements_no_repeats.index(j)] == max_frequency - i:
                ans1.append(j)
        if len(ans1) >= 1:
            ans.append(ans1)

    return ans


if __name__ == '__main__':
    elements = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 3, 3, 3, 10, 10, 8, 8, 7, 8, 8, 8, None, True, True]
    elements1 = [1, 2, 7, 1, 3, 2, 4, 7, 2, 1]
    elements2 = ['new', None, True, 2.012, 2.012, True, False, 8, 8, 8, 8, 10]


    print(split_to_lists(elements))
    print(split_to_lists(elements1))
    print(split_to_lists(elements2))
