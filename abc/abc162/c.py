import math

def main():
    k = int(input())
    ans = 0
    for a in range(k):
        for b in range(k):
            for c in range(k):
                ans += math.gcd(math.gcd(a+1, b+1), c+1)
    print(ans)


if __name__ == '__main__':
    main()
