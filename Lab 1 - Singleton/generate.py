# A simple test case generator for CSC 349 at Cal Poly
# Outputs a file with a list of duplicates, except for one unique element
# Credit: Rodrigo Canaan

import random
import datetime
import os.path
from os import path

# Parameters for the generator

def generate():
	min = -1000
	max = 1000
	n = 50

	while True:
		# Generate a random list of distinct numbers
		numbers = random.sample(range(min,max),n)

		# Add singleton of the first number to the final list
		unique = numbers[0]

		fileName = "unique{}".format(unique)

		if not os.path.isfile(fileName):
			L = [unique]

			# Add duplicates of the remaining entries, then sort
			for n in numbers[1:]:
				L.append(n)
				L.append(n)
			L.sort()

			with open(fileName,"x") as f:
				for n in L:
					f.write("{}\n".format(n))

			f.close()

			return fileName

