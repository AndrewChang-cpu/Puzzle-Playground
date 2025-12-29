# Use test data as input (easier than overriding stdin)
if 'Puzzle-Playground' in __file__:
    simulated = """4
    4
    3 7 4 5
    2 1 2 4
    4
    1 2 3 4
    3 3 3 3
    2
    1 2
    10 10
    2
    10 10
    1 2
    """

    def input_generator():
        for line in simulated.split('\n'):
            yield line
    gen = input_generator()

    def input():
        return next(gen)

t = int(input())
for _ in range(t):
    n, a, b = int(input()), list(map(int, input().split())), list(map(int, input().split()))
    a.append(0)
    b.append(0)
    pairs = sorted(zip(a, b), reverse=True)
    min_time = pairs[0][0]
    traverse = 0
    for i in range(n):
        traverse += pairs[i][1]
        if traverse > min_time:
            break
        min_time = max(traverse, pairs[i + 1][0])
        # print(i, min_time, traverse)
    print(min_time)

    """
    7 5 4 3
    1 4 2 2
    """