NAME = "Selection Sort"


def sort(l: list) -> list:
	len_l = len(l)
	for i in range(len_l - 1):
		idx, value = i, l[i]
		for j in range(i + 1, len_l):
			if l[j] < value:
				idx, value = j, l[j]
		if idx != i:
			l[i], l[idx] = l[idx], l[i]
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
