from sys import stdin

def each_case(K, L, S, keyboard, target):
    E = float((S-L+1) * reduce(lambda p, t: p * keyboard.count(t), target, 1)) / float(K**L)
    if E == 0:
        return 0.

    for t in xrange(1, L):
        if target[t:] == target[:-t]:
            return (S-L) / t + 1 - E

    return S / L - E

T = int(stdin.readline())
for t in xrange(1,T+1):
    K, L, S = map(int, stdin.readline().split())
    keyboard = stdin.readline()[:K]
    target = stdin.readline()[:L]
    print 'Case #{}: {}'.format(t, each_case(K, L, S, keyboard, target))
