def i_list(el, li):
    out = None
    for i in range(len(li) - 1):
        for j in range(len(li) - 1):
            if el == li[i][j]:
                out = (i, j)
    return out

