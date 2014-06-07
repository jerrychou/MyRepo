from sys import stdin

def each_case():
    N = int(stdin.readline())
    impossible = False
    strings = [None]
    counts = []

    # first line
    for c in stdin.readline().strip():
    	if c == strings[-1]:
            counts[-1][0] += 1
        else:
            strings.append(c)
            counts.append([1] + [0]*(N-1))
    lstrings = len(strings) - 1

    for n in xrange(1, N):
        m = -1
        for c in stdin.readline().strip():
            if c != strings[m+1]:
                m += 1
            if m < lstrings and c == strings[m+1]:
                counts[m][n] += 1
            else:
                impossible = True
                break
	if m+1 != lstrings:
            impossible = True

    if impossible:
        return 'Fegla Won'

    Nmove = 0
    for count in counts:
        center = sorted(count)[N//2]   # median
        Nmove += sum(map(lambda x: abs(x - center), count))
    return Nmove

T = int(stdin.readline())
for t in xrange(1,T+1):
    print 'Case #{}: {}'.format(t, each_case())
