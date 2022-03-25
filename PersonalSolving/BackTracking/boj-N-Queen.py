class Solution:
    answer = 0
    def __init__(self):
        length = int(input())
        queen_set = [-1 for _ in range(length)]

        def DFS(cur_index):
            if cur_index == length:
                self.answer += 1
                return None
            else:
                for set_queen in range(length):
                    is_valid = True
                    for i in range(cur_index):
                        if queen_set[i] == set_queen or cur_index - i == abs(queen_set[i] - set_queen):
                            is_valid = False
                            break
                    if is_valid:
                        queen_set[cur_index] = set_queen
                        DFS(cur_index + 1)
                        queen_set[cur_index] = -1

        for i in range(length):
            queen_set[0] = i
            DFS(1)
        print(self.answer,end="")

Solution()


