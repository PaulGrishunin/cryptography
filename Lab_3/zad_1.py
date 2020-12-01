def add_GF(p,q):
    add = str(bin(int(p, 2) ^ int(q, 2)))
#     print(add[2:])
    return add[2:]



def bin2hex(bin_str, pad):

    a = (int(bin_str, 2))
    b = hex(a)
    c = str(b[2:])
  
    if len(c)<pad:
        left = pad-len(c)
        c = left*"0" + c

    return c



