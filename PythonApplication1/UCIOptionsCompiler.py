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


def get_files(path):
	return [f for f in listdir(path) if isfile(join(path, f))]


def main():
	dir_path = 'c:/pet/engines/'
	all_files = get_files(dir_path)
	engines = [f for f in all_files if f.endswith('.exe')]

	print(f"found {len(engines)} engines")
	
	for e in engines:
		print(f"running {e}")
		engine_path = dir_path + e
		engine = chess.engine.SimpleEngine.popen_uci(engine_path)
		option_dic = engine.options
		
		for key, value in option_dic.items():
			print(f"{e} {key} {value}")
			

		# send text command to engine	
		
		engine.quit()

	assert(1==2), 'break'
	return
	

		
if __name__ == "__main__":
	main()


