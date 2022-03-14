def swap_bits(x, i, j ):
    #if i and j are different they will swap
    if(x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (i << j)
        x ^= bit_mask
        #the book selects the bit to switch with bit_mask
        # since x^1 = 0 when x = 1 and 1 when x = 0 
        # using an XOR will 

    return x