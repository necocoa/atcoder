def main():
    n, a, b = map(int, input().split())
    ab = a + b
    k = n // ab
    m = n % ab
    ans = k * a
    ans += min(m, a)
    print(ans)

if __name__ == '__main__':
    main()
