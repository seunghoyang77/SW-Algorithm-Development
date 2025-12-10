# ==============================================================
# 이진 탐색 트리 (Binary Search Tree) 구현 + 성능 테스트
# ==============================================================
import random, time

# 1. 노드 클래스 정의
class BSTNode:
    def __init__(self, key, value):
        """노드 생성: key(비교 기준), value(저장 데이터). 좌/우 자식은 None으로 초기화."""
        self.key = key        # 키 (노드 비교 기준)
        self.value = value    # 값 (저장 데이터)
        self.left = None      # 왼쪽 자식 노드
        self.right = None     # 오른쪽 자식 노드

    # 출력 시 보기 좋은 형식으로 표시 (튜플 형태)
    def __repr__(self):
        return f"( {self.key!r},{self.value!r} )"

# 2. 키(key)값으로 노드를 찾는 탐색 (순환구조)
def search_bst(n, key):
    # n : BSTNode
    """키(key)값으로 노드를 찾는 순환 탐색 : 사전에서 "단어(키)"를 찾는 것 → 알파벳 순서로 찾기"""
    if n is None:
        return None     # 탐색 실패
    elif key == n.key:  # 키 일치
        return n 
    elif key < n.key :
        return search_bst(n.left, key)    # 왼쪽 서브트리로 재귀 탐색
    else:
        return search_bst(n.right, key)   # 오른쪽 서브트리로 재귀 탐색

# 3. 값(value)으로 노드를 찾는 탐색 (전위 순회 기반)
def search_value_bst(n, value):
    """value로 노드를 찾는 전위 순회 탐색:사전에서 "뜻"을 찾는 것 → 모든 단어의 뜻을 전부 읽어봐야 함"""
    if n is None:
        return None
    if value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)

# 4. 삽입 연산 (순환 구조)
def insert_bst(root, node):
    # (1) 현재 BST트리가 비어있으면 새 노드가 그 트리의 루트가 됨
    if root is None:
        return node
    # (2) 동일한 키가 이미 있으면 중복 삽입을 허용하지 않으므로 기존 노드 그대로 반환
    if node.key == root.key:
        return root
    # (3) 삽입할 키가 현재 루트의 키보다 작으면 왼쪽 서브트리로 재귀 삽입
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
      # (4) 크면 오른쪽 서브트리로 재귀 삽입
        root.right =  insert_bst(root.right, node) 

    return root

# 5. 삭제 연산
def delete_bst(root, key):
    """BST에서 키가 key인 노드를 삭제"""
    if root is None:
        return root
    # (1) 삭제할 노드가 왼쪽 서브트리에 있는지 검사
    if key < root.key:
        root.left = delete_bst(root.left, key)
    # (2) 삭제할 노드가 오른쪽 서브트리에 있는지 검사
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else: 
        # (3) 삭제할 노드를 찾음
        # (1-2) 자식이 없는 경우 또는 자식이 하나인 경우: 해당 자식 노드로 대체
        if root.left is None :
            return root.right
        elif root.right is None:
            return root.left
        # (3) 자식이 둘인 경우: 오른쪽 서브트리에서 최소값(후계자)을 찾아 현재 노드(root)를 대체
        succ = root.right # 임시 후계자
        # (3-1)오른쪽 서브트리에서 가장 왼쪽 노드가 후계자(최솟값)
        while succ.left is not None:
            succ = succ.left

         # (3-2) 후계자의 키와 값을 현재 노드(root)로 복사
        root.key = succ.key
        root.value = succ.value
        # (3-3) 후계자 노드는 중복되므로 오른쪽 서브트리에서 후계자 키를 재귀적으로 삭제
        root.right = delete_bst(root.right, succ.key)

    return root 

# 6. 순회 함수
def preorder(n): # n : BSTNode
    if n is not None:
        print(f'({n.key}:{n.value})', end=' ')
        preorder(n.left)
        preorder(n.right)

# 7. 출력 함수
def print_node(msg, n): # n: BSTNode
    if n is None:
        print(msg, "탐색 실패")
    else:
        print(msg, f"({n.key}:{n.value})")

def print_tree(msg, r): # r: 트리의 루트 노드
    print(msg, end='')
    preorder(r)
    print()

# 8. 기본 테스트　
if __name__ == "__main__":
    # 샘플 데이터: (key, value) 형식
    data = [
        (6, "여섯"),  # key=6
        (8, "여덟"),  # key=8
        (2, "둘"),    # key=2
        (4, "넷"),    # key=4
        (7, "일곱"),  # key=7
        (5, "다섯"),  # key=5
        (1, "하나"),  # key=1
        (9, "아홉"),  # key=9
        (3, "셋"),    # key=3
        (0, "영")     # key=0
    ]

    root = None # 루트를 초기화
    for key, value in data: # 각 항목으로 BSTNode 생성 후 트리에 삽입 (중복 키는 insert_bst에서 무시)
        root = insert_bst(root, BSTNode(key, value))

    print_tree("현재 트리 전위순회:", root)

    # 키로 탐색
    n = search_bst(root, 3)
    print_node("srch 3:", n)

    n = search_bst(root, 8)
    print_node("srch 8:", n)

    n = search_bst(root, 0)
    print_node("srch 0:", n)

    n = search_bst(root, 10)
    print_node("srch 10:", n)

    # 값으로 탐색
    n = search_value_bst(root, "둘")
    print_node("search value '둘':", n)
    n = search_value_bst(root, "열")
    print_node("search value '열':", n)

    # 키 노드 삭제 후 전위순회 출력
    root = delete_bst(root, 7)
    print_tree("키=7 삭제 후 트리:", root)

    root = delete_bst(root, 8)
    print_tree("키=8 삭제 후 트리:", root)

    root = delete_bst(root, 2)
    print_tree("키=2 삭제 후 트리:", root)

    root = delete_bst(root, 6)
    print_tree("키=6 삭제 후 트리:", root)
