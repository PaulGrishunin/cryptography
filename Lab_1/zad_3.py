
lalf = ['a','ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
             'm', 'n', 'ń', 'o','ó', 'p', 'q','r', 's', 'ś', 't', 'u','v', 'w', 'x','y', 'z','ź','ż']
ualf =  ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł',
             'M', 'N', 'Ń', 'O','Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']

czestotliwosc={'a':0.0891,'ą':0.0099, 'b':0.0147, 'c':0.0396, 'ć':0.004, 'd':0.0325, 'e':0.0766, 'ę':0.0111,
            'f':0.003, 'g':0.0142, 'h':0.0108, 'i':0.0821, 'j':0.0228, 'k':0.0351, 'l':0.021, 'ł':0.0182,'m':0.028,
            'n':0.0552, 'ń':0.002, 'o':0.0775,'ó':0.0085, 'p':0.0313, 'q':0.0014, 'r':0.0469, 's':0.0432,'ś':0.0066,
            't':0.0398, 'u':0.025, 'v': 0.0004, 'w':0.0465 ,'x':0.0002,'y':0.0376, 'z':0.0564,'ź':0.0006,'ż':0.0083}

def decryptCezar(msg, shift):
    ret = ""
    for x in msg:
        if x in lalf:
            ind = lalf.index(x)
            ret += lalf[ind - shift]
        elif x in ualf:
            ind = ualf.index(x)
            ret += ualf[ind - shift]
        else:
            ret += x
    return ret

plik=open('ksiazka1.txt')
ksiazka=plik.read()

count = {}                            #словарь { 'буква': кол-во повторений в тексте }
for character in ksiazka.lower():
    if character in lalf:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

print(count)

maxlit = max(count, key=count.get)    #получаем ключ с наибольшим значением
print(maxlit)

key1 = lalf.index(maxlit) - lalf.index('a')
key2 = lalf.index(maxlit) - lalf.index('i')

#print(decryptCezar(ksiazka, key1), "key=", key1)

#print(decryptCezar(ksiazka, key2), "key=", key2)

plik.close()