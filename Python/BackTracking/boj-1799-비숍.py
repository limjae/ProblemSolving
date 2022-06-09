import sys
from collections import defaultdict
class Solution:
    max_odd = 0
    max_even = 0
    def __init__(self):
        map_size = int(sys.stdin.readline())
        odd_range = map_size - 1 if map_size % 2 == 0 else map_size
        even_range = map_size - 1
        odd_set = set()
        even_set = set()

        available_dict = defaultdict(set)

        for y in range(map_size):
            data = list(map(int, sys.stdin.readline().split()))
            for x, value in enumerate(data):
                if value == 1:
                    available_dict[y+x].add((y, x))

        def DFS_odd(cur_index):
            if cur_index == odd_range+1:
                self.max_odd = max(self.max_odd, len(odd_set))
                return None
            else:
                for next_set in available_dict[2 * cur_index]:
                    is_valid = True
                    for check_y, check_x in odd_set:
                        if abs(check_y - next_set[0]) == abs(check_x - next_set[1]):
                            is_valid = False
                            break
                    if is_valid:
                        odd_set.add(next_set)
                        DFS_odd(cur_index + 1)
                        odd_set.remove(next_set)
                DFS_odd(cur_index + 1)

        def DFS_even(cur_index2):
            if cur_index2 == even_range+1:
                self.max_even = max(self.max_even, len(even_set))
                return None
            else:
                for next_set2 in available_dict[2 * cur_index2 + 1]:
                    is_valid2 = True
                    for check_y2, check_x2 in even_set:
                        if abs(check_y2 - next_set2[0]) == abs(check_x2 - next_set2[1]):
                            is_valid2 = False
                            break
                    if is_valid2:
                        even_set.add(next_set2)
                        DFS_even(cur_index2 + 1)
                        even_set.remove(next_set2)
                DFS_even(cur_index2 + 1)

        DFS_odd(0)
        DFS_even(0)
        print(self.max_odd + self.max_even,end="")

Solution()

#
# 6
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1