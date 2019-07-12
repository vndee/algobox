def longest_increase_sequence(ls: list):
    f = []
    for id, num in enumerate(ls):
        f.append(1)
        for prev in range(0, id):
            if num >= ls[prev] and f[prev] + 1 > f[id]:
                f[id] = f[prev] + 1
    return max(f)
