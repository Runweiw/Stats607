


def myfloat(x):
    try:
        return float(x)
    except ValueError:
        return float('nan')


#`````
#Input:
#x: string(contain numbers)
#Output:
#out: float(if not empty)
#else: nan
#``````