'''
문제 : https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
코드 설명 :
 array 를 받아서 정렬한 후 k-1 번째 값을 print 한다.
'''


n = int(input())
l = list(map(int, input().split()))
l.sort()
print(l[int(input())-1])
