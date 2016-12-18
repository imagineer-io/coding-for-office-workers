# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# list []
print("list")
list_a = [1, 2, 3]
print(list_a)
print(type([1, 2, 3]))
# index는 0부터 시작합니다.
print(list_a[0])
print(list_a[1])
print(list_a[2])
# slice
print(list_a[0:2])
list_a.append(4)
print(list_a)
list_a.remove(2)
print(list_a)
list_a.clear()
print(list_a)

# tuple (1, )
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))
# tuple은 한 번 생성 후 내부 값 변경 불가
# tuple_a.append(4)

# dict (map) {}
# key & value
dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])
# edit value
dict_a["pen"] = "something to write"
print(dict_a)

# set set([])
set_a = set([1, 2, 3])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

# 중복 제거!
# 집합 - 교집합, 합집합, 차집합, 여집합
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
