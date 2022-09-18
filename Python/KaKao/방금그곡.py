def solution(m, musicinfos):
    answer = "(None)"
    answer_list = []

    m = convert_symbol(m)

    for info in musicinfos:
        start, end, title, melody = info.split(",")
        start_second = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
        end_second = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
        duration = end_second - start_second

        melody = convert_symbol(melody)

        total_melody = "".join([melody[i % len(melody)] for i in range(duration)])
        print(melody, total_melody)
        index = total_melody.find(m)
        if index > -1:
            answer_list.append([duration, title])

    answer_list.reverse()
    answer_list.sort(key=lambda x: x[0])

    print(answer_list)

    return answer_list.pop()[1] if answer_list else "(None)"


def convert_symbol(s):
    s = s.replace("A#", "a")
    s = s.replace("C#", "c")
    s = s.replace("D#", "d")
    s = s.replace("F#", "f")
    s = s.replace("G#", "g")
    return s
