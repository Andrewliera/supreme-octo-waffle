#write a program that takes a 64 bit unsigned int 
# and returns a 64 bit unsigned int with the bits in reversed order
# 4 bit ex
# input -> (1101) 	output -> (1011)
# 
# in the function,
#  extract least significant bit 
#  left shift position by one
#  or value with a var to add to it  
#  
#  the book uses a cache to solve this problem
#  
#   ill be refering to P&P programming EPI 4.3 walkthrough for the first function
#   his explenation and implementation were really good in the youtube video.
#
#
#                  most sig.                           least significant
#                      [4]        [3]        [2]          [1]
#   [64-bit int]    [16-bit]   [16-bit]    [16-bit]    [16 bit]
#    bit order          <-        <-          <-           <-
#----------------------function-----------------------
#                      [1]        [2]         [3]       
#[reverse-bit cache]  [16-bit]   [16-bit]    [16-bit]    [16 bit]
#    bit order          ->        ->           ->        ->
#   
#   [in]        10 11 00 01
#   [out]       10 00 11 01 
# 
# 

CACHE = []  
def build_rev_cache():
    for x in range (0, 2**16):
        CACHE.append(reverse_bits(x)) #add value of reversed bit to cache 

def reverse_bits(x):
    build_rev_cache()
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF #16 bits in hex
    
    return (CACHE[x & BIT_MASK] << (3 * MASK_SIZE) | 
    CACHE[(X >> MASK_SIZE) & BIT_MASK] << (2* MASK_SIZE) |
    CACHE[(x >> (2 * MASK_SIZE))& BIT_MASK]  << (MASK_SIZE) |
    CACHE[(x >> (3 * MASK_SIZE)) & BIT_MASK])





