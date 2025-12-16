from collections import deque
from functools import lru_cache
import numpy as np
import ast

with open('day10_input copy.txt') as f:
    lines = f.read().splitlines()

def preprocess_buttons(buttons, target_arr):
    """Return a sorted list of (mul, np.array) transformed button vectors.

    For each input button (tuple of indices), we compute the maximum multiplicity
    allowed by the target and produce vectors for mul=1..max_mul.
    """
    transformed = []
    for b in buttons:
        # maximum times we can press this button without exceeding target at any index
        if len(b) == 0:
            continue
        max_mul = min(int(target_arr[i]) for i in b)
        for mul in range(1, max_mul + 1):
            arr = np.zeros_like(target_arr)
            arr[list(b)] = mul
            transformed.append((mul, arr))
    # sort heuristically by mul descending (try larger chunks first)
    transformed.sort(key=lambda x: x[0], reverse=True)
    return transformed


@lru_cache(None)
def backtrack(state_tuple, button_idx):
    """Backtracking with memoization. state_tuple is a tuple of ints."""
    if state_tuple == target_tuple:
        return 0
    if button_idx >= len(buttons_np):
        return float('inf')

    state_arr = np.array(state_tuple, dtype=int)

    mul, btn_arr = buttons_np[button_idx]
    # try taking this transformed button (adds btn_arr, costs mul)
    new_state_arr = state_arr + btn_arr
    if np.any(new_state_arr > target_arr):
        # cannot take this transformed button; skip to next
        return backtrack(state_tuple, button_idx + 1)
    new_state_tuple = tuple(new_state_arr.tolist())
    take_cost = backtrack(new_state_tuple, button_idx) + mul
    skip_cost = backtrack(state_tuple, button_idx + 1)
    return min(take_cost, skip_cost)


res = 0
for line in lines:
    i1 = line.index(']')
    i2 = line.index('{')
    lights = line[1:i1]
    button_tokens = line[i1+1:i2].strip().split()
    target_tuple = tuple(map(int, line[i2+1:-1].strip().split(',')))
    target_arr = np.array(target_tuple, dtype=int)

    # safe parsing of button tokens
    buttons = []
    for b in button_tokens:
        v = ast.literal_eval(b)
        if isinstance(v, int):
            buttons.append((v,))
        else:
            buttons.append(tuple(v))

    buttons_np = preprocess_buttons(buttons, target_arr)
    # clear cache since target/buttons change per machine
    backtrack.cache_clear()
    s = backtrack(tuple(0 for _ in range(len(target_tuple))), 0)
    print(s)
    res += s
print(res)