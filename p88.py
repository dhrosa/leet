def merge(xs: list[int], xs_count: int, ys: list[int], ys_count: int) -> None:
    i = 0
    j = 0
    out = list[int]()
    while True:
        if j >= ys_count:
            out.extend(xs[i:xs_count])
            break
        if i >= xs_count:
            out.extend(ys[j:ys_count])
            break
        x = xs[i]
        y = ys[j]
        if x <= y:
            out.append(x)
            i += 1
        else:
            out.append(y)
            j += 1
    xs[:] = out
