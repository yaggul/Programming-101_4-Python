# ["apple", "banana", "apple", "pie"]
# ["python", "python", "python", "ruby"]


def count_words(arr):
    counter = {}
    for i in arr:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 0
            counter[i] += 1
    return counter


def nan_expand(times):
    nan = 'NaN'
    pref = 'Not a '
    if times == 0:
        return ''
    else:
        return times * pref + nan


def iterations_of_nan_expand(expanded):
    nan = 'NaN'
    pref = 'Not a '
    start = 0
    counter = 0
    if expanded == '':
        return ''
    elif expanded.find(nan) == -1:
        return False
    else:
        while start < len(expanded) - len(pref):
            if expanded[start:start + len(pref)] == pref:
                counter += 1
            else:
                pass
            start += 1
    return counter


# [1,1,1,2,3,1,1]
# [[1,1,1],[2],[3],[1,1]]

def group2(l1):
    grouper = [l1[0]]
    res = []
    ind = 1
    while ind < len(l1):
        if l1[ind] == l1[ind - 1]:
            grouper += [l1[ind]]
            ind += 1
        else:
            res += [grouper]
            grouper = []
            grouper += [l1[ind]]
            ind += 1
    res += [grouper]
    grouper = []
    return res

# second solution with 'for loop'


def group(l):
    grouper = [l[0]]
    res = []
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            grouper += [l[i]]
        else:
            res += [grouper]
            grouper = []
            grouper += [l[i]]
    res += [grouper]
    grouper = []
    return res


def max_consecutive(items):
    max_len = 0
    for i in group(items):
        if len(i) > max_len:
            max_len = len(i)
        else:
            pass
    return max_len


def gas_stations(distance, tank_size, stations):
    res = []
    start = 0
    pitstop = 0
    for i in range(len(stations)):
        if stations[i] - start < tank_size:
            pitstop = stations[i]
        else:
            start = pitstop
            if pitstop <= distance:
                res += [pitstop]
            else:
                pass
            if stations[i] - start < tank_size:
                pitstop = stations[i]
            else:
                pass
    if pitstop <= distance:
        res += [pitstop]
    else:
        pass
    if distance - res[-1] > tank_size:
        return 'You will run out of fuel before reaching destination'
    else:
        return res


def sum_of_numbers(word):
    digits = '0123456789'
    grouper = ''
    res = []
    for i in word:
        if i in digits:
            grouper += i
            if len(grouper) == len(word):
                return int(grouper)
        else:
            if grouper == '':
                pass
            else:
                res.append(int(grouper))
                grouper = ''
    if grouper == '':
        pass
    else:
        res.append(int(grouper))
    if len(res) == 0:
        return 0
    else:
        return sum(res)


def numbers_to_message(ps):
    keypad = {0: ' ', 1: 'cap', 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: [
        'j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
    num_message = group(ps)
    word = ''
    caps = False
    for i in range(len(num_message)):
        if num_message[i][0] == -1:
            continue
        elif num_message[i][0] == 0:
            word += ' '
        elif num_message[i][0] == 1:
            caps = True
        else:
            if len(num_message[i]) > len(keypad[num_message[i][0]]):
                ln = len(num_message[i]) - len(keypad[num_message[i][0]])
                if caps == True:
                    word += keypad[num_message[i][0]][ln - 1].capitalize()
                    caps = False
                else:
                    word += keypad[num_message[i][0]][ln - 1]
            else:
                if caps == True:
                    word += keypad[num_message[i][0]
                                   ][len(num_message[i]) - 1].capitalize()
                    caps = False
                else:
                    word += keypad[num_message[i][0]][len(num_message[i]) - 1]
    return word


def message_to_numbers(msg):
    charpad = {('a', 'b', 'c'): 2, ('d', 'e', 'f'): 3, ('g', 'h', 'i'): 4, ('j', 'k', 'l'): 5,
               ('m', 'n', 'o'): 6, ('p', 'q', 'r', 's'): 7, ('t', 'u', 'v'): 8, ('w', 'x', 'y', 'z'): 9}
    res = []
    for i in range(len(msg)):
        for j in charpad.keys():
            if msg[i].lower() in j:
                if msg[i] == msg[i].capitalize():
                    res += [1]
                elif msg[i] == ' ':
                    res += 0
                else:
                    pass
                for k in range(j.index(msg[i].lower())+1):
                    res += [charpad[j]]
                if msg[i] in j and msg[i-1] in j:
                    res += [-1]
                else:
                    pass
    if res[-1] == -1:
        return res[:-1]
    else:
        return res
