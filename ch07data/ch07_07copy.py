#별개의 새로운 리스트를 만든다. 예전에 데이터를 그대로 사용
oldList = ['짜장면']
newList=oldList

print("oldList:",oldList)
print("newList:",newList)

oldList.append("피자")

print("oldList:",oldList)
print("newList:",newList)

newList=[]

for i in range(0, len(oldList)):
    newList.append(oldList[i])

print(newList)

print(1)

