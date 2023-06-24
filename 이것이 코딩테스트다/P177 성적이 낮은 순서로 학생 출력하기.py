n = int(input())
student = [input().split() for _ in range(n)]

def setting(data):
    return data[1]

student = sorted(student, key=setting)

for name, score in student:
    print(name, end=' ')

# 답안 2
# n = int(input())
#
# array = []
# for i in range(n):
#     input_data = input().split()
#     # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
#     array.append((input_data[0], int(input_data[1])))
#
# # 키(Key)를 이용하여, 점수를 기준으로 정렬
# array = sorted(array, key=lambda student: student[1])
#
# # 정렬이 수행된 결과를 출력
# for student in array:
#     print(student[0], end=' ')

# 0625 복습답안
n = int(input())
std = []

for _ in range(n):
    name, score = input().split()
    std.append([name, score])

def setting(data):
    return data[1]

std = sorted(std, key=setting)

for name, score in std:
    print(name, end=' ')