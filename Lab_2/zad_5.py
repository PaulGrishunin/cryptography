 
def F(right, subkey):
    
    perm_E = permute(right, E)
#     print("perm_E:", perm_E)
    
    xor_perm_E = xor(perm_E, subkey)
#     print("xor_perm_E:", xor_perm_E)
    
    groups = [xor_perm_E[i:i+6] for i in range(0, len(xor_perm_E), 6)]
#     print("groups=", groups)
    
    afterSBox = ''
    for g in range(0, len(groups)):

#         print("cicle=", g)
#         print("group=", groups[g])
        
        wiersz = bin2dec(groups[g][0]+groups[g][5])
#         print('wiersz=', wiersz)
        
        kolumna = bin2dec(groups[g][1]+groups[g][2]+groups[g][3]+groups[g][4])
#         print('kolumna=', kolumna)
        
        
        elem = SBox[g][wiersz][kolumna]
#         print('elem=', elem)
        
        fourbits = dec2bin(elem,4)
#         print('fourbits=', fourbits)
        
        afterSBox = afterSBox + fourbits
     
#     print('afterSBox=', afterSBox)
    
    return permute(afterSBox, P)
