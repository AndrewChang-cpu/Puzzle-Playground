s ="96952600-96977512,6599102-6745632,32748217-32835067,561562-594935,3434310838-3434398545,150-257,864469-909426,677627997-677711085,85-120,2-19,3081-5416,34-77,35837999-36004545,598895-706186,491462157-491543875,5568703-5723454,6262530705-6262670240,8849400-8930122,385535-477512,730193-852501,577-1317,69628781-69809331,2271285646-2271342060,282-487,1716-2824,967913879-967997665,22-33,5722-11418,162057-325173,6666660033-6666677850,67640049-67720478,355185-381658,101543-146174,24562-55394,59942-93946,967864-1031782"
s = list(map(lambda x:list(map(int, x.split("-"))), s.split(",")))
s.sort()
print(len(s))

def in_interval(intervals, point):
    for interval in intervals:
        if interval[0] <= point <= interval[1]:
            return True
    return False

res = 0
seen = set()
for i in range(1, 100000):
    base = str(i) 
    for mul in (2, 3, 5, 7):
        if mul * len(base) > 10:
            continue
        query = int(base * mul)
        if query in seen:
            continue
        seen.add(query)
        if in_interval(s, query):
            res += query
print(res)