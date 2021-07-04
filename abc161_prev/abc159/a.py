def main():
    a, b = map(int, input().split())
    sa = a * (a - 1) // 2
    sb = b * (b - 1) // 2
    print(sa + sb)


if __name__ == '__main__':
    main()
