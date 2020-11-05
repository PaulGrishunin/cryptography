lalf = ['a','ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
             'm', 'n', 'ń', 'o','ó', 'p', 'q','r', 's', 'ś', 't', 'u','v', 'w', 'x','y', 'z','ź','ż']
ualf = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł',
             'M', 'N', 'Ń', 'O','Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']


def Cezar(msg, shift):
    ret = ""
    for x in msg:
        if x in lalf:
            ind = lalf.index(x) % len(lalf)
            ret += lalf[(ind + shift) % len(lalf)]
        elif x in ualf:
            ind = ualf.index(x) % len(lalf)
            ret += ualf[(ind + shift) % len(lalf)]
        else:
            ret += x
    return ret


print(Cezar('Ala ma kota.',3)=='Cnc oc mqwc.')
print(Cezar('Ala ma kota.',20)=='Óżó ąó źćió.')
print(Cezar('Ala ma 2 koty.',5)=='Dod pd 2 ńsyą.')
print(Cezar('Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.',7)
                  =='Jęxkrsk eępk, vxuesc źxżj,\nGkćyńpsk ćqtxćkhćksńę!\nVxćkecźchn óyćźęqźuą eęjks hżj\nSńk ąxuhń jt ńyźsńksńę.')
print(Cezar('Cnc oc mqwc.',-3)=='Ala ma kota.')
print(Cezar('Óżó ąó źćió.',-20)=='Ala ma kota.')
print(Cezar('Dod pd 2 ńsyą.',-5)=='Ala ma 2 koty.')
print(Cezar('Jęxkrsk eępk, vxuesc źxżj,\nGkćyńpsk ćqtxćkhćksńę!\nVxćkecźchn óyćźęqźuą eęjks hżj\nSńk ąxuhń jt ńyźsńksńę.',-7)
                  =='Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.')