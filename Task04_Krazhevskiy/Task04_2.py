
def most_frequent_word(filename):
    '''
    read the file and return the most frequent word
    input: filename
    output: most frequent word
    '''
    fin = open(filename, 'r')
    words = fin.read().split()

    new_words = [word.lower() for word in words]
    
    fin.close()

    if not new_words:
        return

    marks = ',.!?:;-()[]'
    for c in marks:
        for word in new_words:
            for char in word:
                if char in marks:
                    new_words[new_words.index(word)] = word.replace(char, '')

    max_count = 0
    max_word = ''
    for word in new_words:
        count = new_words.count(word)
        if count > max_count:
            max_count = count
            max_word = word
    
    if max_count == 1:
        return 'No word was repeated.'
    
    max_words = []
    for word in new_words:
        if new_words.count(word) == max_count:
            if word not in max_words:
                max_words.append(word)
    
    if len(max_words) != 1:
        return max_words
    else:
        return max_word


if __name__ == '__main__':
    filename = 'file.txt'

    print(most_frequent_word(filename))
