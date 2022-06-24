from itertools import combinations as comb


def bananas(s):
    result = set()
    # Conditions for a "meaningless" check
    a = 0
    b = 0
    n = 0
    for i in s:
        if i == 'b':
            b += 1
        if i == 'a':
            a += 1
        if i == 'n':
            n += 1

    if all((
            len(s) >= 6,
            b >= 1,
            n >= 2,
            a >= 3
    )):
        # The main algorithm
        string = 'banana'
        symbol = '-' * (len(s) - len(string))
        for tuple_item in comb(range(len(s)), len(symbol)):
            pattern = list(s)

            for n in tuple_item:
                pattern[n] = '-'
            pattern = ''.join(pattern)

            if pattern.replace('-', '') == string:
                result.add(pattern)
        return result
    else:
        return result
