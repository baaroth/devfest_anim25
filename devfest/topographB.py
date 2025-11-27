*l,=open(0)

data = {}
starts,ends = set(),set()
for j in range(len(l)):
    for i in range(len(l[0].strip())):
        data[(i,j)] = int(l[j][i])
        if data[(i,j)] == 0: starts.add((i,j))
        if data[(i,j)] == 9: ends.add((i,j))

def step(a):
    a = a[0] + a[1] * 1j
    for i in(-1j, 1j, -1, 1):
        k = a + i
        t = (k.real,k.imag)
        if t in data: yield t

def hike(start):
    queue = [start]
    score_p1,score_p2 = set(),0
    while queue:
        curr = queue.pop(0)
        if curr in ends:
            score_p1.add(curr)
            score_p2 += 1
        for new in step(curr):
            if data[new] == data[curr]+1:
                queue.append(new)
    return len(score_p1),score_p2

score_p1 = score_p2 = 0
for start in starts:
    p1,p2 = hike(start)
    score_p1 += p1
    score_p2 += p2
print("Part 1:", score_p1)
print("Part 2:", score_p2)