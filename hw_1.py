import glob
import os
# part 1, open + read all .seq files
path = "fasta_problem"
for filename in glob.glob(os.path.join(path, '*.seq')):
	f = open(filename, "r")
	# part 2, single fasta-formatted file per individual file
	new_filename = filename.strip(".seq") + ".fas"
	new_file = open (new_filename,"w")
	for i, line in enumerate (f):
		if i == 0:
			new_file.write(line)
		#part 3
		else:
			new_file.write(line.lower())
	new_file.close()
	f.close()

