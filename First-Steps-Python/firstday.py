def sum_of_digits(n):
    res = 0
    digs = '0123456789'
    for i in str(n):
        if i not in digs:
            pass
        else:
            res += int(i)
    return res


def to_digits(n):
    res = []
    for i in str(n):
        res.append(i)
    return res


def to_number(digits):
    res = ''
    for i in digits:
        res = res + str(i)
    res = int(res)
    return res


def fact_digits(n):
    mem = []
    res = 1
    total = 0
    while n > 0:
        mem.append(n % 10)
        n = n // 10
    for i in mem:
        for j in range(1, i + 1):
            res *= j
        total += res
        res = 1
    return total


def fibonaci(n):
    fib = []
    a, b = 1, 1
    while len(fib) <= n - 2:
        fib.append(a)
        fib.append(b)
        a += b
        b += a
    return fib


def fib_number(n):
    res = ''
    for i in n:
        res += str(i)
    return int(res)


def palindrome(obj):
    res = ''
    for i in str(obj):
        res += i
    return res == res[::-1]


def count_vowels(word):
    vowels = 'aeiouyAEIOUY'
    count = 0
    for i in word:
        if i in vowels:
            count += 1
        else:
            pass
    print(count)


def count_consonants(word):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    count = 0
    for i in word:
        if i in consonants:
            count += 1
        else:
            pass
    print(count)


def char_histogram(word):
    mem = {}
    for i in word:
        if i in mem.keys():
            mem[i] += 1
        else:
            mem[i] = 1
    print(mem)
