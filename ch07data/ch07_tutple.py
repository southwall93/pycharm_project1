#tuple -> (10,20,30)-->(10,200,30)
tt1=(10,20,30)

aa=list(tt1)

aa[tt1.index(20)]=200



taa=tuple(aa)

print(taa)

