t=int(input())
for _ in range(t):
    n=int(input())
    a=list(input())
    b=list(input())
    resultat=0

    for j in range(0,n):

        if int(b[j])==1:
            if int(a[j])==0:
                resultat+=1
                continue
            else:
                if(j>0):
                    if(int(a[j-1])==1):
                        resultat+=1
                        a[j-1]='2'
                        continue
                if j!=n-1:
                    if(int(a[j+1])==1):
                        resultat+=1
                        a[j+1]='2'
                        continue
    print(resultat)