from sys import stdin
from fractions import Fraction

def each_case(P, Q):
    r = Fraction(P, Q)
    P, Q = r.numerator, r.denominator

    if Q & (Q-1):
        return 'impossible'
    else:
        return (Q.bit_length() - P.bit_length())

T = int(stdin.readline())
for t in xrange(1,T+1):
    P, Q = map(int, stdin.readline().split('/'))
    print 'Case #{}: {}'.format(t, each_case(P, Q))
