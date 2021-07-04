def main():
    s = input()
    sl = (len(s) - 1) // 2
    a = s[:sl]
    b = s[-sl:]
    if a == b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
