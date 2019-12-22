x=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(x):
    print(A[i]+B[i],end=" ")
