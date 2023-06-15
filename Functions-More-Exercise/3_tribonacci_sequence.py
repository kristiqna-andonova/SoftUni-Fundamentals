number = int(input())


def tribonacci_fun(n):
    list_nums = [1, 0, 0]
    for i in range(n):
        next_num = sum(list_nums)
        print(next_num, end=" ")
        list_nums.append(next_num)
        list_nums.pop(0)


tribonacci_fun(number)
