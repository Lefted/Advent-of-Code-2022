"""--- Day 8: Treetop Tree House ---
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390
Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
The top-middle 5 is visible from the top and right.
The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?"""

# Solution
# Change directory to this file's directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read input
with open('input.txt', 'r') as file:
    input = file.read().splitlines()

# Convert input to 2d array by splitting each line into a list of characters
input = [list(line) for line in input]

# Get dimensions of input
height = len(input)
width = len(input[0])

# add the 4 edges to the list of trees
numVisibleTrees = height * 2 + width * 2 - 4

# loop through each row but the first and last
for row in range(1, height - 1):
    # loop through each column but the first and last
    for col in range(1, width - 1):
        # get the height of the current tree
        tree_height = int(input[row][col])

        # loop through the trees in the row left of the current tree
        # if all of them are shorter than the current tree, the current tree is visible
        for i in range(col - 1, -1, -1):
            if int(input[row][i]) >= tree_height:
                break
        else:
            numVisibleTrees += 1
            continue

        # loop through the trees in the row right of the current tree
        # if all of them are shorter than the current tree, the current tree is visible
        for i in range(col + 1, width):
            if int(input[row][i]) >= tree_height:
                break
        else:
            numVisibleTrees += 1
            continue

        # loop through the trees in the column above the current tree
        # if all of them are shorter than the current tree, the current tree is visible
        for i in range(row - 1, -1, -1):
            if int(input[i][col]) >= tree_height:
                break
        else:
            numVisibleTrees += 1
            continue

        # loop through the trees in the column below the current tree
        # if all of them are shorter than the current tree, the current tree is visible
        for i in range(row + 1, height):
            if int(input[i][col]) >= tree_height:
                break
        else:
            numVisibleTrees += 1
            continue

# print the number of visible trees
print(numVisibleTrees)


"""--- Part Two ---
Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390
Looking up, its view is not blocked; it can see 1 tree (of height 3).
Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
Looking right, its view is not blocked; it can see 2 trees.
Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390
Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
Looking left, its view is not blocked; it can see 2 trees.
Looking down, its view is also not blocked; it can see 1 tree.
Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?"""

# Solution

max_scenic_score = 0

# loop through each row but the first and last
for row in range(1, height - 1):
	# loop through each column but the first and last
	for col in range(1, width - 1):
		# get the height of the current tree
		tree_height = int(input[row][col])
		
		# initialize the scenic score to 0
		scenic_score = 0

		# loop through the trees in the row left of the current tree
		scenic_score_left = 0
		for i in range(col - 1, -1, -1):
			# if this tree is smaller than the current tree, add 1 to the scenic score and continue; else add 1 to the scenic score and break
			if int(input[row][i]) < tree_height:
				scenic_score_left += 1
			else:
				scenic_score_left += 1
				break

		# loop through the trees in the row right of the current tree
		scenic_score_right = 0
		for i in range(col + 1, width):
			# if this tree is smaller than the current tree, add 1 to the scenic score and continue; else add 1 to the scenic score and break
			if int(input[row][i]) < tree_height:
				scenic_score_right += 1
			else:
				scenic_score_right += 1
				break

		# loop through the trees in the column above the current tree
		scenic_score_up = 0
		for i in range(row - 1, -1, -1):
			# if this tree is smaller than the current tree, add 1 to the scenic score and continue; else add 1 to the scenic score and break
			if int(input[i][col]) < tree_height:
				scenic_score_up += 1
			else:
				scenic_score_up += 1
				break

		# loop through the trees in the column below the current tree
		scenic_score_down = 0
		for i in range(row + 1, height):
			# if this tree is smaller than the current tree, add 1 to the scenic score and continue; else add 1 to the scenic score and break
			if int(input[i][col]) < tree_height:
				scenic_score_down += 1
			else:
				scenic_score_down += 1
				break

		# if the scenic score is greater than the max scenic score, set the max scenic score to the scenic score
		scenic_score = scenic_score_left * scenic_score_right * scenic_score_up * scenic_score_down
		if scenic_score > max_scenic_score:
			max_scenic_score = scenic_score
			pos_x, pos_y = col, row


# print the max scenic score
print(max_scenic_score)