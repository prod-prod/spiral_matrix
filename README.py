# spiral_matrix
n=int(input())
a=[[0 for j in range(n)] for i in range(n)]
k=1
s=0
for j in range(s,n):
    for i in range(s,n):
       
         if k!=n*n:
            for j in range(s,n):
                if a[i][j]==0 :
                    a[i][j]+=k
                    k+=1
            for i in range(s+1,n):
                        if a[i][j]==0:
                            a[i][j]+=k
                            k+=1

            for j in range(n-1,s-1,-1):
                                if a[i][j]==0 :
                                    a[i][j]+=k
                                    k+=1
                            
            for i in range(n-2,s-1,-1):
                                    if a[i][j]==0:
                                        a[i][j]+=k
                                        k+=1 
            n-=1
            s+=1
for x in a:
        print(*x)
