n = int(input())
a = map(int, input().split())

d = [i for i in a if i % 2 == 0]
for num in d:
    if num % 3 != 0 and num % 5 != 0:
        print('DENIED')
        exit()
print('APPROVED')
