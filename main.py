#!/data/data/com.termux/files/usr/bin/python3

import os

reqpath = input("Enter your dir path: ")

if os.path.isfile(reqpath):
	print("The given path is a file ! Enter the dir path.")
else:
	allfds = os.listdir(reqpath)
	if len(allfds) == 0:
		print("This directory is empty !!!")
	else:
		reqex = input("Enter the extension of file as .py/.sh/.txt/.log: ")
		reqfiles = []
		for eachf in allfds:
			if eachf.endswith(reqex):
				reqfiles.append(eachf)
		if len(reqfiles) == 0:
			print(f"\nThere is no file with {reqex} extension on this path.\n")
		else:
			print("-"*50)
			print(f" {len(reqfiles)} files with {reqex} extension.")
			print("-"*50)
			print(f"And output is/are: \n{reqfiles}\n")

