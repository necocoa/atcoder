from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans_hash = {}
    num_hash = {}
    for n in A:
        if n not in ans_hash:
            ans = 0
            a = A[:]
            i = a.index(n)
            del a[i]
            val = Counter(a).values()
            for num in val:
                if num in num_hash:
                    ans += num_hash[num]
                else:
                    num_hash[num] = num * (num - 1) // 2
                    ans += num_hash[num]
            ans_hash[n] = ans
        print(ans_hash[n])


if __name__ == '__main__':
    main()
