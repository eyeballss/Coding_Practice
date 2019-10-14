'''
문제 : https://practice.geeksforgeeks.org/problems/sum-of-bit-differences/0
코드 설명 :
 주어진 리스트에서 모든 쌍을 만들어 XOR 연산을 하면
 다른 bit 만큼 1로 바뀐다.
 bit 가 1인 mask 를 만들고<< 로 1의 위치를 바꿔가며 & 연산 한다.
 양수가 나오는 횟수를 누적해주면 1의 개수를 알 수 있게 된다.
 마지막에 2 를 곱하는 이유는,
 가령 쌍이 (1,3) 이라고 했을 때 (3,1) 도 나올 수 있는데
 두 쌍 모두 계산하면 결과값은 똑같아서
 하나만 계산한 후 2배를 하여 쓸데 없는 계산을 피하기 위함이다.
'''

#code
def cal(n):
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            x = arr[i]^arr[j]
            mask = 1
            for m in range(0, 7):
                if x&mask > 0 :
                    sum+=1
                mask=mask<<1
    print(sum*2)

case = int(input())
for i in range(0,case):
    cal(int(input()))
