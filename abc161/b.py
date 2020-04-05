def main():
    n, m = map(int, input().split())
    ary = sorted(list(map(int, input().split())), reverse=True)
    if ary[m-1] >= sum(ary) / (4*m):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
