import os

new_name = "wallpaper"
directory = "C:\\Users\\Daniel Boling\\Pictures\\Wallpapers"

count = 0
skipped = 0
renamed = 0

os.chdir(directory)

count = 0

for i in os.listdir():
	count += 1
	prefix, ext = os.path.splitext(i)
	name = [new_name, '_0{0}'.format(str(count)), ext]
	name = ''.join(name)
	if name in os.listdir():
		continue
	else:
		os.rename(i, name)
