def main():
    ary = '1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51'
    ans = list(map(int, ary.split(', ')))
    a = int(input()) - 1
    print(ans[a])


if __name__ == '__main__':
    main()
