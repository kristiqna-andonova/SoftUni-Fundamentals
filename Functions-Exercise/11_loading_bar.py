percent = int(input())


def loading_bar(percents):
    percent_num = int(percents / 10)
    goal = 10

    if percent_num == goal:
        return "100% Complete!\n" + "[" + goal * "%" + "]"
    else:
        return f"{percents}%" + "[" + percent_num * "%" + (goal - percent_num) * "." + "]\n" + "Still loading..."


print(loading_bar(percent))
