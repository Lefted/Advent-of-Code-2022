import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read input
with open('input.txt') as f:
	data = f.read()

# iterate over characters
for i in range(len(data)):
	# get current character
	current_character = data[i]

	# get previous 14 characters
	previous_characters = data[i - 14:i]

	# check if previous characters are all different
	if len(set(previous_characters)) == 14:
		# print result
		print(i)
		break



