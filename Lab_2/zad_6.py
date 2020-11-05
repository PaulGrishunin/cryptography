def DES(message, subkeys):
    
    perm_IP = permute(message, IP)
#     print('perm_IP=', perm_IP)
    
    feistel = Feistel(perm_IP, subkeys, F)
    
    perm_FP = permute(feistel, FP)
#     print('perm_FP=', perm_FP)
    
    return perm_FP
