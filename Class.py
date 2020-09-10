# class Point:
#     def __init__(self,x,y):
#         self.a=x
#         self.b=y
#     def show(self):
#         print(self.a, self.b)
#     def distance(self, taX, taY):
#         return(((self.a-taX)**2)+((self.b-taY)**2))**0.5
# p=Point(6,8)
# p.show()
# result=p.distance(1,2)
# print(result)

class File:
    def __init__(self,name):
        self.name=name
        self.file=None
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
f1=File("TestForData.txt")
f1.open()
data=f1.read()
print(data)