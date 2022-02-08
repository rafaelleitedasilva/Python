def _min(*args):
    res = float(inf)
    for value in args:
        if value < res:
            res = value
    
    return res
    
