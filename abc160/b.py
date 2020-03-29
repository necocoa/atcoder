def main():
    x = int(input())
    ans = x // 500 * 1000
    xx = x % 500
    ans += xx // 5 * 5
    print(ans)


if __name__ == '__main__':
    main()
