llst = ['a','ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
             'm', 'n', 'ń', 'o','ó', 'p', 'q','r', 's', 'ś', 't', 'u','v', 'w', 'x','y', 'z','ź','ż']
blst =  ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł',
             'M', 'N', 'Ń', 'O','Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']


def encryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x) % len(llst)
            #print("ind=", ind)
            ret += llst[(ind + shift) % len(llst)]
        elif x in blst:
            ind = blst.index(x) % len(llst)
            #print("ind=", ind)
            ret += blst[(ind + shift) % len(llst)]
        else:
            ret += x
    return ret


def decryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind - shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind - shift]
        else:
            ret += x
    return ret

#print(encryptCaesar('Dod pd 2 ńsyą.',-5)=='Ala ma 2 koty.')
print(decryptCaesar('Hćcrek okyź hćęy? Okzpń sńóź rsńk t źt sńk vcźę, ąńkr. Okzpń vcźęofhkrż żyńqżol ącźqżręhćci, sńk ąńkr.', 3))