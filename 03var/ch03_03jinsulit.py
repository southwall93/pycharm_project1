# 16진수의 FF를 10진수로 -> 255
a = 0xFF
# 8진수의 77을 10진수 -> 64
b = 0o77
# 2진수 1111 -> 15
c = 0b1111
print(a, b, c)

# 변수 a의 타입을 출력해보자
print(a, "의 타입은 ", type(a))

# -- 실수형 데이터 입력
a = 3.14
# 3.14e5 -> 3.14 * 100000 -> 314000.0
b = 3.14e5

print(a, b)

print(a, "의 타입은 ", type(a))

# 2개의 처리문을 한 줄에 사용하기 위한 ";"
a = 10; b = 20
print(a + b)

a, b = 10, 20
print(10 ** 20)

b = 3
print(a / b)
print(a % b)
#몫만 구하는 연산
print(a // b)

a = True
b = False

print(a, type(a))

a = (100 > 100)
print(a, type(a))
