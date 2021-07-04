import math


def main():
    a, b = map(int, input().split())
    if a >= 20:
        price = b * 10
        tax = math.floor(price * 0.08)
        if a == tax:
            print(price)
        else:
            print(-1)
    else:
        ans = []
        ary_a = [(a * 100 + i * 10) // 8 for i in range(10)]
        ary_b = [(b * 100 + i * 10) // 10 for i in range(10)]
        for n in ary_a:
            if ary_b.count(n) > 0:
                ans.append(n)
        if not ans:
            print(-1)
        else:
            print(min(ans))


if __name__ == '__main__':
    main()
