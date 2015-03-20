import os

path = "dictionaries_and_flow/richness_fishbase_family.csv"
fishes = {}
f = open(path, "r")
#make a dictionary
for i, line in enumerate(f):
	#skip first line
	if (i == 0):
		continue
	else:
		list = line.split(",")
		fishes[list[0]] = list[1].strip("\n")
f.close()

#fn 1
def printFamilies(fishes, threshold):
	within = 0
	for key, value in fishes.iteritems():
		if (threshold < int(value)):
			#change within to 0 if there are families with species greater than threshold amt
			within = 1
			print("Family %s contains %s species" % (key, value))
		else:
			continue
	if (within == 0):
		print("No families have more than %d species" % threshold)

#fn 2
def printOneSpecies(fishes):
	for key, value in fishes.iteritems():
		if (int(value) == 1):
			print(key)

printFamilies(fishes, 10000)
printOneSpecies(fishes)