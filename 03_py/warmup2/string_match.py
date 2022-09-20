def string_match(a,b):
	return sum([a[i:i+2]==b[i:i+2] for i in range(len(a)-1)])
