class Fourcal():
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first* self.second
        return result
    def sub(self):
        result =self.first-self.second
        return result
    def sub(self):
        result =self.first/self.second
        return result

a=Fourcal(4,2)
print(a.add())



print(0%5)
print(1%5)
print(2%5)


test=[1,2,34,4,5]
print(max(test))

a,b=5,3
t1=a & b
t2= a | b
print(t1)
print(t2)