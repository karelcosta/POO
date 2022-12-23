from typing import List, Tuple

def simplex_revisado(c: List[float], A: List[List[float]], b: List[float]) -> Tuple[List[float], float]:
    m, n = len(A), len(A[0])
    cb = [0] * m
    basicas = list(range(m))
    nonbasicas = list(range(m, m+n))

    def pivot(l, e):
        A[l] = [ai / A[l][e] for ai in A[l]]
        for i in range(m):
            if i != l:
                A[i] = [A[i][j] - A[i][e] * A[l][j] for j in range(n+1)]
        cb[l], nonbasicas[e] = nonbasicas[e], cb[l]

    while True:
        e = cb.index(min(cb))
        if c[e] >= 0:
            return [0] * m + [1], sum(c[i] * x for i, x in enumerate(basicas))

        ratios = [A[i][-1] / A[i][e] for i in range(m) if A[i][e] > 0]
        if not ratios:
            return None, float('inf')
        l = ratios.index(min(ratios))
        pivot(l, e)



fo = [-20, -24, -0, -0]
sa = [[3, 6, 1, 0][4, 2, 0, 1]]
sab = [60, 32]
simplex_revisado(fo, sa, sab)