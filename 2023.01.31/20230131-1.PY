class Calculator:
    def add(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y
    def substract(self, x, y):
        self.x = x
        self.y = y
        return self.x - self.y
    def multuply(self, x, y):
        self.x = x
        self.y = y
        return self.x * self.y
    def divide(self, x, y):
        self.x = x
        self.y = y
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return f"0으로 나눌 수 없습니다."

c1 = Calculator()
print(c1.add(1, 2))
print(c1.substract(2, 1))
print(c1.multuply(3, 4))
print(c1.divide(4, 0))

# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0