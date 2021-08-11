"""
欧几里得算法：求两数的最大公约数
"""


# 若q是0，则最大公约数为p。否则，将p除以q得到余数r，p和q的最大公约数即为q和r的最大公约数。
def gcd(q, p):
    if p == 0:
        return q
    r = q % p
    return gcd(p, r)


if __name__ == '__main__':
    print(gcd(68, 128))
