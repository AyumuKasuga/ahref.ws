def int_to_36(d):
    all = '0123456789abcdefghijklmnopqrstuvwxyz'
    lall = len(all)
    r = list()
    c = d
    while True:
        c, o = c // lall, c % lall
        r.append(o)
        if c < 1:
            r.append(c) if c is not 0 else None
            break
    r.reverse()
    return ''.join(map(lambda x: all[x], r))