class People():
    def make_instance(self):   # 함수이름은 __init__이라고 하면, h1.make_instance() 없어도 바로 객체생성
        self.name = None
        self.age = None
        self.addr = None

h1 = People()
h1.make_instance()
print(h1.addr)
h2 = People()
print(h2.addr)    # h2는 h2.make_instance()라는 객체를 선언안해서 오류