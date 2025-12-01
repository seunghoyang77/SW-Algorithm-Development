# 양승호_문제2.py
# 문제 2. 여행 짐 꾸리기 (0/1 배낭 문제, Bottom-up DP + 역추적)

def solve_knapsack(capacity):
    """
    0/1 배낭 문제를 해결하여 최대 만족도와 선택된 물건 목록을 반환하는 함수
    :param capacity: 배낭의 최대 용량 W (kg)
    :return: (최대 만족도, 선택된 물건 리스트)
    """
    # 물건 데이터 정의: (이름, 무게, 만족도)
    # 인덱스 편의를 위해 0번 인덱스는 더미(None) 처리하거나, 로직에서 i-1로 접근
    items = [
        ("노트북", 3, 12),        # 1번
        ("카메라", 1, 10),        # 2번
        ("책", 2, 6),             # 3번
        ("옷", 2, 7),             # 4번
        ("휴대용 충전기", 1, 4)   # 5번
    ]
    
    n = len(items)
    
    # 1. DP 테이블 초기화 (행: 물건 개수 0~n, 열: 배낭 용량 0~W)
    # A[i][w] = i번째 물건까지 고려했을 때, 무게 w에서의 최대 만족도
    A = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 2. Bottom-up 방식으로 DP 테이블 채우기
    for i in range(1, n + 1):
        name, weight, value = items[i-1] # 현재 물건 정보 (리스트는 0부터 시작하므로 i-1)
        
        for w in range(1, capacity + 1):
            if weight > w:
                # 현재 물건이 배낭 용량보다 무거우면 넣을 수 없음 -> 이전 상태 유지
                A[i][w] = A[i-1][w]
            else:
                # 넣지 않는 경우 vs 넣는 경우 중 더 큰 가치 선택
                val_without = A[i-1][w]
                val_with = value + A[i-1][w - weight]
                A[i][w] = max(val_without, val_with)
    
    max_satisfaction = A[n][capacity]

    # 3. 역추적 (Backtracking)하여 선택된 물건 찾기
    selected_items = []
    curr_w = capacity
    
    # 마지막 물건부터 거꾸로 확인
    for i in range(n, 0, -1):
        # 현재 값이 바로 위 행의 값과 다르다면, 현재 물건(i)이 선택된 것임
        if A[i][curr_w] != A[i-1][curr_w]:
            name, weight, value = items[i-1]
            selected_items.append(name)
            curr_w -= weight # 남은 용량 갱신

    # 역추적 결과는 역순으로 담기므로 보기 좋게 뒤집을 수도 있으나, 
    # 문제 예시는 순서가 섞여 있으므로 그대로 두거나 정렬 가능.
    # 여기서는 발견된 순서대로 리스트를 반환합니다.
    
    return max_satisfaction, selected_items

if __name__ == "__main__":
    try:
        # 사용자 입력
        w_input = input("배낭 용량을 입력 하세요 : ")
        W = int(w_input)
        
        if W < 0:
             print("용량은 0 이상의 정수여야 합니다.")
        else:
            # 알고리즘 수행
            max_val, selected_list = solve_knapsack(W)
            
            # 결과 출력
            print(f"최대 만족도: {max_val}")
            # 출력 예시 형식에 맞춤 (리스트 출력)
            print(f"선택된 물건: {selected_list}")
            
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
