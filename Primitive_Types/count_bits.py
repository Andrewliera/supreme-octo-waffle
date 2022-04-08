def counts_bits(x):
	num_bits = 0
	while x:
		num_bits += x&1
		x >>= 1
	return num_bits

<<<<<<< HEAD
x = 1234567890
=======
>>>>>>> refs/remotes/origin/master

print(counts_bits(x))
