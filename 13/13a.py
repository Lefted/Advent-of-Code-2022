import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("input.py") as f:
    input = f.read().split("\n\n")

pairs = [i.splitlines() for i in input]


def check_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            result = check_order(left[i], right[i])
            if result is not None:
                return result
        if len(left) == len(right):
            return None
        return len(left) < len(right)
    elif isinstance(left, int):
        return check_order([left], right)
    elif isinstance(right, int):
        return check_order(left, [right])


def check_pair(pair):
    left = eval(pair[0])
    right = eval(pair[1])
    if not check_order(left, right):
        return False
    return True


sum_indices = 0
for i in range(len(pairs)):
    if check_pair(pairs[i]):
        sum_indices += i+1

print(sum_indices)


# tests
assert(check_pair(["[1,1,3,1,1]", "[1,1,5,1,1]"]))
assert(check_pair(["[[1],[2,3,4]]", "[[1],4]"]))
assert(not check_pair(["[9]", "[[8,7,6]]"]))
assert(check_pair(["[[4,4],4,4]", "[[4,4],4,4,4]"]))
assert(not check_pair(["[7,7,7,7]", "[7,7,7]"]))
assert(check_pair(["[]", "[3]"]))
assert(not check_pair(["[[[]]]", "[[]]"]))
assert(not check_pair(
    ["[1,[2,[3,[4,[5,6,7]]]],8,9]", "[1,[2,[3,[4,[5,6,0]]]],8,9]"]))
