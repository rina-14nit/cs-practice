def count_items(values):
    counts = {}
    for elem in values:
        counts[elem] = counts.get(elem, 0) + 1
    return counts

def unique_sorted(values):
    return sorted(set(values))

def common(first, second):
    return sorted(set(first) & set(second))

def only_in_first(first, second):
    return sorted(set(first) - set(second))
