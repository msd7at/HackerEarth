def count(A,L,R):
    if A[R]==0:
        return "EVEN"
    else:
        return "ODD"
def change(A,h):
    if A[h]==0:
        A[h]=1
    else:
        A[h]=0
    return A   
p=list(map(int,input().split()))
x=list(map(int,input().split()))
for i in range(p[1]):
    q=list(map(int,input().split()))
    if len(q)==2:
        change(x,q[1]-1)
    else:
        print(count(x,q[1]-1,q[2]-1))
