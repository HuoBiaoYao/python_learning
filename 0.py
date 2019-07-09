import csv

from matplotlib import pyplot as plt

filename = 'Soil_vwc.DAT'

try:
	with open(filename) as f_obj:
		reader = csv.reader(f_obj)
		header_row= next(reader)
		
		for index,column_header in enumerate(header_row):
			print(index,column_header)
			
		records = []
		datetimes = []
		for row in reader:
			records.append(row[0])
			datetimes.append(row[1])
		
	with open(filename) as f_obj:
		contents = f_obj.read()
	with open(filename) as f_obj:
		lines = f_obj.readlines()
		print("The file " + filename + " has about " + (str)(len(lines)) + " lines.")
except FileNotFoundError as e:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")
	
	fig = plt.figure(dpi=128,figsize=(10,6))
	plt.plot(records,c='red')
	plt.title("test")
	plt.xlabel('',fontsize=16)
	plt.ylabel("the number of record",fontsize=16)
	plt.tick_params(axis='both',which='major',labelsize=16)
	
	plt.show()
