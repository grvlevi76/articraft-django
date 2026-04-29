n,m= map(int,input().split())
 
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,m+1):
            print('#',end='')
        print()
    else:
        for j in range(1,m+1):
            if j==m:
                print('#')
            else:
                print('.',end='')