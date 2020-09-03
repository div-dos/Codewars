def snail(snail_map):
    j = 0
    if len(snail_map) == 1: return snail_map[0]
    s, res = len(snail_map), []

    while j <= s:
        for i in range(j, s): res.append(snail_map[j][i])
        for i in range(j + 1, s - 1): res.append(snail_map[i][s - 1])
        for i in range(s, j, - 1) if s - j > 1 else []: res.append(snail_map[s - 1][i - 1])
        for i in range(s - 2, j, -1): res.append(snail_map[i][j])
        s, j = s - 1, j + 1

    return res