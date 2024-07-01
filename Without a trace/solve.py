import numpy as np
from Crypto.Util.number import bytes_to_long
from itertools import permutations

"""
2 ma trận F, M là ma trận đường chéo
F = [
        [f1, 0, 0, 0, 0],
        [0, f2, 0, 0, 0],
        [0, 0, f3, 0, 0],
        [0, 0, 0, f4, 0],
        [0, 0, 0, 0, f5],
    ]
    
M = [
        [m1, 0, 0, 0, 0],
        [0, m2, 0, 0, 0],
        [0, 0, m3, 0, 0],
        [0, 0, 0, m4, 0],
        [0, 0, 0, 0, m5],
    ]
    
Nên np.matmul(F, M) = [
        [m1*f1, 0, 0, 0, 0],
        [0, m2*f2, 0, 0, 0],
        [0, 0, m3*f3, 0, 0],
        [0, 0, 0, m4*f4, 0],
        [0, 0, 0, 0, m5*f5],
    ]
Ý tưởng là gửi (1, 1, 1, 1, 1) rồi (2, 1, 1, 1, 1), (1, 2, 1, 1, 1) và tiếp tục ...
ta sẽ có f1, f2, f3, f4, f5 -> FLAG
"""
