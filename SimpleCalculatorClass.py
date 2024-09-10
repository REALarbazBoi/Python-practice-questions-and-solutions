class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

    @staticmethod
    def div(a,b):
        return a//b

    @staticmethod
    def mul(a,b):
        return a*b

x=10
y=5
print(Calculator.add(x,y))
print(Calculator.sub(x,y))
print(Calculator.div(x,y))
print(Calculator.mul(x,y))