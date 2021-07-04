def main():
    n, m = map(int, input().split())
    ary = [input().split() for _ in range(m)]
    ac_cnt = 0
    wa_cnt = 0
    ac_ary = [[0, 0] for i in range(n)]
    for toi_num, kekka in ary:
        num = int(toi_num) - 1
        if ac_ary[num][0] == 0:
            if kekka == 'WA':
                ac_ary[num][1] += 1
            elif kekka == 'AC':
                ac_ary[num][0] = 1
                ac_cnt += 1
                wa_cnt += ac_ary[num][1]
    print(ac_cnt, wa_cnt)

if __name__ == '__main__':
    main()
