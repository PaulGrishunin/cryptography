def multiply(p,q):
    a='0'
#     l=[]
    
    for i,b in enumerate(p[::-1]):
        if b=='1':
            a=add_GF(a,q+i*'0')

    return a 



