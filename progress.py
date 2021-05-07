class ProgressWriter:
	def __init__(self, count, width=10):
		self._count = count
		self._width = width
		self._last_print = ''
	
	def __enter__(self):
		self._done = 0
		self._comment = ""
		self._print()
		return self

	def __exit__(self, type, value, tb):
		print()

	def _print(self):
		print('\b'*len(self._last_print), end='')
		print(' '*len(self._last_print), end='')
		print('\b'*len(self._last_print), end='')
		to_print = '['
		filled = int((self._done / self._count) * self._width)
		to_print += '#' * filled
		to_print += ' ' * (self._width - filled)
		to_print += '] '
		percent = int((self._done / self._count) * 100)
		to_print += f'{percent}%'
		if self._comment:
			to_print += f' - {self._comment}'
		print(to_print, end='', flush=True)
		self._last_print = to_print

	def progress(self, comment=""):
		self._done += 1
		self._comment = comment
		self._print()
