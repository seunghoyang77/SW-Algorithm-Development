import random, time
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Malgun Gothic"   
# 랜덤 시드 고정
random.seed(42)

# 1. 순차 탐색 (Sequential Search): O(n)
def linear_search(arr, key, low=0, high=None): 
    if high is None:
        high = len(arr) - 1
    count = 0
    for i in range(low, high + 1):
        count += 1
        if arr[i] == key:
            return i, count
    return -1, count

# 2. 이동 평균 탐색 (Sequential Search with Transpose)
def sequential_search_transpose(arr, key, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    count = 0
    for i in range(low, high + 1):
        count += 1
        if arr[i] == key:
            if i > low:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                i -= 1
            return i, count
    return -1, count

# 3. 이진 탐색 (Binary Search): O(log n)
def binary_search_iter(arr, key, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    count = 0
    left, right = low, high
    while left <= right:
        mid = (left + right) // 2
        count += 1
        if arr[mid] == key:
            return mid, count
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1, count

# 4. 보간 탐색 (Interpolation Search)
def interpolation_search(arr, key, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    count = 0
    left, right = low, high
    while left <= right and arr[left] <= key <= arr[right]:
        count += 1
        if arr[right] == arr[left]:
            break
        mid = left + int((right - left) * (key - arr[left]) / (arr[right] - arr[left]))
        if arr[mid] == key:
            return mid, count
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1, count


# 5. 성능 테스트
n = 10000
arr = sorted(random.sample(range(n * 3), n))
targets = random.sample(arr, 1000)

def measure(func, arr, targets):
    total_time, total_cmp = 0, 0
    for t in targets:
        test_arr = arr[:]
        start = time.time()
        _, cmp_cnt = func(test_arr, t, 0, len(test_arr) - 1)
        total_time += time.time() - start
        total_cmp += cmp_cnt
    return total_time / len(targets), total_cmp / len(targets)

linear_t, linear_c = measure(linear_search, arr, targets)
sequential_t, sequential_c = measure(sequential_search_transpose, arr, targets)
binary_t, binary_c = measure(binary_search_iter, arr, targets)
interp_t, interp_c = measure(interpolation_search, arr, targets)

print("=== 탐색 알고리즘 성능 비교 결과 ===")
print(f"순차 탐색 : 평균 {linear_c:.2f}회 비교, 평균시간 {linear_t*1e6:.2f} μs")
print(f"이동 평균 탐색 : 평균 {sequential_c:.2f}회 비교, 평균시간 {sequential_t*1e6:.2f} μs")
print(f"이진 탐색 : 평균 {binary_c:.2f}회 비교, 평균시간 {binary_t*1e6:.2f} μs")
print(f"보간 탐색 : 평균 {interp_c:.2f}회 비교, 평균시간 {interp_t*1e6:.2f} μs")

# 6. 시각화
labels = ["순차 탐색", "이동 평균 탐색", "이진 탐색", "보간 탐색"]
compare_counts = [linear_c, sequential_c, binary_c, interp_c]
times = [linear_t*1e6, sequential_t*1e6, binary_t*1e6, interp_t*1e6]

#x = np.arange(len(labels))
x = [0, 1, 2, 3]    # np.arange() 대신 리스트
width = 0.35
# 리스트는 벡터 연산이 안 되므로 각 원소별로 계산
x_positions = [v - width/2 for v in x]

fig, ax1 = plt.subplots(figsize=(9, 5))

#bars1 = ax1.bar(x - width/2, compare_counts, width,
#               label="비교 횟수", color=["gray", "lightblue", "skyblue", "lightgreen"])
bars1 = ax1.bar(x_positions, compare_counts, width,
                label="비교 횟수", color=["gray", "lightblue", "skyblue", "lightgreen"])
ax1.set_ylabel("평균 비교 횟수")
ax1.set_title("탐색 알고리즘 비교 (비교 연산 횟수 및 실행 시간, n=10,000, 1000회 평균)")
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.set_yscale("log")

ax2 = ax1.twinx()
#bars2 = ax2.bar(x + width/2, times, width, label="평균 실행 시간 (μs)",
#                color=["dimgray", "deepskyblue", "limegreen", "mediumseagreen"])
x_positions = [v + width/2 for v in x]
bars2 = ax2.bar(x_positions, times, width, label="평균 실행 시간 (μs)",
                color=["dimgray", "deepskyblue", "limegreen", "mediumseagreen"])
ax2.set_ylabel("평균 실행 시간 (μs)")
ax2.set_yscale("log")

fig.legend(loc="upper right", ncol=2)
plt.tight_layout()
plt.show()
