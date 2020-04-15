import itertools


def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    l = [i for i in range(1, n + 1)]
    mp = {}
    for v in itertools.permutations(l, n):
        mp[v] = len(mp)
    print(abs(mp[p] - mp[q]))


if __name__ == '__main__':
    main()
