import random
numbers = []

for num in range(0,10):
    print("a", num+1)
    numbers.append(random.randrange(0,10))

print("생성된 리스트", numbers)

for num in range(0,10):
    if num in numbers:
        print("숫자 %d는 리스트에 있다." %num)
    if num not in numbers:
        print("숫자 %d는 리스트에 없다." % num)
