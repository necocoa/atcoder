from collections import Counter


def main():
    _, *S = open(0).read().split()

    c = Counter(S)
    max_cnt = max(c.values())
    ans = [k for k, v in c.items() if v == max_cnt]
    ans.sort()
    print("\n".join(ans))


if __name__ == '__main__':
    main()
