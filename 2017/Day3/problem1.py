# -*- coding: utf-8 -*-
from math import ceil

def get_angle_from_index(i, r):
    """ Calculate the angle of the given index (`i`) in the ring of the given radius (`r`).

    This function only works for `r >= 2`.

    Angle (`θ`) is calculated by the following function:
    ```
    θ = (-1)^(i/r)(r + (2⌈i/(2r)⌉)r - i - 1)
    ```

    This is the function for the graph that looks like this:
    ```

       max θ |    /\    /\    /\    /
    θ        |\  /  \  /  \  /  \  /
           0 |_\/____\/____\/____\/__
         i = 0 r-1  3r-1  5r-1  7r-1
    ```
    The graph is translated in order to account for the rings' 0-th position being one up from the bottom right corner.

    This allows you to easily determine the "angle" away from 0 at any index in any ring in this pattern:
    ```
    4 3 2 1 0 1 2 3 4
    3 3 2 1 0 1 2 3 3
    2 2 2 1 0 1 2 2 2
    1 1 1       1 1 1
    0 0 0       0 0 0
    1 1 1       1 1 1
    2 2 2 1 0 1 2 2 2
    3 3 2 1 0 1 2 3 3
    4 3 2 1 0 1 2 3 4
    ```
    and continuing outward arbitrarily.
    """
    if r < 2:
        raise ValueError("Radius must be greater than or equal to 2")

    if i == 0:
        i = i + 8 * r # Translate by 1 rotation to avoid divide by zero

    return int((-1)**(i / r) * (r + ((2 * ceil(i / (2 * r))) * r) - i - 1))

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
