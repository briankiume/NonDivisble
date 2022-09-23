from collections import Counter


def nonDivisible(a):
    non_div = []
    all_div = []
    for x, num in enumerate(a):
        remaining = a[:x] + a[x + 1:]
        for y in remaining:
            if num % y != 0:
                non_div.append((x, y))
            else:
                all_div.append(x)

    all_counts = Counter(all_div)
    culprits = []
    for x in all_counts:
        if all_counts[x] == (len(a) - 1):
            culprits.append(x)

    culprits_pairs = []
    for culprit in culprits:
        culprits_pairs.append((culprit, 0))

    dict_num = Counter()
    for pair in non_div:
        dict_num[pair[0]] += 1

    sorted_keys = sorted(dict_num.keys())
    sorted_vals = []
    for x in sorted_keys:
        for y in dict_num:
            if x == y:
                sorted_vals.append(dict_num[x])

    for pair in culprits_pairs:
        sorted_vals.insert(pair[0], pair[1])

    return sorted_vals


print(nonDivisible([3, 1, 2, 3, 6]))
