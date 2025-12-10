#============================================================================================
#  알고리즘 설계 기법 : 분할과 정복 (Divide & Conquer)
#============================================================================================
#  1. 배열(arr)의 합 문제 : 억지기법 vs. 분할 정복

def sum_bf(arr): # 시간복잡도 - O(n), n = len(arr), 공간복잡도 - O(1)
    """억기기법 - 단순 반복문"""
    total = 0
    for x in arr:
        total += x
    return total

def sum_dc(arr,left, right): # 시간복잡도 - O(n) , 시스템 스택 호출 - (n)
    """분할정복 기반 재귀함수"""
    # 원소가 한 개인 경우 -> 이미 정복
    if left == right :
        return arr[left] # 종료 조건
    # 원소가 2개 이상인 경우 반으로 나누기
    mid = (left + right) // 2 
    # 왼쪽 부분문제 배열의 합
    left_sum = sum_dc(arr,left, mid)
    # 오른쪽 부분문제 배열의 합
    right_sum = sum_dc(arr,mid + 1, right)
    # 병합 (두 개의 부분문제의 결롸를 합침)
    return left_sum + right_sum

# 테스트
arr = [5, 3, 8, 4, 1, 6, 2, 7]
print("Iterative Sum =", sum_bf(arr))
print("Divide & Conquer Sum =", sum_dc(arr, 0, len(arr) - 1))
print("="*100)

#=========================================================================
# 2. 거듭제곱 계산 문제 : 억지기법 vs.분할(축소)정복
def power_bf(x,n): # x^n = x*x*...*x
    """억지기법 반복문 구조 : O(n)"""
    result = 1.0
    for _ in range(n):
        result *= x # x를 n번 곱함
    return result

def power_dc(x, n):
    """DC의 축소 정복 기반 재귀 구조 : O(logn)"""
    if n ==  1: # 종료 조건
        return x
    elif n % 2 == 0: # n이 짝수
        return power_dc(x*x, n//2) # 재귀호출 - 절반 크기로 감소 - O(logn)
    else : # n이 홀수
        return x * power_dc(x*x, (n-1)//2) # 재귀호출 - 절반 크기로 감소 - O(logn)
    
# 테스트 코드
x = 2.0
n = 10
print(f"억지기법_ x의 n 거듭제곱({x}, {n}) = {power_bf(x, n)}")
print(f"축소정복_ x의 n 거듭제곱({x}, {n}) = {power_dc(x, n)}")
print("="* 100)

#==============================================================================
# 3. k번째 최소값(k-th smallest element) 찾기 문제
def partition_left(A, left, right): # pivot = A[left] 기준 분할
    pivot = A[left] # pivot 설정
    i = left + 1 # 왼쪽 포인터
    j = right # 오른쪽 포인터

    while True: 
        while i <= j and A[i] <= pivot: # 왼쪽에서부터 pivot보다 큰 값 찾기
            i += 1       # 오른쪽으로 이동
        while i <= j and A[j] > pivot: # 오른쪽에서부터 pivot보다 작은 값 찾기
            j -= 1     # 왼쪽으로 이동
        if i > j:   # 포인터가 엇갈리면 종료
            break
        A[i], A[j] = A[j], A[i] # 교환
        
    # pivot을 j 위치로 이동
    A[left], A[j] = A[j], A[left]
    return j    # pivot의 최종 위치

# 억지기법  : 정렬 이용 
def kth_smallest_bf(arr, k):
    B = sorted(arr)          # O(n log n)
    return B[k-1]            

# 최소분할정복 (pivot = A[left]) : 재귀기법 - 퀵정렬과 비슷 
def quick_select(A, left, right, k):
    if left == right:    # 요소 1개 남았을 때 - 종료 조건
        return A[left]   

    pos = partition_left(A, left, right) # 분할
    # Case 1: 피벗이 k번째 작은 값인 경우
    if k + left == pos + 1 :          
        return A[pos]
    # Case 2: k번째 작은 값이 왼쪽 부분에 있는 경우
    elif k + left < pos + 1 :              
        return quick_select(A, left, pos - 1, k) 
    # Case 3: 오른쪽 부분에서 찾는 경우
    else:          
        return quick_select(A, pos + 1, right, k - (pos + 1 - left)) 


# 테스트 코드
A1 = [7, 2, 1, 8, 6, 3, 5, 4, 0]
A2 = A1.copy()
k = 3  # 3번째 최소값은 3
print("재귀 Quick-Select:", quick_select(A1, 0, len(A1)-1, k))
print("억지기법 Quick-Select:",kth_smallest_bf(A2, k))
print("="*100)

#==============================================================================
# 4. 병합정렬(Merge Sort) 
def merge(A, left, mid, right):
    # A: 정렬할 리스트
    # left: 왼쪽 부분 리스트의 시작 인덱스
    # mid: 왼쪽 부분 리스트의 끝 인덱스
    # right: 오른쪽 부분 리스트의 끝 인덱스
    # A[left..mid]와 A[mid+1..right]는 이미 정렬된 상태 -> 이를 하나의 정렬된 리스트 A[left..right]로 병합
    
    # 1. 임시 리스트 생성 - 크기 = right - left + 1
    sorted_list = [0] * (right - left + 1)  

    # 2. 두 부분 리스트의 시작 인덱스
    i = left        # 왼쪽 부분리스트 시작 index
    j = mid + 1     # 오른쪽 부분리스트 시작 index
    k = 0           # 임시 리스트 sorted_list index

    # 3. 두 정렬 리스트를 비교하며 작은 값을 sorted_list에 채움
    while i <= mid and j <= right: # 양쪽 리스트에 원소가 남아 있을 때 
        if A[i] <= A[j]:    # 왼쪽 원소가 더 작으면
            sorted_list[k] = A[i]   # 왼쪽 원소를 복사
            i += 1      # 왼쪽 포인터 이동
            k += 1        # sorted_list 포인터 이동 

        else:           # 오른쪽 원소가 더 작으면
            sorted_list[k] = A[j]    # 오른쪽 원소를 복사
            j += 1   # 오른쪽 포인터 이동
            k += 1        # sorted_list 포인터 이동 

        
    # 4. 왼쪽 부분이 남아 있으면 모두 복사
    while i <= mid:  
        sorted_list[k] = A[i]  # 왼쪽 원소 복사
        i += 1    # 왼쪽 포인터 이동
        k += 1   # sorted_list 포인터 이동

    # 4. 오른쪽 부분이 남아 있으면 모두 복사
    while j <= right:   
        sorted_list[k] = A[j]  # 오른쪽 원소 복사
        j += 1  # 오른쪽 포인터 이동
        k += 1   # sorted_list 포인터 이동

    # 5. 결과를 원래 A 리스트에 덮어쓰기
    for t in range(k): 
        A[left + t] = sorted_list[t]  

def merge_sort(A, left, right):  # 병합정렬 함수
    # A: 정렬할 리스트, left: 정렬할 부분 리스트의 시작 인덱스, right: 정렬할 부분 리스트의 끝 인덱스
    
    if left < right:                      # 항목이 2개 이상일 때만 분할 - O(log n) 깊이
        mid = (left + right) // 2         # 반으로 나누기

        # 왼쪽 부분  정렬
        merge_sort(A, left, mid)      

        # 오른쪽 부분 정렬
        merge_sort(A, mid + 1, right)

        # 정렬된 두 부분을 병합
        merge(A, left, mid, right)      
    else:     
        pass                           #항목이 1개면 이미 정렬된 상태 (더 이상 할 일 없음)

# 테스트 코드
A = [38, 27, 43, 3, 9, 82, 10]
print("정렬 전:", A)
merge_sort(A, 0, len(A) - 1)
print("정렬 후:", A)
print("="*100) 

#==============================================================================
# 알고리즘 설계 전략 - 동적계획법(DP, Dynamic Programming) 알고리즘
# ==============================================================================
# 1.피보나치 수열
# 1-1. 피보나치 수열 : 메모이제이션 기반 피보나치 함수이다.
# 재귀 구조 - top-down(하향식) 방식 : 주어진 문제에서 작은 문제로 해결해 나가는 방식

# 메모이제이션 배열 준비 (0~10까지)
# 전역변수
mem = [None] * 11

def fib_dp_mem(n):
    if mem[n] is None:
        if n < 2:         # 처음 계산하는 값이면 저장 
            mem[n] = n    # F(0)=0, F(1)=1
        else:             # 그렇지 않으면 - 중복 계산 피함
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]         # (n + 1)번째 피보나치 숫 반환

# 테스트
print("n = 6일 때 ", fib_dp_mem(6))
print("mem =", mem[:7]) # 결과 출력 (0~6 인덱스만)
print()

# 1-2. 피보나치 수열 : : 테이블화 기반 피보나치 함수이다.
# 반복문 배열 기반- bottom-up (상향식)방식 : 작은 부분 문제부터 해결하여 큰 문제을 해결해 나가는 방식

# 테이블 생성
def fib_dp_tab(n):
    # 1차원 테이블 준비
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1

    # Bottom-up 방식으로 테이블 채우기
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table

# 테스트 : fib_dp_tab(6) 실행
table = fib_dp_tab(6)
print(table[6]) 
print("table =", table[:7]) # # 0~8 인덱스 출력
print("="*100)

#==================================================================
# 2. 0/1 배낭 문제 DP 구현 - 물건의 개수는 n, 배낭의 용량은 W
# DP 테이블 A[i][w] (주어진 남아있는 배낭 용량 w에서 1부터 i 물건을 까지 고려했을 때 얻어지는 배낭의 최대 가치)을 완성.
# 최종 출력값 A[n][W]는 "최대 가치"만 알려줄 뿐, 어떤 물건들을 선택해야 이 값을 만들 수 있는지 알려주지 않음.
"""
동작 방식 요약 : 
1. i: 위에서 아래로, 물건 1개 → n개
2. w: 왼쪽에서 오른쪽으로, 용량 0 → W
3. 각 칸에서 현재 물건의 무게와 남아 있는 배낭의 용량의 크기을 비교해서
- 넣을 수 없으면 위 값 복사
- 넣을 수 있으면
    - 넣는 경우
    - 안 넣는 경우 
    → 더 큰 값으로 갱신
4. 테이블 오른쪽 아래 A[n][W]가 최종 해답
"""
def knapSack_dp(W, wt, val, n):
    # 1. DP 테이블 초기화 : (n+1) X (W + 1)
    A = []
    for i in range(n + 1):          # 행 생성 (0 ~ n)
        row = []
        for w in range(W + 1):      # 열 생성 (0 ~ W)
            row.append(0)           # 모든 값을 0으로 초기화
        A.append(row)

    # 2. DP 테이블 채우기
    for i in range(1, n + 1):       # 물건 index 1~n - 위에서 아래로 진행
        for w in range(1, W + 1):   # 배낭 용량 1~W - 좌에서 우로 진행
            if w < wt[i-1]:         # i번째 물건이 용량 초과해서  넣을 수 없으므로 위 값 복사
                A[i][w] = A[i-1][w]
            else:                   # i번째 물건을 넣을 수 있으면
                valWith = val[i-1] + A[i-1][w - wt[i-1]]  # 넣는 경우
                valWithout = A[i-1][w]                    # 빼는 경우
                A[i][w] = max(valWith, valWithout)        # 더 큰 값을 선택
    
    # 3. 최대 가치와 DP테이블 A 둘 다 반환
    return A[n][W], A


# 테스트 
n = 3
wt = [2, 1, 3]
val = [12, 10, 20]
W = 5

max_value, A = knapSack_dp(W, wt, val, n)

print("1. 최대 가치 =", max_value)
print()
print("2. DP table")
for i in range(4):
    for w in range(6):
        print(A[i][w],  end = "   ")
    print()

print()
print("3. 선택된 물건 역추적 기능")
"""
선택된 물건의 무게만큼 용량을 줄이고, DP 테이블에서 위로 올라가며 계속 확인한다.
"""
selected = []
w = W
# 물건 데이터
items = [("item1", 2, 12), ("item2",1, 10),("item3",3, 20)]

for i in range(n, 0, -1): # DP 테이블을 거꾸로 올라가며 선택된 물건을 하나씩 찾아내는 과정이 필요
    if A[i][w] != A[i-1][w]:         # i번째 물건은 선택되어 가방에 들어감
        name, wt, val = items[i-1]   # i번째 물건을 리스트에 추가
        selected.append(name)  
        w -= wt                      # i번째 물건을 배낭에 넣었으므로 배낭의 용량에서 그 무게만큼 줄어든다.
                                     # 줄어든 나머지 용량 w에서 앞선 물건(i-1번째까지)으로 최대 가치를 만드는 방법 고려
    else:
        pass

selected.reverse()
print("선택된 물건:", selected)
