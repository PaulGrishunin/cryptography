 
img_enc=Image.open('img_enc.png')
arr=np.array(img_enc).ravel()
arr_bin=[dec2bin(d,pad=8) for d in arr]
bits=''.join(arr_bin)
img_enc
# print("bits=", bits)
 
 
key = '1010101010111011000010010001100000100111001101101100110011011101'


blocks = [bits[i:i+64] for i in range(0, len(bits), 64)]
# print("length blocks=", len(blocks))

img_t=''
for block in range(0, len(blocks)):
#     print('block=', blocks[block])
    
    decrypt_block = DES(blocks[block], subkeys[::-1])
#     print('decrypt_block=', decrypt_block)
    
    img_t = img_t + decrypt_block
    
#print("img_t=", img_t) 

def split_img(message, n):
    
    spl = [message[i:i+n] for i in range(0, len(message), n)]
    print("spl=", spl)
    return spl

# print(split_img('1100000010110111101010001101000001011111001110101000001010011100', 8)
    

# #img_t to ciąg stringów powstałych z odszyfrowania DES-em
img=np.array([bin2dec(b) for b in split_img(img_t,8)]).reshape(np.array(img_enc).shape)
Image.fromarray(np.uint8(np.array(img)))
