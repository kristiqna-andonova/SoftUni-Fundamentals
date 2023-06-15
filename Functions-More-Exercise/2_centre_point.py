import math

x_1 = math.floor(float(input()))
y_1 = math.floor(float(input()))
x_2 = math.floor(float(input()))
y_2 = math.floor(float(input()))

sum_x1 = math.floor(abs(x_1) + abs(y_1))
sum_x2 = math.floor(abs(x_2) + abs(y_2))


def center_point_searcher(sum1, sum2):
    if sum1 <= sum2:
        return f"({x_1}, {y_1})"
    else:
        return f"({x_2}, {y_2})"


print(center_point_searcher(sum_x1, sum_x2))
