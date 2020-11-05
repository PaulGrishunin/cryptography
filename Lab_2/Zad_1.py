 
def bin2dec(bin_str):
    l = len(bin_str)
    dec = 0 
    for i in range(0, l):
        dec = dec + int(bin_str[i])*(2**(l-i-1))
 
    return dec

    
    
def dec2bin(dec_str,pad):
    n = int(dec_str)
    bina = ''
    
    while n > 0:
        bina = str(n%2) + bina
        n = n//2
        
    if len(bina)<pad:
        left = pad-len(bina)
        bina = left*"0" + bina
        
    return bina
    
    
    
def shift_left(tab,n):
    
    for i in range(n):
        tab.append(tab.pop(0))
   
    return tab    
    
    
    
