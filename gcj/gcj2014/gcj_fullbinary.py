from sys import stdin

def each_case():
    N = int(stdin.readline())
    adj_list = {n:{} for n in xrange(1, N+1)}
    adj_list[0] = {n:1 for n in xrange(1, N+1)}
    for i in xrange(N-1):
        X, Y = map(int, stdin.readline().split())
	adj_list[X][Y] = 1
	adj_list[Y][X] = 1

    update = True
    while update:
#    for i in xrange(N):   # maybe N/2 ?
        update = False
        for v, edges in adj_list.iteritems():
            for v1 in edges:
                #if len(adj_list[v1]) >= (3 if v else 2):
                max1, max2 = 0, 0
                for v2, score in adj_list[v1].iteritems():
                    if v2 != v and max2 < score:
                        if score < max1:
                            max2 = score
                        else:
                            max1, max2 = score, max1
                if max2:
                    maxTree = max1 + max2 + 1
                    if edges[v1] != maxTree:
                        edges[v1] = maxTree
                        update = True

    return N - max(adj_list[0].itervalues())
    
T = int(stdin.readline())
for t in xrange(1,T+1):
    print 'Case #{}: {}'.format(t, each_case())
