n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))

print('A: %s' % A)

cnt = n - 1
ans = []

i = 0
count = 0
for a in A:
    for num in range(cnt):
        ans.append(a * A[i + num + 1])
        count += 1
        if k == count:
            break
    else:
        i += 1
        cnt -= 1
        continue
    break

print('count: %s' % count)
print('ans: %s' % ans)
sorted_ans = sorted(ans)
print(sorted_ans[k-1])
