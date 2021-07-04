def main():
    n = int(input())
    ans_dist = {}
    for _ in range(n):
        ans_dist[input()] = 0
    print(len(ans_dist.keys()))


if __name__ == '__main__':
    main()
