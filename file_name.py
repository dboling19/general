import os, shutil

extend = input('Extension: ')
new_name = input('File name(s): ')
direct = input('Directory: ')

count = 0

os.chdir(direct)

for j in os.listdir():
	count += 1

for i in os.listdir():
	prefix, ext = os.path.splitext(i)
	name = [new_name, '(0{0})'.format(str(count)), extend]
	name = ''.join(name)
	os.rename(i, name)