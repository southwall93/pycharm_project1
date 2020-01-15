salesList=['삼각김밥','바나나','도시락','삼각김밥','도시락','삼각김밥','삼각김밥']
a,b,c=0,0,0
for t in salesList:
    if t=='삼각김밥':
        a+=1
    elif t=='바나나':
        b+=1
    elif t=='도시락':
        c+=1

print("삼각김밥%d개, 바나나%d개, 도시락%d개" %(a,b,c))

set(salesList)

for i in set(salesList):
    print("%s의 판매갯수: %d" %(i,salesList.count(i)))

mySet1={1,2,3,4,5}
mySet2={4,5,6,7}
#교집합 합집합 차집합 대칭차칩합
print(mySet1 & mySet2)
print(mySet1 | mySet2)
print(mySet1 - mySet2)
print(mySet1 ^ mySet2)


#1~5까지의 데이터로 list를 만들어보세요
list1=[]
for i in range(1,6):
    list1.append(i)

print(list1)

list2=[num for num in range(1,8)]

print(list2)

#1~10사이 3의 배수로 리스트 만들기
list3=[num for num in range(1,10+1) if num %3 ==0]

print(list3)

#리스트명 = [ 수식 for num in range(a,b) 조건]
#1~5사이의 데이터를 제곱을 구해서 리스트로 만들기

list4=[num*num for num in range(1,5+1)]

print(list4)

foods=['떡볶이','짜장면','라면','피자']
sides=['오뎅','단무지','김치']

flength=len(foods)
slength=len(sides)
maxlength=flength
if slength>maxlength:
    maxlength=slength


try:
    for i in range(0,len(foods)):
        print(foods[i],sides[i])
except:
    print()

#zip함수를 이용해서 튜플 리스트 딕셔너리 만들기기
tupList = list(zip(foods,sides))

print(tupList)

dic = dict(zip)