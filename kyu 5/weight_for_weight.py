from collections import defaultdict
def order_weight(strng):
    # your code
    data = defaultdict(list)
    for i in strng.split():
        data[sum(map(int, i))].append(i)
    return ' '.join(' '.join(sorted(data[a])) for a in sorted(data))