 
def permute(k,perm):
    
    res = ''
    for i in perm:
        res = res+k[i]
   
    return res



def xor(bin_str1, bin_str2):
    res =''
    n=0
   
    for i in bin_str1:
        
#         print("n1:", bin_str1[n])
#         print("n2:", bin_str2[n])
        if bin_str1[n] != bin_str2[n]:
            res = res + '1'
        else:
            res = res + '0'
            
        n+=1
    #print((res)    
    return res
