 
def divide(p,q):
    q1 = q
    s = ''
    while len(p)>=len(q):
 
        while len(q)<len(p):
            q = q +'0'
#         print("q=", q)   
    
        p = add_GF(p,q)
#         print("p=", p)   
        s = s + "1"
        q = q1
    if p == "1" and q[-1] == "1":
        s = s+"0"

    return s, p


