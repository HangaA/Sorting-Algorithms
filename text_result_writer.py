class TextResultWriter:
	def __init__(self, filename) -> None:
		self._file = open(filename, "w")
		self._seq_idx = 0
	
	def close(self):
		self._file.close()

	def __enter__(self):
		return self

	def __exit__(self, type, value, tb):
		self.close()

	def register_sequence(self, seq):
		print(f"[SEQ] {self._seq_idx + 1}. {seq}", file=self._file)
		self._seq_idx += 1
	
	def algorithm(self, name):
		class AlgorithmResultWriter:
			def __init__(self, file, name):
				self._file = file
				self._idx = 0
				print(f"{name}:", file=self._file)

			def record(self, elem_count: int, repetitions: int, time: float, type: str):
				print(f"  {self._idx + 1}. Cnt: {elem_count} | Rep: {repetitions} | Type: {type} | Time: {time}", file=self._file)
				self._idx += 1

			def __enter__(self):
				return self

			def __exit__(self, type, value, tb):
				print(file=self._file, flush=True)
	
		return AlgorithmResultWriter(self._file, name)