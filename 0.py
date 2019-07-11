import csv
import os
import re

from matplotlib import pyplot as plt
from datetime import datetime

time = '2019-07'
filename = 'Soil_vwc.DAT'
new_filename = 'Soil_vwc_' + time +'.DAT'

def Split():
	try:
		with open(filename) as f_obj:
			lines = f_obj.readlines()
		# ~ with open(filename) as f_obj:
			# ~ contents = f_obj.read()
	except FileNotFoundError as e:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		# ~ words = contents.split()
		# ~ num_words = len(words)
		print("原文件 " + filename + " 中包含 " + (str)(len(lines)) + " 行(包括表定义行).")
		#筛选出相应月份的数据
		new_lines = []
		new_lines.append(lines[0])
		for line in lines:
			if time in line:
				new_lines.append(line)
		#利用set删除重复项
		new_lines = sorted(set(new_lines),key=new_lines.index)
		#创建新文件，写入筛选后的内容		
		new_file = open(new_filename,'w') 
		for line in new_lines:
			new_file.write(line)
		new_file.close()
			
		print("新文件 " + new_filename + " 中包含 " + (str)(len(new_lines)) + " 行(包括表定义行).")
		 
		with open(new_filename) as new_f_obj:
			reader = csv.reader(new_f_obj)
			header_row= next(reader)
			# ~ for index,column_header in enumerate(header_row):
				# ~ print(index,column_header)
			records = []
			datetimes = []
			for row in reader:
				current_datetime = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
				datetimes.append(current_datetime)
				records.append(row[0])
		
		# ~ fig = plt.figure(dpi=128, figsize=(10,6))
		# ~ plt.plot(records, c='red')
		# ~ plt.title("test", fontsize=16)
		# ~ plt.xlabel('', fontsize=16)
		# ~ plt.ylabel("number of record", fontsize=16)
		# ~ plt.tick_params(axis='both', which='major', labelsize=16)
		
		# ~ plt.show()
		
if __name__ == "__main__":
	try:
		os.chdir(r'ygs')
	except FileNotFoundError:
		msg = "未发现ygs文件夹，请在本程序根目录下创建ygs文件夹，并将遥感所所有的站点数据文件夹拷贝到该目录下."
		print(msg)
	else:	
		current_path = os.getcwd()
		file_paths = os.listdir()
		for file_path in file_paths:
			os.chdir(file_path)
			print("进入 " + file_path)
			Split()
			os.chdir(current_path)
