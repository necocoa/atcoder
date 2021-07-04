def main():
    n, m = map(int, input().split())
    a_sum = sum(list(map(int, input().split())))
    if n < a_sum:
        print(-1)
    else:
        print(n - a_sum)


if __name__ == '__main__':
    main()
