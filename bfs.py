# Breadth first traversal of a undirected unweighted graph
n,root=map(int,input().split())
l=[]
l.append(0)
x=[]
queue=[]
result=[]
queue.append(root)
result.append(root)
var=root
for i in range(0,n):
    x=list(map(int,input().split()))
    l.append(x)
while(len(result)!=n):
    flag=0
    for j in range(0,n):
        if((l[var][j]==1)and((j+1)not in result)):
            flag=1
            queue.append(j+1)
            result.append(j+1)
    if(len(result)==n):
        break
    if(len(queue)==1):
        break
    queue=queue[1:]
    var=queue[0]
print(*result)
