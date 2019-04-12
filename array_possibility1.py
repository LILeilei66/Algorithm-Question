"""
via Baidu
一个长为 N+1 的array, a[0] == a[N] == 1;
for i in range(1, N): a[i] != a[i-1] and 1 <= a[i] <= M
问: 有几种可能性.
"""

def possi(M, N):
    n = N-1
    one = 0
    not_one = (M-1)
    possibility = [one, not_one]
    print(possibility)
    n -= 1
    while n != 0:
        possibility = [possibility[1], possibility[0] * (M-1) + possibility[1] * (M-2)]
        n -= 1
        print(possibility)
    return possibility[1]

if __name__ == '__main__':
    print(possi(3, 4))

