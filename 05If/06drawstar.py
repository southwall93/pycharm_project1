n=int(input("별의 줄 갯수를 설정하세요"))

for i in range(1,2*n):
    if i<n+1:
        for j in range(1,n-i+1):
            print(' ',end='')
        for j in range(1,2*i):
            print("\u2605",end='')
        for j in range(1,n-i+1):
            print(" ",end='')
    else:
        for j in range(1,i-n+1):
            print(" ",end='')
        for j in range(1,2*(2*n-i)):
            print("\u2605",end='')
        for j in range(1,i-n+1):
            print(" ",end='')

    print()