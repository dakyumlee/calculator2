one = float(input("첫번째 값 입력"))
two = float(input("두번째 값 입력"))

class calculator() :
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result

    def min(self):
        result = self.first - self.second
        return result
    
    def multi(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
three = calculator(one, two)
print("+", three.add())
print('-', three.min())
print("x", three.multi())
print("/", three.div())