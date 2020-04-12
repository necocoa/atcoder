def checkCount(ary, Sk, ji):
    cnt = ary.count(Sk)
    if len(ary) > ji - 1:
        if ary[ji-1] == Sk:
            cnt -= 1
    return cnt


def main():
    n = int(input())
    ary = list(input())
    ans = 0
    for i in range(n-3):
        Si = ary.pop(0)
        for j, Sj in enumerate(ary):
            if Sj != Si:
                tmp = ary[j + 1:]
                if tmp != []:
                    ji = (j + 1 + i) - i
                    if Si == 'R':
                        if Sj == 'G':
                            ans += checkCount(tmp, 'B', ji)
                        else:
                            ans += checkCount(tmp, 'G', ji)
                    if Si == 'G':
                        if Sj == 'R':
                            ans += checkCount(tmp, 'B', ji)
                        else:
                            ans += checkCount(tmp, 'R', ji)
                    if Si == 'B':
                        if Sj == 'R':
                            ans += checkCount(tmp, 'G', ji)
                        else:
                            ans += checkCount(tmp, 'R', ji)
    print(ans)


if __name__ == '__main__':
    main()
