input_list = [1,3,4,2]
input_list.sort()
slicing_list = []
i = 0
j = 0
k = 0
sum = 0

while j < len(input_list) // 2:
    slicing_list.append(input_list[i: i + 2])
    i += 2
    j += 1

while k < j:
    sum += slicing_list[k][0]
    k += 1

print(sum)