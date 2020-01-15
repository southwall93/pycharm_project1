
#숫자를 계속 더해서 더한 숫자가 100보다 커지면 빠져나가서 출력

i=1
sum=0
while True:
    sum+=i
    i+=1
    if sum>100:
        print("i: ",i-1)
        print("sum: ", sum)
        break

#1~10 출력 홀수만 출력
#1부터 시작하면서 2씩 증가
i=1

while True:
    print(i)
    i+=2
    if i>10:
        break

i=1
while True:
    if i%2==0:
        i += 1
        continue
    if i>10:
        break
    print(i)
    i+=1
