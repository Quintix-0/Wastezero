def optimize(n, f, s):
    x = round(n/(f+s))
    y=x
    excess = n - (x*f + y*s)
    options = [[x, y, excess]]
    while y > 0:

        if excess >= 0:
            x += 1
        else:
            y -= 1
        if y <= 0.33*x and x > 2:
            break
        excess = n - (x*f + y*s)
        options.append([x, y, excess])

    return sorted(options, key=lambda x: abs(x[2]))
