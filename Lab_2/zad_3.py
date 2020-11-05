 
def key_schedule(key):
    
    keylist =[]
    
    
    key56 = permute(key, PC1)
    print(key56)
    
    left_half = list(key56[:28])
    right_half = list(key56[28:])
    print(left_half)
    print(right_half)
        
    for i in range(len(shift_table)):
        print(i)
    
        left_half_shift = shift_left(left_half, shift_table[i])
#         print(left_half_shift)
        right_half_shift = shift_left(right_half, shift_table[i])
#         print(right_half_shift)
    
        lef=''.join(left_half_shift)
        rig=''.join(right_half_shift)
        m=lef+rig
#         print(m)
    
        key48 = permute(m, PC2)
        print(key48)
        
        keylist.append(key48)    
    print('keylist=', keylist)
    return keylist
