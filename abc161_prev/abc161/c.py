def main():
    n, k = map(int, input().split())
    m = n % k
    print(min(m, k-m))


if __name__ == '__main__':
    main()
