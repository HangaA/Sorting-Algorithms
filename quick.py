from enum import Enum

NAME = "Quick Sort"


class PivotChoice(Enum):
	FIRST = 1
	LAST = 2
	MIDDLE = 3
	RANDOM = 4


def sort(l: list, start: int = 0, stop: int = None, pivot_choice: PivotChoice = PivotChoice.MIDDLE) -> list:
	stack = [('partition', start, stop)]

	while len(stack) > 0:
		current = stack.pop()
		if current[0] == 'partition':
			start, stop = current[1], current[2]
			if stop is None:
				stop = len(l)
			if start == stop or start == stop - 1:
				continue

			pivot_idx = 0
			if pivot_choice == PivotChoice.LAST:
				pivot_idx = stop - 1
			elif pivot_choice == PivotChoice.MIDDLE:
				pivot_idx = (stop - start - 1) // 2 + start
			elif pivot_choice == PivotChoice.RANDOM:
				import random
				pivot_idx = random.randrange(start, stop)

			l[pivot_idx], l[stop - 1] = l[stop - 1], l[pivot_idx]
			pivot_idx = stop - 1

			left = start
			right = pivot_idx - 1
			while left < right:
				while left < right and l[left] < l[pivot_idx]:
					left += 1

				while left < right and l[right] >= l[pivot_idx]:
					right -= 1

				if left >= right:
					break

				l[left], l[right] = l[right], l[left]

				left += 1
				right -= 1
			if l[left] < l[pivot_idx]:
				left += 1

			l[left], l[pivot_idx] = l[pivot_idx], l[left]
			right = left + 1
			
			# stack.append(('move pivot', pivot_idx))
			stack.append(('partition', right, stop))
			stack.append(('partition', start, left))
			continue
		if current[0] == 'move pivot':
			pivot_idx = current[1]

			while pivot_idx > 0 and l[pivot_idx - 1] >= l[pivot_idx]:
				l[pivot_idx], l[pivot_idx - 1] = l[pivot_idx - 1], l[pivot_idx]
				pivot_idx -= 1
			continue

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
