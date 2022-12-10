"""--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?"""

# Solution

# change directory to this file's directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read input
with open('input.txt', 'r') as file:
	input = file.read().splitlines()

# import anytree
from anytree import Node, RenderTree

# create root node
root = Node('/')
root.size = 0

# set current node to root
current = root

# create nodes
for line in input:
	# split line into tokens
	tokens = line.split(' ')
	# if line is command
	if tokens[0] == '$':
		# if command is cd
		if tokens[1] == 'cd':
			# if argument is ..
			if tokens[2] == '..':
				# move up one level
				current = current.parent
			# if argument is /
			elif tokens[2] == '/':
				# move to root
				current = root
			# if argument is directory
			else:
				# move to directory
				# current = current.children[tokens[2]]
				# but children is a tuple and must use index
				# so we have to do this instead
				for child in current.children:
					if child.name == tokens[2]:
						current = child
						break
	# if line is directory
	elif tokens[0] == 'dir':
		# create directory and add to current node
		# current.children.append(Node(tokens[1]))
		# but children is a tuple and has no append method
		# so we have to do this instead
		current.children = current.children + (Node(tokens[1], size=0),)
	# if line is file
	else:
		# create file and add to current node
		file = Node(tokens[1], size=int(tokens[0]))
		# current.children.append(file)
		# but children is a tuple and has no append method
		# so we have to do this instead
		current.children = current.children + (file,)

# calculate total size of each node recursively
def calculate_total_size(node):
	# if node is directory
	if node.is_leaf == False:
		# for each child of node
		for child in node.children:
			# calculate child's total size
			calculate_total_size(child)
			# add child's total size to node's total size
			node.size += child.size

calculate_total_size(root)

# render tree
# for pre, fill, node in RenderTree(root):
# 	print("%s%s %s" % (pre, node.name, node.size if hasattr(node, 'size') else ''))

# find all directories with total size <= 100000
# and calculate sum of their total sizes
sum = 0
for pre, fill, node in RenderTree(root):
	# if node is directory
	if node.is_leaf == False:
		# if node has total size <= 100000
		if node.size <= 100000:
			# add node's total size to sum
			sum += node.size

# print sum
print(sum)