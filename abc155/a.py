a, b, c = map(int, input().split())
if a == b == c:
    print('No')
    exit()
if a != b and b != c and a != c:
    print('No')
    exit()
print('Yes')
