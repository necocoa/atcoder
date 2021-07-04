from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))
    C = Counter(a)
    for i in range(1, n + 1):
        if C[i]:
            print(C[i])
        else:
            print(0)


if __name__ == '__main__':
    main()
