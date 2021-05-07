#! /usr/bin/env python3

import random
from contextlib import ExitStack
import sys

import bubble
import heap
import insertion
import merge
import quick_all as qa
import selection

import text_result_writer
from progress import ProgressWriter

ALGORITHMS = [
	(qa.FIRST, 50_000), 
	(qa.LAST, 50_000), 
	(qa.MIDDLE, None), 
	(qa.RANDOM, None), 
	(heap, None), 
	(merge, None), 
	(bubble, 50_000), 
	(insertion, 50_000), 
	(selection, 50_000)
]
ITEM_COUNTS = [1000, 5000, 10_000, 50_000, 100_000, 500_000, 1_000_000]

def make_sorter(sort_fn, l: list):
	return lambda: sort_fn(l)

def time_sorter(sort_fn, l: list, repetitions=10000):
	import timeit
	return timeit.timeit(make_sorter(sort_fn, l), number=repetitions)

def calculate_repetitions(length):
	return 5
	# if length <= 5_000:
	# 	return 100
	# elif length <= 10_000:
	# 	return 50
	# elif length <= 100_000:
	# 	return 10
	# else:
	# 	return 5

seqs = []
if len(sys.argv) > 1:
	print("Reusing sequences from", sys.argv[1])
	with open(sys.argv[1], "r") as f:
		for line in f.readlines():
			if line.startswith('[SEQ]'):
				dot_idx = line.find('.')
				lst_str = line[dot_idx + 2:]
				import ast
				seq = ast.literal_eval(lst_str)
				seqs.append(seq)
	print("Read", len(seqs), "sequences")
else:
	seqs = [random.choices(range(10_000), k=count) for count in ITEM_COUNTS]

with text_result_writer.TextResultWriter("result.txt") as rw:
	for (algorithm, max_item_count) in ALGORITHMS:
		print(algorithm.NAME)
		with ExitStack() as es:
			allowed_seqs = [seq for seq in seqs if not max_item_count or len(seq) <= max_item_count]

			aw = es.enter_context(rw.algorithm(algorithm.NAME))
			pw = es.enter_context(ProgressWriter(len(allowed_seqs) * 3))

			for orig_seq in allowed_seqs:
				seq = orig_seq[:]
				repetitions = calculate_repetitions(len(seq))
				# Random
				time = time_sorter(algorithm.sort, seq, repetitions=repetitions)
				aw.record(len(seq), repetitions, time, 'random')

				pw.progress(f"{len(seq)} - random")
				# Sorted
				s = list(sorted(orig_seq))
				time = time_sorter(algorithm.sort, s, repetitions=repetitions)
				aw.record(len(s), repetitions, time, 'sorted')

				pw.progress(f"{len(s)} - sorted")
				# Reversed
				s = list(reversed(sorted(orig_seq)))
				time = time_sorter(algorithm.sort, s, repetitions=repetitions)
				aw.record(len(s), repetitions, time, 'reverse sorted')

				pw.progress(f"{len(s)} - reverse sorted")

	for seq in seqs:
		rw.register_sequence(seq)
