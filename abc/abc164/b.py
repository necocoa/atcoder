def main():
    a, b, c, d = map(int, input().split())
    while a > 0 or b > 0:
        c -= b
        if c <= 0:
            print('Yes')
            exit()

        a -= d
        if a <= 0:
            print('No')
            exit()


if __name__ == '__main__':
    main()
