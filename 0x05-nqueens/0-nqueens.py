#!/usr/bin/python3
import sys
from typing import List
import copy


if len(sys.argv) < 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError as e:
    print('N must be a number')
    exit(1)

if n < 4:
    print('N must be at least 4')
    exit(1)


def allSolutions(n: int) -> List[List[int]]:
    """ Returns all solutions """
    solutions = []
    queenspos = [[0, 0] for i in range(n)]
    cols = set()
    posDiag = set()
    negDiag = set()

    def backtrack(r: int):
        """ performs backtracking """
        if r == n:
            board_copy = copy.deepcopy(queenspos)
            solutions.append(board_copy)
            return
        for c in range(n):
            if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                continue
            cols.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            queenspos[r][0] = r
            queenspos[r][1] = c
            # print(queenspos)
            backtrack(r + 1)

            cols.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            queenspos[r][0] = 0
            queenspos[r][1] = 0

    backtrack(0)
    return solutions


def print_solutions():
    solutions = allSolutions(n)
    for solution in solutions:
        print(solution)


print_solutions()
