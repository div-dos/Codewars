def ips_between(start, end):
    # TODO
    s = sum(int(a) << (24 - i * 8) for i, a in enumerate(start.split('.')))
    e = sum(int(a) << (24 - i * 8) for i, a in enumerate(end.split('.')))
    return e-s