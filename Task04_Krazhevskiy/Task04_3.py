
def same_words_in_files(filename1: str, filename2: str) -> list:
    '''
    find same words in two files
    input: filename1, filename2
    output: same words
    '''
    fin1 = open(filename1, 'r')
    fin2 = open(filename2, 'r')

    words1 = fin1.read().split()
    words2 = fin2.read().split()

    if not words1 or not words2:
        return []

    fin1.close()
    fin2.close()

    new_words1 = [word.lower() for word in words1]
    new_words2 = [word.lower() for word in words2]

    same_words = []
    for word in new_words1:
        if word in new_words2:
            if word not in same_words:
                same_words.append(word)
        
    if len(same_words) == 0:
        return 'No same words.'

    return same_words


if __name__ == '__main__':
    filename1 = 'file1.txt'
    filename2 = 'file2.txt'

    print(same_words_in_files(filename1, filename2))
