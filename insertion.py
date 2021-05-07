NAME = "Insertion Sort"


def sort(l: list) -> list:
	for i in range(1, len(l)):
		for j in range(i - 1, -1, -1):
			if l[j] > l[j + 1]:
				l[j], l[j + 1] = l[j + 1], l[j]
			else:
				break
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
