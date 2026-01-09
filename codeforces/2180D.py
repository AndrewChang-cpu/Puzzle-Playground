# Use test data as input (easier than overriding stdin)
if 'Puzzle-Playground' in __file__:
    simulated = """4
3
1 2 3
4
1 2 4 5
6
1 2 11 12 21 22
7
0 1 2 3 5 8 13
"""

    def input_generator():
        for line in simulated.split('\n'):
            yield line
    gen = input_generator()

    def input():
        return next(gen)
    
t = int(input())
for _ in range(t):
    _ = int(input())
    arr = list(map(lambda x:int(x) * 2, input().split()))
    ignore, connect = arr[0] + 1
    ignore_val = connect_val = 0
    for i in range(1, len(arr)):
        # Compare max radius before overlapping with next point vs. min radius to connect current point with last point
        # Calculate connection with last point
        # Store max and min radius that connects with last
        # If last min radius overlaps with curr, find most recent that doesn't overlap
        # If 

        """
        .  .    .  .  .
         |   |
         1   1
             | | | |
             2 1 1 2
                 |   |
                 2   2
        """