# Person 클래스
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        #f-string: 포맷 스트링(python 3.6)
        return f"ID: {self.id}, Name: {self.name}"

# Manager 클래스 (Person을 상속받음)
class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        return f"ID: {self.id}, Name: {self.name}, Title: {self.title}"

# Employee 클래스 (Person을 상속받음)
class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        return f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}"

# 테스트 코드
def test_code():
    # 1. Person 객체 생성 테스트
    person = Person(1, "Alice")
    assert person.printInfo() == "ID: 1, Name: Alice", "Test 1 Failed"
    
    # 2. Manager 객체 생성 테스트
    manager = Manager(2, "Bob", "Project Manager")
    assert manager.printInfo() == "ID: 2, Name: Bob, Title: Project Manager", "Test 2 Failed"
    
    # 3. Employee 객체 생성 테스트
    employee = Employee(3, "Charlie", "Python Developer")
    assert employee.printInfo() == "ID: 3, Name: Charlie, Skill: Python Developer", "Test 3 Failed"
    
    # 4. Person 객체 수정 테스트
    person.id = 4
    person.name = "David"
    assert person.printInfo() == "ID: 4, Name: David", "Test 4 Failed"
    
    # 5. Manager 객체 수정 테스트
    manager.title = "Senior Manager"
    assert manager.printInfo() == "ID: 2, Name: Bob, Title: Senior Manager", "Test 5 Failed"
    
    # 6. Employee 객체 수정 테스트
    employee.skill = "Java Developer"
    assert employee.printInfo() == "ID: 3, Name: Charlie, Skill: Java Developer", "Test 6 Failed"
    
    # 7. 다양한 Person 객체 테스트
    person2 = Person(5, "Eve")
    assert person2.printInfo() == "ID: 5, Name: Eve", "Test 7 Failed"
    
    # 8. Manager 객체 추가 테스트
    manager2 = Manager(6, "Frank", "HR Manager")
    assert manager2.printInfo() == "ID: 6, Name: Frank, Title: HR Manager", "Test 8 Failed"
    
    # 9. Employee 객체 추가 테스트
    employee2 = Employee(7, "Grace", "Data Scientist")
    assert employee2.printInfo() == "ID: 7, Name: Grace, Skill: Data Scientist", "Test 9 Failed"
    
    # 10. 상속 관계 테스트
    assert isinstance(manager, Person), "Test 10 Failed"
    assert isinstance(employee, Person), "Test 10 Failed"
    
    print("All tests passed.")

# 테스트 실행
test_code()