def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    ANS = [0 for _ in range(N)]
    ANS[0] = 1
    for i, s in enumerate(S):
        if s[0] == 1 and s[1] == 0:
            print(-1)
            exit()
        for i2, s2 in enumerate(S):
            if i == i2:
                continue
            if s[0] == s2[0]:
                if s[1] != s2[1]:
                    print(-1)
                    exit()
        ANS[s[0] - 1] = s[1]
    ans = int(''.join([str(n) for n in ANS]))
    print(ans)


if __name__ == '__main__':
    main()
