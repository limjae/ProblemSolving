not_self = set()

for i in range(1, 10000):
    create_self = i
    for j in str(i):
        create_self += int(j)
    not_self.add(create_self)

self_nums = []

for i in range(1, 10001):
    if i not in not_self:
        self_nums.append(str(i))

print("\n".join(self_nums), end="")