# in this solution we are supposed to assume there is a precomputed parity cache
# assume the cache is a 16 bit cache.
# the book explains that 2^16 makes using an array achievable 
# 16 bits also makes it easier to deal with 64 bit words since it divides evenly.

def parityThree(x): 
    MASK_SIZE = 16 # 16 bits 
    BIT_MASK = 0xFFFF # 16 1's with the bit mask parity & bitmask will remove the unwanted bits after shifting 
    return(PRECOMPUTED_PARITY[ x >> (3 * MASK_SIZE)] # leftmost 16 bits are shifted to the right
        ^ PRECOMPUTED_PARITY[( x >> (2 * MASK_SIZE)) & BIT_MASK] # xor next set then & with bit_mask
        ^ PRECOMPUTED_PARITY[ (x >> MASK_SIZE) & BIT_MASK]#  xor then & again
        ^ PRECOMPUTED_PARITY[x & BIT_MASK]) # 
        