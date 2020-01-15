#-*-coding: utf-8-*-

var1=var2=var3=var4=200

print(var1, var2, var3, var4)

sel= int(input('입력 진수 결정'));

#선택한 진수에 해당되는 값 입력
num= input('값 입력: ')
print("numtype ==>", type (num))
#조건문에서 sel의 입력된 값에 따라 10진수로 변환을 해준다
if sel == 16:
    num10=int(num, 16)
if sel == 10:
    num10=int(num, 10)
if sel == 8:
    num10=int(num, 8)
if sel == 2:
    num10=int(num, 2)


#num10의 변수에 10진수값 저장
print("16진수: ", hex(num10))
print("10진수: ", num10)
print("8진수: ", oct(num10))
print("2진수: ", bin(num10))