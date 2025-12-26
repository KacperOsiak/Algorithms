def nb_year(p0, percent, aug, p):
    n = 0
    percent = percent/100 
    while p>p0:
        n +=1
        p0 = int(p0 + p0 * percent + aug)
    return n

