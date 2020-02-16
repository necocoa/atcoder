n, k = map(int, input().split())
ar = list(map(int, input().split()))

cnt = n - 1
ps = []
for a in ar:
    for num in range(cnt):
        ps.append(a * ar[-(num + 1)])
    cnt -= 1

ans = sorted(ps)
print(ans[k-1])
