import glob
import os
import datetime
# part 1, open + read all .seq files
path = "fasta_problem"
name = []
length = []

def fastaConvert (path, name, length):
	for filename in glob.glob(os.path.join(path, '*.seq')):
		count = 0
		f = open(filename, "r")
		# part 2, single fasta-formatted file per individual file
		new_filename = filename.strip(".seq") + ".fas"
		new_file = open (new_filename,"w")
		for i, line in enumerate (f):
			if i == 0:
				new_file.write(line)
				#extract name for part 4
				name.append(line.strip(">").strip("\n"))
			#part 3
			else:
				new_file.write(line.lower())
				#get length of sequence
				count += len(line)
		length.append(count)
		new_file.close()
		f.close()


def logCreate (name, length):
	#part 4 make log file
	log_name = "log.txt"
	f = open(log_name, "w")
	f.write("sequence_name,length\n")
	for i in range(10):
		f.write(name[i] + "," + str(length[i]) + "\n")
	#part 5 date and time
	current_time = datetime.datetime.now()
	f.write(str(current_time))

fastaConvert(path, name, length)
logCreate(name, length)