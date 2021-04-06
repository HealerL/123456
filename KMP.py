def get_next(T):
    next = [0]*(len(T)+1)
    next[0] = -1
    i = 0
    j = -1
    while i < len(T):
        if T[i]==T[j] or j ==-1:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next

def index_search(S, T):
    next_T = get_next(T)
    print(next_T)
    p = -1
    q = 0
    while q< len(S) and p < len(T):
        if p==-1 or S[q] == T[p]:
            q += 1
            p += 1
        else:
            p = next_T[p]

    if p>=len(T):
        
        return q-len(T)
    else:
        return 0


A = 'abecdefgcde'
B = 'cde'

result = index_search(A, B)
print(result)
print('test')
