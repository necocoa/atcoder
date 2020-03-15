def main():
    a, b = map(int, input().split())
    ans = (a * b) // 2
    ans += (a * b) % 2
    print(ans)

if __name__ == '__main__':
    main()
