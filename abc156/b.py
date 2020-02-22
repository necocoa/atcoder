def main():
    N, K = map(int, input().split())
    x = Base_10_to_n(N, K)
    print(len(x))


def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X % n)
    return str(X % n)


if __name__ == '__main__':
    main()
