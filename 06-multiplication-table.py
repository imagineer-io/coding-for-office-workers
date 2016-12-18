# 1) 사용자로부터 몇 단을 출력할 지 받을 것
# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

dan = int(input("몇 단을 출력 하시겠습니까?"))
for num in range(1, 10):
    print("{} * {} = {}".format(dan, num, dan * num))
