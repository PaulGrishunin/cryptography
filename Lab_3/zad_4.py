def multiply_GF(p,q):
    
    m = multiply(p,q)
#     print("m=", m) 
    mult_gf = divide(multiply(p,q),"100011011")
   
#     print("mult_gf=", mult_gf) 
    return mult_gf[1]
