def solution(files):
    head_number_string = []

    for string in files:
        head, number = 0, 0

        for c in string:
            if not c.isnumeric():
                head += 1
            else:
                break

        number = head
        for c in string[number:]:
            if c.isnumeric():
                number += 1
            else:
                break

        head_number_string.append((string[:head], int(string[head:number]), string))

    head_number_string.sort(key=lambda x: (x[0].upper(), x[1]))
    return [s[2] for s in head_number_string]

