def main():
    _ = int(input())
    X = list(map(int, input().split()))
    min = 10**8
    i = 0
    cnt = 0

    while True:
        sum = 0
        for a in X:
            sum += (a - i) ** 2
        i += 1
        if sum < min:
            min = sum
            cnt += 1
        if i > cnt:
            break
    print(min)


if __name__ == '__main__':
    main()
