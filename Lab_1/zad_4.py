alfabet = u"aąbcćdeęfghijklłmnoópqrsśtuvwxyzźżAĄBCĆDEĘFGHIJKLŁMNOÓPRSŚTUVWXYZŹŻ0123456789"

d = { 4: 'A', 5: 'Ą', 6: 'B', 7: 'C', 8: 'Ć', 9: 'D', 10: 'E', 11: 'Ę', 12: 'F', 13: 'G', 14: 'H', 15: 'I', 16: 'J', 17: 'K', 18: 'L', 19: 'Ł',
             20: 'M', 21: 'N', 22:'Ń', 23: 'O', 24: 'Ó', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'Ś', 30: 'T', 31: 'U', 32: 'V', 33: 'W', 34: 'X', 35: 'Y', 36: 'Z', 37: 'Ź', 38: 'Ż',
            39: 'a', 40: 'ą', 41: 'b', 42: 'c', 43: 'ć', 44:'d', 45: 'e', 46: 'ę', 47: 'f', 48: 'g', 49: 'h', 50: 'i', 51: 'j', 52: 'k', 53: 'l', 54:'ł',
   55: 'm', 56: 'n', 57: 'ń', 58: 'o', 59: 'ó', 60: 'p', 61: 'q', 62: 'r', 63: 's', 64: 'ś', 65: 't', 66: 'u', 67: 'v', 68: 'w', 69: 'x', 70: 'y', 71: 'z', 72: 'ź', 73: 'ż'}


# кодируем слова в буквы
def encode_val(word):
    list_code = []
    lent = len(word)

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
                list_code.append(value)
                print("list_code:", list_code)
    return list_code


# компаратор 2-х списков
def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0
    for i in value:
        dic[full] = [i, key[iter]]
        full = full + 1
        iter = iter + 1
        if (iter >= len_key):
            iter = 0
    print("dic:", dic)
    return dic


# finish full encode
def full_encode(value, key):
    dic = comparator(value, key)
    print('Compare full encode', dic)

    lis = []

    for v in dic:
        go = (dic[v][0] + dic[v][1]) % len(d)
        lis.append(go)
    return lis


##### DECODER

# decode to numeric values
def full_decode(value, key):
    dic = comparator(value, key)

    print('Deshifre=', dic)

    lis = []
    for v in dic:
        go = (dic[v][0] - dic[v][1] + len(d)) % len(d)
        lis.append(go)
    return lis


def decode_val(list_in):
    list_code = []
    lent = len(list_in)

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
                list_code.append(d[value])
    return list_code


if __name__ == "__main__":
    word = 'Ala ma kota.'
    key = 'ela'

    print('Слово ', word)
    print('', key)
    # Закодировали буквы в цифры
    key_encoded = encode_val(key)
    value_encoded = encode_val(word)

    print('Value=', value_encoded)
    print('Key=', key_encoded)

    # сдвигаем
    shifre = full_encode(value_encoded, key_encoded)
    print('Шифр=', ''.join(decode_val(shifre)))

    decoded = full_decode(shifre, key_encoded)
    print('Decode list=', decoded)
    decode_word_list = decode_val(decoded)
    print('Word=', ''.join(decode_word_list))