lalf = ['a','ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
             'm', 'n', 'ń', 'o','ó', 'p', 'q','r', 's', 'ś', 't', 'u','v', 'w', 'x','y', 'z','ź','ż']
ualf =  ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł',
             'M', 'N', 'Ń', 'O','Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']

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

for i in range(1, len(lalf)):
    print("key=",i, decryptCezar('Hćcrek okyź hćęy? Okzpń sńóź rsńk t źt sńk vcźę, ąńkr. Okzpń vcźęofhkrż żyńqżol ącźqżręhćci, sńk ąńkr.', i))
