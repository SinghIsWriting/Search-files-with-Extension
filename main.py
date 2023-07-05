import os    # importing os module to deal with directories and files

path = input("Your directory path(press enter for current directory): ")

if path == "":
	path = os.getcwd()

# checking if given path is a file
if os.path.isfile(path):
	print("The given path is a file ! Enter the path of any directory.")
else:
	# listing all files in this path
	allFiles = os.listdir(path)

	if len(allFiles) == 0:
		print("This directory is empty !!!")
	else:
		# taking input extension of file that you want to get
		extensionOfFile = input("Enter the extension of output files(.txt/.py/.html): ")
		outputFiles = []
		for file in allFiles:
			if file.endswith(extensionOfFile):
				outputFiles.append(file)
		if len(outputFiles) == 0:
			print(f"\nThere is no file with {extensionOfFile} extension on this path.\n")
		else:
			print("-"*50)
			print(f" {len(outputFiles)} file(s) with .{extensionOfFile} extension.")
			print("-"*50)
			print(f"And output files is/are: \n{outputFiles}\n")

