def counts_bits(x):
	num_bits = 0
	while x:
		num_bits += x&1
		x >>= 1
	return num_bits


print(counts_bits(x))
