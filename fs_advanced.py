from operator import truediv
import os, shutil, sys


def display_help():
	# print a help message
	# this will run by either running file_mgr.py with no args, or the help operation is specified.
	print(
"""
Usage: file_mgr.py <operation> [...]
-f  --filename <filename>		Specify the filename
-d  --directory <directory>		Specify the directory to look/run in
-h  --help						Prints this message

A filename is required.
If no directory is specified, directory will default to the cwd.

Ex: file_mgr.py --file-name "wallpaper_" --directory "~/Pictures/Wallpapers"
Ex: file_mgr.py -f "wallpaper_" -d "~/Pictures/Wallpapers"
""")
# use a multi-line comment to format help messages


def manage_vars():
	for i in sys.argv:
		if i == '-f' or i == '--filename':
			if sys.argv[sys.argv.index(i)+1] == '-d' or sys.argv[sys.argv.index(i)+1] == '--directory':
				display_help()
				sys.exit()
			else:
				try: 
					filename = sys.argv[sys.argv.index(i)+1]
				except IndexError:
					display_help()
					sys.exit()
		elif i == '-d' or i == '--directory':
			directory = sys.argv[sys.argv.index(i)+1]
		else:
			continue
		# loop through the args list and set options.
		# when reaching end of list, continue.

	if not filename:
		# if no filename specified, display help and exit
		display_help()
		sys.exit()

	return filename, directory


def main():
	filename, directory = manage_vars()
	count = 0
	renamed = 0
	skipped = 0
	
	if directory:
		os.chdir(directory)
	else:
		cwd = os.getcwd()
		print('No directory specified. Script will run in {0}'.format(cwd))

	files = os.listdir()
	prefix_files = []
	for f in files:
		prefix, ext = os.path.splitext(f)
		prefix_files.append(prefix)
	# stores entire folder array
	for i in files:
		count += 1
		prefix, ext = os.path.splitext(i)
		# rip the filename apart into two pieces to preserve the ext
		# we don't use prefix
		name = [filename, '_0{0}'.format(str(count)), ext]
		# build a list of filename attributes
		name = ''.join(name)
		# join all attributes together to make a cohesive filename
		if name[:name.index('.')] in prefix_files:
			# if the filename already exists, ignore/skip it
			# this allows rerunning the script periodically and not affecting old files
			skipped += 1
			continue
		else:
			renamed += 1
			os.rename(i, name)
			# rename each file in the loop with the generated filename

	print('Renamed: {0}/{2}; Skipped: {1}/{2}'.format(renamed, skipped, count))


main()
