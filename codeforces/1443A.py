n = int(input())
for _ in range(n):
    t = int(input())
    for i in range(t * 2, t * 4, 2):
        print(i, end=' ')
    print()