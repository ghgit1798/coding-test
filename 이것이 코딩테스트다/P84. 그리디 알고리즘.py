import sys
from collections import deque

input = sys.stdin.readline


'''
정렬을 빠르게 하려면 -> 정렬알고리즘
최단 경로를 빠르게 찾으려면 -> 플로이드 워셜, 다익스트라 알고리즘
 - 다익스트라 알고리즘은 사실상 암기가 필요한 그리디 알고리즘
 - 그리디 알고리즘 & 정렬은 세트
 - 문제 유형 파악이 어렵다면 그리디 알고리즘 의심!
'''

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
