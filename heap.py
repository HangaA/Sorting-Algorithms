NAME = "Heap Sort"


def heapify(l: list, root: int, until=None) -> list:
	"""
	Repairs zero-indexed heap in-place.
	Assumes that the heap is correct apart from the root.
	"""
	if until is None:
		until = len(l)

	left = root * 2 + 1
	right = root * 2 + 2
	largest = root

	if left < until and l[left] > l[largest]:
		largest = left
	if right < until and l[right] > l[largest]:
		largest = right

	if largest != root:
		l[root], l[largest] = l[largest], l[root]
		heapify(l, root=largest, until=until)

	return l


def sort(l: list) -> list:
	# Make heap
	for root in range((len(l) - 1) // 2, -1, -1):
		heapify(l, root)

	current_tail = len(l) - 1
	while current_tail != 0:
		l[0], l[current_tail] = l[current_tail], l[0]

		heapify(l, root=0, until=current_tail)

		current_tail -= 1

	return l


# Test
if __name__ == '__main__':
	print(NAME)
	
	import random
	l = random.choices(range(1000), k=random.randint(10, 20))

	print(l)

	l = sort(l)

	print(l)	
