

def reverse_line(line):
    ans = ''
    last_indx = 0

    for i in range(len(line)):
        if i == len(line) - 1:
            ans = ans + reverse_word(line[last_indx:i+1])
            break
        
        if line[i] == ' ' or line[i] == ',' or line[i] == '.' or line[i] == '?' or line[i] == '!':
            ans = ans + reverse_word(line[last_indx:i]) + line[i]
            last_indx = i + 1
            
    return ans


def reverse_word(word):
    if len(word) == 0 or len(word) == 1:
        return word
    else:
        return word[-1] + reverse_word(word[:-1])
   

if __name__ == '__main__':
    line = str(input("Enter a line:"))
    
    print(f"Line with reversed words: {reverse_line(line)}")
    