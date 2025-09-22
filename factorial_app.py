import time

def factorial_iter(n: int) -> int:
    """
    반복문을 사용하여 n의 팩토리얼을 계산합니다.
    n이 0보다 작으면 ValueError를 발생시킵니다.
    """
    if n < 0:
        raise ValueError("0 이상의 정수만 입력 가능합니다.")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_rec(n: int) -> int:
    """
    재귀 호출을 사용하여 n의 팩토리얼을 계산합니다.
    n이 0보다 작으면 ValueError를 발생시킵니다.
    """
    if n < 0:
        raise ValueError("0 이상의 정수만 입력 가능합니다.")
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)

def run_with_time(func, n):
    """
    주어진 함수의 실행 시간을 측정하고 결과와 시간을 반환합니다.
    """
    start_time = time.perf_counter()
    try:
        result = func(n)
    except Exception as e:
        result = e
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def get_user_input():
    """
    사용자로부터 0 이상의 정수 n을 입력받습니다.
    유효하지 않은 입력 시 재입력을 요청합니다.
    """
    while True:
        try:
            n_str = input("n 값(정수, 0 이상)을 입력하세요: ")
            n = int(n_str)
            if n < 0:
                print("정수(0 이상의 숫자)만 입력하세요.")
                continue
            return n
        except ValueError:
            print("정수(0 이상의 숫자)만 입력하세요.")

def main():
    """
    메인 프로그램을 실행하는 함수
    """
    while True:
        print("\n================ Factorial Tester ================")
        print("1) 반복으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        print("================================================")
        
        choice = input("선택: ")

        if choice == '1':
            n = get_user_input()
            result, elapsed_time = run_with_time(factorial_iter, n)
            print(f"[반복] {n}! = {result}")
            print(f"[반복] 시간: {elapsed_time:.6f} s")

        elif choice == '2':
            n = get_user_input()
            result, elapsed_time = run_with_time(factorial_rec, n)
            print(f"[재귀] {n}! = {result}")
            print(f"[재귀] 시간: {elapsed_time:.6f} s")

        elif choice == '3':
            n = get_user_input()
            iter_result, iter_time = run_with_time(factorial_iter, n)
            rec_result, rec_time = run_with_time(factorial_rec, n)
            
            print(f"[반복] {n}! = {iter_result}")
            print(f"[재귀] {n}! = {rec_result}")
            
            match_status = "일치" if iter_result == rec_result else "불일치"
            print(f"결과 일치 여부: {match_status}")
            
            print(f"[반복] 시간: {iter_time:.6f} s | [재귀] 시간: {rec_time:.6f} s")

        elif choice == '4':
            test_data = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]
            print("[테스트 데이터 실행]")
            for n in test_data:
                iter_result, iter_time = run_with_time(factorial_iter, n)
                rec_result, rec_time = run_with_time(factorial_rec, n)
                
                is_same = (iter_result == rec_result)
                
                print(f"n= {n:<3} | same={is_same!s:<5} | iter={iter_time:.6f}s, rec={rec_time:.6f}s")
                print(f"{n}! = {iter_result}")
        
        elif choice.lower() == 'q':
            print("종료합니다.")
            break
            
        else:
            print("잘못된 선택입니다. 메뉴에 있는 항목을 입력해주세요.")

if __name__ == "__main__":
    main()
