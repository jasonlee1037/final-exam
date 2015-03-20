import os

path = "dictionaries_and_flow/richness_fishbase_family.csv"
fishes = {}
f = open(path, "r")
for i, line in enumerate(f):
	if (i == 0):
		continue
	else:
		list = line.split(",")
		fishes[list[0]] = list[1]
f.close()

