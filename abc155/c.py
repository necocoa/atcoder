from collections import Counter


def main():
    N = int(input())
    A = [input() for _ in range(N)]

    c = Counter(A)
    max_num = c.most_common()[0][1]
    ANS = [i[0] for i in c.items() if i[1] == max_num]
    ANS.sort()
    for ans in ANS:
        print(ans)


if __name__ == '__main__':
    main()
