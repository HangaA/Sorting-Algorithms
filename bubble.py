NAME = "Bubble Sort"


def sort(l: list) -> list:
	len_l = len(l)
	solved = False
	while not solved:
		solved = True
		for i in range(1, len_l):
			if l[i - 1] > l[i]:
				l[i - 1], l[i] = l[i], l[i - 1]
				solved = False
	return l


# Test
if __name__ == '__main__':
	print(NAME)
	
	import random
	# l = random.choices(range(1000), k=random.randint(10, 20))
	l = random.choices(range(30), k=random.randint(10, 20))

	print(l)

	l = sort(l)

	print(l)	
