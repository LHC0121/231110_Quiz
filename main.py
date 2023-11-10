import random
a = []
while len(a) < 6:
    number = random.randint(1, 45)
    if number not in a:
        a.append(number)
a.sort()
print(f"생성된 로또 번호는{a}입니다")