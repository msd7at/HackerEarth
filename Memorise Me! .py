n=int(input())
l=[0]*(1001)
x=list(map(int,input().split()))
for i in x:
    l[i]+=1
q=int(input())
for i in range(q):
    h=int(input())
    if l[h]!=0:
        print(l[h])
    else:
        print("NOT PRESENT")
