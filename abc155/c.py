from collections import Counter
n = int(input())
a = [input() for i in range(n)]

c = Counter(a)
d = c.most_common()
ans = []
for i in c.items():
    if i[1] == d[0][1]:
        ans.append(i[0])
for i in sorted(ans):
    print(i)
