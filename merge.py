NAME = "Merge Sort"


def sort(l: list) -> list:
	if len(l) < 2:
		return l
	
	mid_len = len(l) // 2
	first_sorted = sort(l[:mid_len])
	second_sorted = sort(l[mid_len:])
	result = []
	first_idx = 0
	second_idx = 0
	first_len = len(first_sorted)
	second_len = len(second_sorted)

	while first_idx != first_len and second_idx != second_len:
		if first_sorted[first_idx] < second_sorted[second_idx]:
			result.append(first_sorted[first_idx])
			first_idx += 1
		else:
			result.append(second_sorted[second_idx])
			second_idx += 1
	
	while first_idx != first_len:
		result.append(first_sorted[first_idx])
		first_idx += 1
	
	while second_idx != second_len:
		result.append(second_sorted[second_idx])
		second_idx += 1
	
	return result
	
