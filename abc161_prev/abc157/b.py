def main():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]
    ans = [[0] * 3 for _ in range(3)]
    for b in B:
        for i, a in enumerate(A):
            g = my_index(a, b)
            if g != 'no':
                ans[i][g] = 1
    for r in range(3):
        if 1 == ans[0][r] == ans[1][r] == ans[2][r]:
            print('Yes')
            exit()
    for r in range(3):
        if 1 == ans[r][0] == ans[r][1] == ans[r][2]:
            print('Yes')
            exit()
    if 1 == ans[0][0] == ans[1][1] == ans[2][2]:
        print('Yes')
        exit()
    if 1 == ans[0][2] == ans[1][1] == ans[2][0]:
        print('Yes')
        exit()
    print('No')


def my_index(l, x):
    return l.index(x) if x in l else 'no'


if __name__ == '__main__':
    main()
