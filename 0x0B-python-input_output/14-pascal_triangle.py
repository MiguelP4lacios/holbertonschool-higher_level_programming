#!/usr/bin/python3
"""pascal triangle
"""


def pascal_triangle(n):
    """Function
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [
            [1],
            [1, 1]]
    for r in range(1, n-1):
        row = [1]
        for c in range(0, len(triangle[r]) - 1):
            row.extend([triangle[r][c] + triangle[r][c+1]])
        row += [1]
        triangle.append(row)
    return triangle
