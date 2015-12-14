# 4518    28471
def is_number_balanced(n):
    digits = []
    if len(str(n)) == 1:
        return True
    else:
        for i in str(n):
            digits = [n % 10] + digits
            n = n // 10
        if len(digits) % 2 == 0:
            return sum(digits[:len(digits) // 2]) == sum(digits[len(digits) // 2:])
        else:
            return sum(digits[:len(digits) // 2]) == sum(digits[len(digits) // 2 + 1:])


def is_increasing(seq):
    res = True
    if len(seq) == 1:
        return res
    else:
        for i in range(len(seq) - 1):
            if seq[i] < seq[i + 1]:
                res = True
            else:
                res = False
    return res


def is_decreasing(seq):
    res = True
    if len(seq) == 1:
        return res
    else:
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                res = True
            else:
                res = False
    return res


def get_largest_palindrome(n):
    num = n - 1
    while num > 0:
        if str(num) == str(num)[::-1]:
            return num
        else:
            num -= 1


def prime_numbers(n):
    purge = 2
    if n == 1:
        return ' 1 is not valid input'
    else:
        pnums = [x for x in range(2, n + 1)]
        while purge < 30:
            for i in pnums:
                if i == purge:
                    pass
                else:
                    if i % purge == 0:
                        pnums.remove(i)
                    else:
                        pass
            purge += 1
    return pnums


def is_anagram(word1, word2):
    a = [x for x in word1.lower()]
    b = [x for x in word2.lower()]
    return a.sort() == b.sort()


def birthday_ranges(birthdays, ranges):
    collect = {}
    ret = []
    for i in ranges:
        collect[i] = 0
    # count = 0
    for k in birthdays:
        for j in ranges:
            if k in range(j[0], j[1] + 1):
                collect[j] += 1
            else:
                pass
    for tup in ranges:
        ret += [collect[tup]]
    return ret


def sum_matrix(m):
    summ = 0
    for i in m:
        for j in i:
            summ += j
    return summ


def find_neighbors(x, y, rows, columns):
    res = []
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if rows > i >= 0 and columns > j >= 0 and (i, j) != (x, y):
                res += [(i, j)]
            else:
                pass
    return res

'''
[1,2,3],
[4,5,6],
[7,8,9]
'''


def matrix_bombing_plan(m):
    from copy import deepcopy
    rows = len(m)
    columns = len(m[0])
    positions = {(i, j): m[i][j] for i in range(rows) for j in range(columns)}
    res = {}
    bomb_values = positions
    for row in range(rows):
        for column in range(columns):
            bombed_m = deepcopy(m)
            for i, j in find_neighbors(row, column, rows, columns):
                bombed_m[i][j] -= bomb_values[(row, column)]
                if bombed_m[i][j] < 0:
                    bombed_m[i][j] = 0
                else:
                    pass
            res[row, column] = sum_matrix(bombed_m)
    return res


def is_traversal(traversal, family):
    res = False
    for i in family:
        if len(traversal & i) == 0:
            res = False
        else:
            res = True
    return res
