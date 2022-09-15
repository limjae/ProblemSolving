
def solution(survey, choices):
    answer = ''
    sequence_max = len(survey)

    char_stat = [0,0,0,0]
    char_type = [
        ["R", "T"],
        ["C", "F"],
        ["J", "M"],
        ["A", "N"],
    ]

    for i in range(sequence_max):
        survey_type = survey[i]

        if survey_type == "RT":
            char_stat[0] += choices[i] - 4
        elif survey_type == "TR":
            char_stat[0] += 4 - choices[i]

        elif survey_type == "CF":
            char_stat[1] += choices[i] - 4
        elif survey_type == "FC":
            char_stat[1] += 4 - choices[i]

        elif survey_type == "JM":
            char_stat[2] += choices[i] - 4
        elif survey_type == "MJ":
            char_stat[2] += 4 - choices[i]

        elif survey_type == "AN":
            char_stat[3] += choices[i] - 4
        elif survey_type == "NA":
            char_stat[3] += 4 - choices[i]

    answer = "".join([char_type[index][1] if char_val > 0 else char_type[index][0]
                      for index, char_val in enumerate(char_stat)])


    return answer