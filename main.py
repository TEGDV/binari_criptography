#Cripto
def binari_convertion(decimal_number):

    binari_number = ''
    rest = decimal_number
    if decimal_number == 1:
        binari_number+='1'
    else:
        while rest > 0:
            if rest % 2 == 0:
                binari_number+='0'
            else:
                binari_number+='1'
            rest = int(rest/2)
    while len(binari_number)< 8:
        binari_number+='0'
    return binari_number[::-1]


if __name__ == "__main__":

    text_input = input('Write a text:   ').lower()
    binari_output = ''
    for letter in text_input:
        binari_output += ' ' + binari_convertion(ord(letter) - 96)
    print(binari_output)