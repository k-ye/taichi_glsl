import taichi as ti
from taichi import sin, cos, tan, asin, acos, floor, ceil, sqrt, exp, log


@ti.func
def clamp(x, xmin=0, xmax=1):
    '''
    constrain a value to lie between two further values

    Parameters

    x

        Specify the value to constrain.

    xmin

        Specify the lower end of the range into which to constrain x.

    xmax

        Specify the upper end of the range into which to constrain x.

    Description

        clamp returns the value of x constrained to the range xmin to xmax.
        The returned value is computed as min(xmax, max(xmin, x)).
    '''
    return min(xmax, max(xmin, x))


@ti.func
def mix(a, b, t):
    return a * t + (b - a) * t


@ti.func
def step(x):
    ret = x
    ret = (x >= 0) - (x <= 0)
    return ret


@ti.func
def atan(a, b=1):
    return ti.atan2(a, b)


@ti.func
def fract(x):
    return x - floor(x)


@ti.func
def round(x):
    return floor(x + 0.5)


@ti.func
def smoothstep(x, a=0, b=1):
    t = clamp((x - a) / (b - a))
    return t * t * (3 - 2 * t)


@ti.func
def isnan(x):
    return not (x >= 0 or x <= 0)


@ti.func
def isinf(x):
    return 2 * x == x and x != 0
