def main():
    n, k = map(int, input().split())
    n = n - (n // k * k)
    ans = n
    cnt = 0
    while cnt < 10:
        n = abs(n - k)
        if ans > n:
            ans = n
        else:
            cnt += 1
    print(ans)


if __name__ == '__main__':
    main()
