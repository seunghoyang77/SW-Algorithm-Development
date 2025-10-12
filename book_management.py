# book_management.py

class Book:
    """도서(Book) 객체의 정보를 저장하고 관리하는 클래스"""
    def __init__(self, book_id, title, author, year):
        # 책 번호(book_id)는 중복될 수 없으므로, 도서의 고유 식별자로 사용
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        """도서 정보를 문자열로 반환"""
        return f"[ID: {self.book_id}] 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}"

    def __str__(self):
        """객체 출력 시 사용"""
        return self.display_info()

    def __eq__(self, other):
        """도서의 동등성 비교 (책 제목 기반 삭제/조회를 위해 사용)"""
        # 책 제목으로 삭제/조회가 이루어지므로, 여기서는 제목만 비교
        # 실제 BookManagement 클래스에서 책 번호 중복 검사는 따로 처리
        if isinstance(other, Book):
            return self.title == other.title
        return False

class Node:
    """단순 연결 리스트의 노드 클래스"""
    def __init__(self, elem, next=None):
        # 노드의 data 필드는 Book 객체를 저장
        self.data = elem  
        self.link = next

    # 요구사항에 명시된 append와 popNext 메서드 (사용되지는 않으나 명시된 대로 구현)
    def append(self, new_node):
        """현재 노드 다음에 new_node를 삽입"""
        if self.link is not None:
            new_node.link = self.link
        self.link = new_node

    def popNext(self):
        """현재 노드의 다음 노드를 삭제한 후 반환"""
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


class LinkedList:
    """단순 연결 리스트 구조로, Book 객체를 저장하고 관리하는 클래스"""
    def __init__(self):
        # 리스트의 시작을 가리키는 head 포인터
        self.head = None

    def isEmpty(self):
        """리스트가 비어있는지 확인"""
        return self.head is None

    def add_first(self, book):
        """리스트의 맨 앞에 새로운 도서를 추가 (Node 객체 생성 후 삽입)"""
        new_node = Node(book, self.head)
        self.head = new_node

    def find_by_title(self, title):
        """책 제목으로 도서를 검색하고, 해당 Book 객체를 반환. 없으면 None 반환."""
        current = self.head
        while current is not None:
            if current.data.title == title:
                return current.data  # Book 객체 반환
            current = current.link
        return None

    def find_pos_by_title(self, title):
        """책 제목을 기반으로 리스트에서 도서의 위치(pos, 1부터 시작)를 찾아 반환. 없으면 -1 반환."""
        current = self.head
        pos = 1
        while current is not None:
            if current.data.title == title:
                return pos
            current = current.link
            pos += 1
        return -1

    def find_by_id(self, book_id):
        """책 번호로 도서를 검색하고, 해당 Book 객체를 반환. 없으면 None 반환."""
        current = self.head
        while current is not None:
            if current.data.book_id == book_id:
                return current.data
            current = current.link
        return None
    
    def remove_by_title(self, title):
        """책 제목으로 도서를 삭제하고, 삭제된 Book 객체를 반환. 없으면 None 반환."""
        if self.isEmpty():
            return None
        
        current = self.head
        prev = None
        
        # head 노드 처리
        if current is not None and current.data.title == title:
            deleted_book = current.data
            self.head = current.link
            return deleted_book

        # 중간/끝 노드 처리
        while current is not None:
            if current.data.title == title:
                deleted_book = current.data
                prev.link = current.link  # 이전 노드의 link를 다음 노드로 연결
                return deleted_book
            prev = current
            current = current.link
        
        return None # 해당 제목의 도서가 없는 경우

    def display_all(self):
        """현재 리스트에 등록된 모든 도서를 출력하고, 도서 목록(리스트)을 반환"""
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return []
        
        book_list = []
        current = self.head
        while current is not None:
            book_list.append(current.data.display_info())
            current = current.link
        
        for info in book_list:
            print(info)
            
        return book_list


class BookManagement:
    """도서 관리 프로그램의 핵심 기능을 구현하는 클래스"""
    def __init__(self):
        # 도서 저장을 위해 LinkedList 인스턴스 사용
        self.book_list = LinkedList()

    def add_book(self, book_id, title, author, year):
        """새로운 도서를 리스트에 추가"""
        # 1. 책 번호 중복 검사
        if self.book_list.find_by_id(book_id):
            print("오류: 중복된 책 번호입니다. 도서 추가에 실패했습니다.")
            return

        try:
            # 유효성 검사 (간단한 예시, 실제로는 더 철저한 검사 필요)
            book_id = int(book_id)
            year = int(year)
        except ValueError:
            print("오류: 책 번호와 출판 연도는 숫자로 입력해야 합니다.")
            return

        new_book = Book(book_id, title, author, year)
        # 리스트 맨 앞에 삽입 (요구사항상 특별한 정렬 기준이 없으므로 단순 연결 리스트의 효율적인 삽입 방식을 사용)
        self.book_list.add_first(new_book)
        print(f"도서 추가 성공: '{title}'(ID: {book_id})가 등록되었습니다.")

    def remove_book(self, title):
        """주어진 책 제목에 해당하는 도서를 리스트에서 삭제"""
        deleted_book = self.book_list.remove_by_title(title)
        
        if deleted_book:
            print(f"도서 삭제 성공: '{deleted_book.title}'이(가) 삭제되었습니다.")
            # 삭제된 도서의 정보 출력 (책 번호, 책 제목, 저자, 출판 연도)
            print(f"삭제된 도서 정보: {deleted_book.display_info()}")
        else:
            print(f"오류: 제목 '{title}'에 해당하는 도서가 존재하지 않아 삭제에 실패했습니다.")

    def search_book(self, title):
        """주어진 책 제목에 해당하는 도서를 리스트에서 조회"""
        book_info = self.book_list.find_by_title(title)
        
        if book_info:
            print("도서 조회 성공:")
            # 조회된 도서의 정보 출력 (책 번호, 책 제목, 저자, 출판 연도)
            print(book_info.display_info())
        else:
            print(f"오류: 제목 '{title}'에 해당하는 도서를 찾을 수 없습니다.")

    def display_books(self):
        """현재 리스트에 등록된 모든 도서를 출력"""
        print("\n=== 전체 도서 목록 ===")
        # LinkedList의 display_all 메서드가 출력까지 처리
        self.book_list.display_all()
        print("====================\n")

    def print_menu(self):
        """사용자 메뉴를 출력"""
        print("\n=== 도서 관리 프로그램 ===")
        print("1. 도서 추가")
        print("2. 도서 삭제 (책 제목으로 삭제)")
        print("3. 도서 조회 (책 제목으로 조회)")
        print("4. 전체 도서 목록 출력")
        print("5. 프로그램 종료")
        print("========================")

    def run(self):
        """프로그램이 종료될 때까지 메뉴를 출력하고, 사용자 선택 작업을 수행"""
        while True:
            self.print_menu()
            choice = input("메뉴를 선택하세요 (1-5): ").strip()

            if choice == '1':
                # 1. 도서 추가 기능
                print("\n[도서 추가]")
                book_id = input("책 번호(정수) 입력: ").strip()
                title = input("책 제목 입력: ").strip()
                author = input("저자 입력: ").strip()
                year = input("출판 연도(정수) 입력: ").strip()
                
                # 입력값 유효성 검사 (BookManagement.add_book 내부에서 처리)
                if not book_id or not title or not author or not year:
                    print("오류: 모든 항목을 입력해야 합니다.")
                    continue
                
                self.add_book(book_id, title, author, year)
                
            elif choice == '2':
                # 2. 도서 삭제 기능 (책 제목으로 삭제)
                print("\n[도서 삭제]")
                title = input("삭제할 책 제목 입력: ").strip()
                if not title:
                    print("오류: 책 제목을 입력해야 합니다.")
                    continue
                self.remove_book(title)
                
            elif choice == '3':
                # 3. 도서 조회 기능 (책 제목으로 조회)
                print("\n[도서 조회]")
                title = input("조회할 책 제목 입력: ").strip()
                if not title:
                    print("오류: 책 제목을 입력해야 합니다.")
                    continue
                self.search_book(title)
                
            elif choice == '4':
                # 4. 전체 도서 목록 출력 기능
                self.display_books()
                
            elif choice == '5':
                # 5. 프로그램 종료 기능
                print("\n프로그램을 종료합니다. 안녕히 가세요! 👋")
                break
                
            else:
                # 잘못된 메뉴 선택 시 오류 처리
                print("오류: 잘못된 메뉴 선택입니다. 1에서 5 사이의 숫자를 입력해 주세요.")
                

if __name__ == "__main__":
    # 프로그램 실행 코드 블록
    manager = BookManagement()
    manager.run()
