# Use test data as input (easier than overriding stdin)
if 'Puzzle-Playground' in __file__:
    simulated = """4
3
1 2 1
5
11 7 9 6 8
5
1 3 1 3 1
4
5 2 1 10
"""

    def input_generator():
        for line in simulated.split('\n'):
            yield line
    gen = input_generator()

    def input():
        return next(gen)
    
"""
11 7 9 6 8
subtract from left 11 7 7 6 6
eq 0 0 2 0 2

subtract from left 11 7 7 4 4
eq 0 0 2 2 4

subtract from right 6 6 6 6 8
eq 5 1 3 0 0

subtract from right 8 4 6 6 8
eq 3 3 3 0 0

11 2 9 6 8
 -9 7 -3 2

11 7 9 6 8
 -4 2 -3 2
"""

t = int(input())
for _ in range(t):
    _ = int(input())
    arr = list(map(int, input().split()))

    max_subtract = 1000000
    min_remaining = 0
    valid = True
    for n in arr:
        if min_remaining > n:
            valid = False
            break
        # example: subtract 6, remaining 2, n 7
        if max_subtract < n:
            min_remaining = max(min_remaining, n - max_subtract)
        if n - max_subtract < min_remaining:
            max_subtract = n - min_remaining
    print('YES' if valid else 'NO')