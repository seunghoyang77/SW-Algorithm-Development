# 양승호_문제1.py
# 문제 1. 계단 오르는 방법의 수 계산 (Bottom-up DP)

def count_ways_to_climb(n):
    """
    계단 n개를 오르는 방법의 수를 Bottom-up 방식으로 계산하는 함수
    :param n: 계단의 개수 (정수)
    :return: 방법의 수
    """
    # 계단이 0개 이하인 경우 (예외 처리)
    if n <= 0:
        return 0
    
    # 계단이 1개인 경우: 1가지
    if n == 1:
        return 1
    
    # 계단이 2개인 경우: 2가지 (1+1, 2)
    if n == 2:
        return 2

    # DP 테이블 생성 (인덱스를 1부터 n까지 사용하기 위해 n+1 크기로 할당)
    dp = [0] * (n + 1)

    # 초기값 설정 (Base Cases)
    dp[1] = 1
    dp[2] = 2

    # 3번째 계단부터 n번째 계단까지 점화식 적용 (Bottom-up)
    # 점화식: dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 메인 실행 블록
if __name__ == "__main__":
    try:
        # 1. 사용자에게 계단 수 n을 입력받는다.
        user_input = input("계단의 개수를 입력하시오: ")
        n = int(user_input)
        
        # 2. 동적계획법을 이용하여 계산한다.
        result = count_ways_to_climb(n)
        
        # 4. 계산된 결과를 화면에 출력한다.
        print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")
        
    except ValueError:
        print("올바른 정수를 입력해주세요.")
