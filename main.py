def dot_to_dec(addr_tup):
    num = 0                          
    muls = (16777216,65536,256,1)
    for i in range(len(addr_tup)):
        num += addr_tup[i] * muls[i]
    return num

def dec_to_dot(num):
    bin_num = bin(num)[2:].zfill(32)
    return tuple((int(bin_num[x:x+8], 2)) for x in (0,8,16,24))

