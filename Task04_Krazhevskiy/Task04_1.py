
def morse_decode(encoded: str):
    '''
    turn morse code into readable text
    encoded: string
    return readable text
    '''

    if not encoded:
        return

    morse_code = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
        '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9', '': ' ', '\n': ''
    }

    enc = ''.join([morse_code[i] for i in encoded.split(' ')])

    res = ''
    i = 0
    while i < len(enc):
        if enc[i:i+3] == '   ':
            res += ' '
            i += 3
        else:
            if enc[i:i+2] == '  ':
                res += ' '
                i += 2
            else:
                res += enc[i]
                i += 1

    return res.capitalize()


def morse_encode(decoded: str):
    '''
    turn readable text into morse code
    decoded: string
    return morse coded string
    '''
    if not decoded:
        return

    decoded = decoded.upper()
    morse_code = {
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ',
        'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
        'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ', 'Q': '--.- ', 'R': '.-. ',
        'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
        'Y': '-.-- ', 'Z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ',
        '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ', ' ': '   ', '\n': ''
    }
    enc = ''.join([morse_code[i] for i in decoded])

    i = 0
    res = ''
    while i < len(enc):
        if enc[i:i+3] == '   ':
            res += '   '
            i += 3
        else:
            if enc[i] == ' ' and enc[i-1] == ' ':
                res += ''
                i += 1
            else:
                res += enc[i]
                i += 1

    return res


if __name__ == '__main__':
    fin_cod = open('cod.first.txt', 'r')
    fin = open('second.txt', 'r')
    fout_cod = open('first.txt', 'w')
    fout = open('cod.second.txt', 'w')

    while True:
        line = fin_cod.readline()

        if not line:
            break

        fout_cod.write(morse_decode(line))
        fout_cod.write('\n')

    fout_cod.close()

    while True:
        line = fin.readline()

        if not line:
            break

        morse_coded = morse_encode(line)
        fout.write(morse_coded)
        #print(morse_decode(morse_coded))
        fout.write('\n')

    fout.close()
