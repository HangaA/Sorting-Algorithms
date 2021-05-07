import quick

class QuickFirst:
	NAME = "Quick Sort - Pivot: First"

	def sort(self, l: list) -> list:
		return quick.sort(l, pivot_choice=quick.PivotChoice.FIRST)


class QuickLast:
	NAME = "Quick Sort - Pivot: Last"

	def sort(self, l: list) -> list:
		return quick.sort(l, pivot_choice=quick.PivotChoice.LAST)


class QuickMiddle:
	NAME = "Quick Sort - Pivot: Middle"

	def sort(self, l: list) -> list:
		return quick.sort(l, pivot_choice=quick.PivotChoice.MIDDLE)


class QuickRandom:
	NAME = "Quick Sort - Pivot: Random"

	def sort(self, l: list) -> list:
		return quick.sort(l, pivot_choice=quick.PivotChoice.RANDOM)


FIRST = QuickFirst()
LAST = QuickLast()
MIDDLE = QuickMiddle()
RANDOM = QuickRandom()
