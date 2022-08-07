# Returns None as well,bcz of not defining constructot?
# class person:
#     def talk(self):
#         print("Talk")
# p = person()
# print(p.talk())
class Person:
    def __init__(self,name):
        self.name =name
    def talk(self):
        print("Talk")
    def walk(self):
        print("Walk")
p = Person("maha")
print(p.name)
p.talk()
p.walk()

