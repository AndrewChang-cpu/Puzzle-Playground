# with open("day7_input.txt", "r") as f:
#     lines = list(f.read().splitlines())
#     beams_set = set()
#     res = 0
#     for line in lines:
#         curr_beams_set = set()
#         for i in range(len(line)):
#             if line[i] == 'S':
#                 if i not in beams_set:
#                     curr_beams_set.add(i)
#             elif line[i] == '^' and i in beams_set:
#                 curr_beams_set.add(i - 1)
#                 curr_beams_set.add(i + 1)
#                 beams_set.remove(i)
#                 res += 1
#         beams_set |= curr_beams_set
#     print(res)
    
with open("day7_input.txt", "r") as f:
    lines = list(f.read().splitlines())
    beams_dp = [0] * len(lines[0])
    for line in lines:
        curr_beams_dp = beams_dp[:]
        for i in range(len(line)):
            if line[i] == 'S':
                curr_beams_dp[i] += 1
            elif line[i] == '^' and beams_dp[i]:
                curr_beams_dp[i - 1] += beams_dp[i]
                curr_beams_dp[i + 1] += beams_dp[i]
                curr_beams_dp[i] = 0
        beams_dp = curr_beams_dp
        
    print(sum(beams_dp))

    