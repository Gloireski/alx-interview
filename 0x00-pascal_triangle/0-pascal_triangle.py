#!/usr/bin/python3
"""
    pascal_triangle
"""


def pascal_triangle(n):
    """
        return list of lists
    """
    pascal = []
    if n <= 0:
        return pascal
    lp = []
    for j in range(n):
        nl = lp + [1]
        for i in range(len(lp) - 1):
            nl[i + 1] = lp[i] + lp[i + 1]
        lp = nl
        pascal.append(nl)
    # print(pascal)
    return(pascal)
