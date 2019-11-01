import csv
import os
import re

from matplotlib import pyplot as plt
from datetime import datetime

time = '2019-10'

def Split(filelist):
	for filename in filelist:
		try:
			with open(filename) as f_obj:
				lines = f_obj.readlines()
		except FileNotFoundError as e:
			msg = "Sorry,there is no file here"
			print(msg)
		else:
			print("原文件 " + filename + " 中包含 " +
				  (str)(len(lines)) + " 行(包括表定义行)")
			# 筛选出相应月份的数据
			new_lines = []
			new_lines.append(lines[0])
			for line in lines:
				if time in line:
					new_lines.append(line)
			# 利用set删除重复项
			new_lines = sorted(set(new_lines), key=new_lines.index)
			# 创建新文件，写入筛选后的内容
			new_filename = filename[0:-4] + '_' + time + '.DAT'
			new_file = open(new_filename, 'w')
			for line in new_lines:
				new_file.write(line)
			new_file.close()
			print("新文件 " + new_filename + " 中包含 " +
				  (str)(len(new_lines)) + " 行(包括表定义行).")
			with open(new_filename) as new_f_obj:
				reader = csv.reader(new_f_obj)
				header_row = next(reader)
				records = []
				datetimes = []
				for row in reader:
					current_datetime = datetime.strptime(
						row[1], "%Y-%m-%d %H:%M:%S")
					datetimes.append(current_datetime)
					records.append(row[0])


if __name__ == "__main__":
	try:
		os.chdir('ygs')
	except FileNotFoundError:
		print(root_dir)
		print("未发现ygs文件夹，请在本程序根目录下创建ygs文件夹，并将遥感所所有的站点数据文件夹拷贝到该目录下")
	else:
		root_dir = os.getcwd()
		file_paths = os.listdir()
		for path in file_paths:
			if os.path.isdir(path):
				print(path + " is a directory")
				os.chdir(path)
				file_path = root_dir + '\\' + path
				print("进入 " + file_path)
				fileList = os.listdir(file_path)
				print(fileList)
				Split(fileList)
				os.chdir(root_dir)
			elif os.path.isfile(path):
				print(path + " is a normal file")
			else:
				print(path + " is a special file(socket,FIFO,device file)")
			
