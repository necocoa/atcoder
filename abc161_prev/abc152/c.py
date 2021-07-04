def main():
    n = int(input())
    min_num = 10 ** 9
    ans = 0
    for p in map(int, input().split()):
        if p < min_num:
            ans += 1
            min_num = p
    print(ans)


if __name__ == '__main__':
    main()
