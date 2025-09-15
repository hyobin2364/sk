# 학생클래스 생성
# 인스턴스 변수 : 이름 국 영 수
# 인스턴스 메서드 : 총점,평균

class Student:
    def __init__(self,name,korean,math,english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def get_sum(self) : 
        return self.korean +self.math + self.english 

    def get_average(self):
        return self.get_sum() / 3
    
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
    
    def to_string(self):
        return f'이름: {self.name}, 총점: {self.get_sum()}, 평균; {self.get_average()}'

s1 = Student('홍길동', 90,90,90)
print(s1.to_string())