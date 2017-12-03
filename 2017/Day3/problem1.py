# -*- coding: utf-8 -*-
from math import ceil

def get_angle_from_index(i, r):
    """ Calculate the angle of the given index (i) in the ring of the given radius (r).

    This function only works for `r >= 2`.

    Angle (θ) is calculated by the following function where `s = r - 1` (The ring indices are rotated by -1):

    `θ = ((-1)^(i/r))(s + (2⌈i/2r⌉)r) - ((-1)^(i/r))i`
    """
    if r < 2:
        raise ValueError("Radius must be greater than or equal to 2")

    if i == 0:
        i = i + 8 * r # Transform by 1 rotation to avoid divide by zero

    s = r - 1
    return int(((-1)**(i / r)) * (s + ((2 * ceil(i / (2 * r))) * r)) - (((-1)**(i / r)) * i))

def manhattan_distance(input):
    curr_start = 1
    curr_end = 2
    curr_ring = range(curr_start, curr_end)
    radius = 0
    while input not in curr_ring:
        radius = radius + 1
        curr_start = curr_end
        curr_end = curr_end + 8 * radius # circumference = 8 * radius
        curr_ring = range(curr_start, curr_end)

    theta = get_angle_from_index(curr_ring.index(input), radius)
    return theta + radius

if __name__ == "__main__":
    print manhattan_distance(325489)