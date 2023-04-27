start = input()
end = input()


def chr_range(starts, ends):
    result = ""
    for digit in range(ord(starts) + 1, ord(ends)):
        result += chr(digit)
        result += " "
    return result


print(chr_range(start, end))
