def main():
    _, m = map(int, input().split())
    ary = sorted(list(map(int, input().split())), reverse=True)
    if ary[m-1]*4*m >= sum(ary):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
