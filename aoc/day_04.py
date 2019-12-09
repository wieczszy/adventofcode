def has_double(D):
    D = [int(d) for d in str(D)]
    P = any([i==j for i,j in zip(D, D[1:])]) 
    C = [D.count(d) for d in set(D)]
    if P and 2 in C:
        return True
    return False

def is_increasing(D):
    D = [int(d) for d in str(D)]
    return all([i<=j for i,j in zip(D, D[1:])])

R = [int(x) for x in '136760-595730'.split('-')]
A = [x for x in range(R[0], R[1])]
I = [a for a in A if is_increasing(a)]
D = [i for i in I if has_double(i)]

print(len(D))