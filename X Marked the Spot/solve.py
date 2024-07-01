from itertools import cycle

with open("ct", "rb") as f:
    ct = f.read()

prefix = bytes(a ^ b for a, b in zip(b"uiuctf{", ct[:7]))
print(prefix)
suffix = bytes(a ^ b for a, b in zip(b"}", ct[-1:]))
print(suffix)
key = prefix + suffix
flag = bytes(a ^ b for a, b in zip(ct, cycle(key)))
print(flag)

# Cái này dễ rồi ha, chắc ko cần hướng dẫn đâu :)))