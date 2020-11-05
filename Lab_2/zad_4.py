 
def Feistel(message, subkeys, F):
    
    encr_message = ''
    
    left = message[:32]
    right = message[32:]

#     print('left=', left)
#     print('right=', right)
 
    for i in range(len(subkeys)):
#         print(i)
        
#         print('sk=', subkeys[i])
        funF = F(right, subkeys[i])
#         print("funF=", funF)
       
        xor_funF = xor(left, funF)
#         print("xor_funF=", xor_funF)
        
        if i < 15:
            left = right
            right = xor_funF
#             print('left=', left)
#             print('right=', right)
        else:
            break
    
    encr_message = xor_funF + right
    print('encr_message=', encr_message)
    
    return encr_message
