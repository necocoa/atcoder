def main():
    n, k, m = map(int, input().split())
    now_sum = sum(map(int, input().split()))
    ans = m * n - now_sum
    if ans > k:
        print(-1)
    elif ans >= 0:
        print(ans)
    else:
        print(0)


if __name__ == '__main__':
    main()
