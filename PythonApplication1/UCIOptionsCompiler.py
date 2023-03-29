from importlib.metadata import files
import sys
import random
import os.path
import shutil
import time

import numpy as np
from datetime import datetime

import chess
import chess.engine
import chess.pgn

import subprocess
import os

from shutil import copyfile

from os import listdir
from os.path import isfile, join

def delete_file(path):
	try:
		os.remove(path)
	except OSError:
		pass

def FileExists(f):
	return isfile(f)



# scan directory and sub directories to find files
# return list of files
def get_files(path):
    # r=root, d=directories, f = files
	files = []
	for (r, d, f) in os.walk(path):
		for file in f:
			if '.exe' in file:
				files.append(os.path.join(r, file))
	return files



def main():
	dir_path = 'c:/pet/engines/'
	all_files = get_files(dir_path)
	engines = [f for f in all_files if f.endswith('.exe')]

	print(f"found {len(engines)} engines")

	all_engines = []
	all_options = []
	for e in engines:
		print(e)
	

	# some engines just decline to cooperate (or they are not Uci), so put the name manually in the dud_engines list
	# there may also be exe's that aren't actually chess engines, use the dud_engine list for them too
	dud_engines = ['arasan17', 'ccc', 'chess_5_1_10', 'chess_5_1_11', 'chess_5_1_12',
				'chess_5_1_13', 'chess_5_1_14', 'chess_5_1_4', 'chess_5_1_5', 'chess_5_1_6', 'chess_5_1_7',
				'chess_5_1_8', 'chess_5_1_9', 'chess_5_2_1', 'chess_5_2_2', 
				'chess_5_2_3', 'chess_5_2_4', 'chess_5_2_5', 'chess_5_2_6', 'counter_4.0', 'mea', 'polyglot',
				'tscp181', 'unins000', 'vcredist_x64', 'wb2uci', 'wait', 'client', 'lc0-training-client',
				'pigeon-1.5.1', 'slow64-sse']
	for e in engines:
		if '\\' in e:
			e = e.replace('\\', '/')

		name = e[:-4].split('/')[-1].lower()
		if name in dud_engines:
			continue

		# skip some engines that are not UCI, or on personal grounds(!)
		if 'tal' in name and 'system' in name:
			continue
		if 'corona' in name:
			continue
		if 'crafty' in name:
			continue
		if 'cutechess' in name:
			continue
		if 'slow' in name:
			continue

		option_dic = {}
		print()
		print(f"trying {name}")
		
		try:
			engine = chess.engine.SimpleEngine.popen_uci(e)
		except ValueError:
			print(f"{name} failed to open")
			continue
		try:
			option_dic = engine.options
		except ValueError:
			print(f"{name} failed to get options")
			continue

		for key, value in option_dic.items():
			print(f"{name} {key}")
			all_options.append(key)

		all_engines.append(name)	

		engine.quit()

	def countItemInList():
		# count the number of times each item appears in the list
		# return a dictionary of item:count
		count = {}
		for item in all_options:
			if item in count:
				count[item] += 1
			else:
				count[item] = 1
		return count

	def sortDictbyValue(dict):
		# sort a dictionary by value
		# return a list of tuples
		return sorted(dict.items(), key=lambda x: x[1], reverse=True)


	count_dict = countItemInList()
	sorted_count = sortDictbyValue(count_dict)

	for key, value in sorted_count:
		print(key, value)

	sortedoptions = sorted(all_options)
	uniqueoptions = list(set(all_options))

	print(f"found {len(uniqueoptions)} unique options")
	print(f"found {len(all_engines)} unique engines")
	for o in sortedoptions:
		print(o)

	assert(1==2), 'break'
	return
	

		
if __name__ == "__main__":
	main()


