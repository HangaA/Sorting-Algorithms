#! /usr/bin/env python3

import random
import sys
import os

def argv_param():
	for arg in sys.argv:
		if '=' in arg:
			yield tuple(arg.split('=', maxsplit=1))
argv_param = {k.upper():v for k,v in argv_param()}

def find_or_query(arg: str, query=None):
	if query is None:
		query = arg
	arg = arg.upper().replace(' ', '_')

	if arg in argv_param:
		return argv_param[arg]
	
	if arg in os.environ:
		return argv_param[arg]
	
	return input(f"{query}: ")


filename = find_or_query("Filename")
item_count = int(find_or_query("Item count"))

seq = random.choices(range(1000), k=item_count)

with open(filename, "w") as f:
	for item in seq:
		print(item, file=f)
