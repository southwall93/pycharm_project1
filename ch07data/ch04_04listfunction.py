aa= [85,100,90,70,95,90]
bb=[]
#1.리스트의 갯수를 출력
def List_Length(list):

    print(len(list))
#2. 리스트의 데이터를 바꾸지 않으면서 정렬해서 출력
def List_Sort(list):
    tmp=sorted(list)
    print(tmp)

#3. 90데이터의 위치를 출력
#aa.index(값,시작번호,끝번호)
def Find_90(list):
    n90=0;
    while True:
        if list[n90]==90:
            break
        else:
            n90+=1
    print("90의 위치: ", n90+1)

#4. 마지막 데이터를 꺼내면서 제거해보세요
def List_pop(list):
    print("마지막값: ", list[len(list)-1])
    del(list[len(list)-1])

#5. bb라는 리스트에 동일한 데이터를 가지도록 처리해보세요
def List_Paste(list):

    return list.copy()
#6. aa리스트의 내용을 지운다
def List_Clear(list):
    list.clear()
List_Length(aa)

List_Sort(aa)

Find_90(aa)

List_pop(aa)

print(aa)

bb=List_Paste(aa)
print("복사한 리스트: ", bb)

List_Clear(aa)

print(aa)