from collections import Counter


def main():
    _, *S = open(0).read().split()

    c = Counter(S)
    max_num = c.most_common()[0][1]
    ans = [i[0] for i in c.items() if i[1] == max_num]
    ans.sort()
    print("\n".join(ans))


if __name__ == '__main__':
    main()
