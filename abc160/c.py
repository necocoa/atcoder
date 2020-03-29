def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    a = 0
    for i in range(N-1):
        a += A[i + 1] - A[i]
    ans = a

    c = a - (A[1] - A[0]) + ((K + A[0]) - A[-1])
    if ans > c:
        ans = c
    d = a - (A[-1] - A[-2]) + ((K + A[0]) - A[-1])
    if ans > d:
        ans = d

    for i in range(N-3):
        e = c - (A[i + 2] - A[i + 1]) + (A[i + 1] - A[i])
        if ans > e:
            ans = e
    print(ans)


if __name__ == '__main__':
    main()
