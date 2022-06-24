import math


def count_find_num(primesL, limit):
    min_value = math.prod(primesL)
    if min_value > limit:
        return []
    elif min_value == limit:
        return [1, limit]
    else:
        values = [min_value]
        max_value = min_value
        for i in primesL:
            for n in values:
                new_value = n * i
                while (new_value <= limit) and (new_value not in values):
                    values.append(new_value)
                    if new_value > max_value:
                        max_value = new_value
                    new_value *= i

        return [len(values), max_value]
