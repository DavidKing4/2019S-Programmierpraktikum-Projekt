def i_list(el, li):
    out = None
    for i in range(len(li)):
        for j in range(len(li[i])):
            if el == li[i][j]:
                out = (i, j)
    return out

def listi_list(el, li):
    out = []
    for i in range(len(li) ):
        for j in range(len(li[i]) ):
            if el == li[i][j]:
                out.append((i,j))
    return out

