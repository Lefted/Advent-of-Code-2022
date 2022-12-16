from functools import cmp_to_key
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

# part 2


pairs = [i for pair in pairs for i in pair]

pairs.append("[[2]]")
pairs.append("[[6]]")


def compare_packets(left, right):
    if check_order(eval(left), eval(right)):
        return -1
    elif check_order(eval(right), eval(left)):
        return 1
    else:
        return 0


# sort packets using a custom comparator function usgin functools_cmp_to_key
packets = sorted(pairs, key=cmp_to_key(compare_packets))


divider_packets = []
for i in range(len(packets)):
    if packets[i] == "[[2]]" or packets[i] == "[[6]]":
        divider_packets.append(i+1)

print(divider_packets[0]*divider_packets[1])
