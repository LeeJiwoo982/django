# 11663 선분 위의 점
'''
문제
일차원 좌표상의 점 N개와 선분 M개가 주어진다. 이때, 각각의 선분 위에 입력으로 주어진 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N과 선분의 개수 M이 주어진다. (1 ≤ N, M ≤ 100,000) 둘째 줄에는 점의 좌표가 주어진다. 두 점이 같은 좌표를 가지는 경우는 없다. 셋째 줄부터 M개의 줄에는 선분의 시작점과 끝점이 주어진다. 입력으로 주어지는 모든 좌표는 1,000,000,000보다 작거나 같은 자연수이다.

5 5
1 3 10 20 30
1 10
20 60
3 30
2 15
4 8

출력
입력으로 주어진 각각의 선분 마다, 선분 위에 입력으로 주어진 점이 몇 개 있는지 출력한다.

3
2
4
2
0
'''

import sys
input = sys.stdin.readline

def lower_bound(arr, target):
	'''타겟 이상이면 right=mid'''
	left, right = 0, len(arr)
	while left < right:
		mid = (left + right) // 2
		if arr[mid] < target:
			left = mid + 1
		else:
			right = mid
	return left

def upper_bound(arr, target):
	'''타겟과 같아도 left = mid + 1'''
	left, right = 0, len(arr)
	while left < right:
		mid = (left + right) // 2
		if arr[mid] <= target:
			left = mid + 1
		else:
			right = mid
	return left
		
# 입력
N, M = map(int, input().split())
points = list(map(int, input().split()))

points.sort()

for _ in range(M):
	x, y = map(int, input().split())
	left_idx = lower_bound(points, x)
	right_idx = upper_bound(points, y)
	print(right_idx - left_idx)
	

