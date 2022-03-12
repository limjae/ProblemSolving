def make_seq():
    count = int(input())
    # O(N)
    need_stack = [int(input()) for i in range(count)]
    # O(N)
    need_stack.reverse()

    nums_stack = []
    history = []
    # O(N) + O(N)
    for i in range(1, count+1):
        if not nums_stack:
            nums_stack.append(i)
            history.append("+")
        else:
            while nums_stack:
                if nums_stack[-1] == need_stack[-1]:
                    nums_stack.pop()
                    need_stack.pop()
                    history.append("-")
                elif nums_stack[-1] < need_stack[-1]:
                    break
                else:
                    return "\n".join(["NO"])
            nums_stack.append(i)
            history.append("+")

    while nums_stack:
        if nums_stack[-1] == need_stack[-1]:
            nums_stack.pop()
            need_stack.pop()
            history.append("-")
        else:
            return "\n".join(["NO"])

    return "\n".join(history)

print(make_seq(), end="")
