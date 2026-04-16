def generate_fibonacci_sequence(max_value):
	seq = []
	a,b =0,1

	while a <= max_value:
		seq.append(a)
		a, b = b, a + b

	return seq
