from collections import Counter

def choose2(n):
    return n * (n - 1) // 2


def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    cnt = 0
    for c in C.values():
        cnt += choose2(c)

    for a in A:
        ans = cnt
        ans -= choose2(C[a])
        ans += choose2(C[a] - 1)
        print(ans)


if __name__ == '__main__':
    main()
