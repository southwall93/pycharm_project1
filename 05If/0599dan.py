
answer=0
space="   "
sd,ed=0,0

sd=int(input("시작단수:"))
ed=int(input("마지막단수:"))

for i in range(1,10):
    for j in range(sd,ed+1):
        if(i*j>=10):
            space="  "
        else:
            space = "   "

        print(j,"*",i,"=",i*j,space, end="")
    print("")
