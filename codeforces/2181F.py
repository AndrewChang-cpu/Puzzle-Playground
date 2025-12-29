"""
10 5 5
10 x 5

10 5 1

1 2 2
1 2 x
bob wins

1 1 1 2
bob wins

1 2
bob wins

1
alice wins

1 1
bob wins

1 1 2
alice wins

1 1 2 2 2
x x 2 2 2
or
1 1 2 2 2
1 1 2 1 x
1 1 1 x x
x x 2 2 x
alice wins?

1 1 2 2
1 1 2 x
1 x 2 x

"""

def solve(piles):
    ones = piles.count(1)
    nonones = len(piles) - ones
    if ones % 2:
        print('Bob' if bool(nonones) else 'Alice')
    else:
        print('Alice' if bool(nonones) else 'Bob')

n = int(input())
for _ in range(n):
    _, piles = input(), list(map(int, input().split()))
    solve(piles)