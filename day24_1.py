from itertools import product
from math import floor

z = 0


def execute_block(d, kx, ky, kz):
    global z
    x = z % 26 + kx
    z = floor(z / kz)
    if x != d:
        z *= 26
        z += d + ky


def guess_execution(kx, ky, kz):
    d = z % 26 + kx
    if d > 9 or d < 1:
        return 0
    execute_block(d, kx, ky, kz)
    return d


for digits in product([9, 8, 7, 6, 5, 4, 3, 2, 1], repeat=7):
    number = ''
    z = 0
    execute_block(digits[0], kx=10, ky=0, kz=1)
    execute_block(digits[1], kx=12, ky=6, kz=1)
    execute_block(digits[2], kx=13, ky=4, kz=1)
    execute_block(digits[3], kx=13, ky=2, kz=1)
    execute_block(digits[4], kx=14, ky=9, kz=1)

    number += ''.join(str(i) for i in digits[:5])
    if not (d := guess_execution(kx=-2, ky=1, kz=26)):
        continue
    number += str(d)

    execute_block(digits[5], kx=11, ky=10, kz=1)
    number += str(digits[5])

    if not (d := guess_execution(kx=-15, ky=6, kz=26)):
        continue
    number += str(d)

    if not (d := guess_execution(kx=-10, ky=4, kz=26)):
        continue
    number += str(d)

    execute_block(digits[6], kx=10, ky=6, kz=1)
    number += str(digits[6])

    if not (d := guess_execution(kx=-10, ky=3, kz=26)):
        continue
    number += str(d)

    if not (d := guess_execution(kx=-4, ky=9, kz=26)):
        continue
    number += str(d)

    if not (d := guess_execution(kx=-1, ky=15, kz=26)):
        continue
    number += str(d)

    if not (d := guess_execution(kx=-1, ky=5, kz=26)):
        continue
    number += str(d)

    if z == 0:
        print(number)
        break

# 94992994195998
