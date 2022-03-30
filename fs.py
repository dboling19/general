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
	# rip the filename apart into two pieces to preserve the ext
	# we don't use prefix
	name = [new_name, '_0{0}'.format(str(count)), ext]
	# build a list of filename attributes
	name = ''.join(name)
	# join all attributes together to make a cohesive filename
	if name in os.listdir():
		# if the filename already exists, ignore/skip it
		# this allows rerunning the script periodically and not affecting old files
		skipped += 1
		continue
	else:
		renamed += 1
		os.rename(i, name)
		# rename each file in the loop with the generated filename

print('Renamed: {0}/{2}; Skipped: {1}/{2}'.format(renamed, skipped, count))