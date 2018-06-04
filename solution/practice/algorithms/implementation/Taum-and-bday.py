def taumBday(b, w, x, y, z):
    cost = 0
    if (((x+z)*w)<(y*w)):
        cost = x*b + (x+z)*w
    elif (((y+z)*b)<(x*b)):
        cost = (y+z)*b + y*w
    else:
        cost = x*b + y*w
    return cost
    
