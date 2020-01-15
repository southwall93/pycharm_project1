#dictionary -> {key:value[, key:value]} ->js : json 형식

#마지막 키 값이 적용
dic1={1:'a',2:'b',3:'c',3:'e'}

print(dic1,type(dic1))

#학생 딕셔너리 생성
student={"학번":1000, "이름":"홍길동", "학과":"파이썬학과"}
print(student, type(student))


#학생의 이름 데이터 가져오기(순수한 리스트는 아님)
print(student["이름"])
print(student.get("이름"))

#모든 키를 출력해보자
keylist=student.keys()
print(keylist)

valuelist=student.values()
print(valuelist)

#학생 딕셔너리가 가지고 있는 모든 데이터 출력해보기
for a in keylist:
    print(a, ":", student[a])

#keylist를 리스트로 변환
keylist=list(keylist)
print(keylist)

studentlist=list(student.items())

print(studentlist)

#딕셔너리의 데이터 추가
singer={}
singer["이름"]="트와이스"

print(singer)

food={"떡볶이":"오뎅",
    "짜장면":"단무지",
    "라면":"김치",
    "피자":"피클",
    "맥주":"땅콩",
    "치킨":"치킨무",
      }

while True:
    a=input("음식명을 입력해주세요:")
    if a in food:
        print(a,"와 어울리는 음식은 ",food[a],"입니다")
    elif a=="끝":
        break
    else:
        print("다시 입력해주세요")

