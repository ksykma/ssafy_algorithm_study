import random

class ClassHelper:
    def __init__(self, namelst):
        self.namelst = namelst
    def pick(self, n):
        return random.sample(self.namelst, n)
    def match_pair(self):
        result = []
        try:
            for i in range(int(len(self.namelst)) / 2):
                result.append(random.sample(self.namelst, 2))
                self.namelst.remove(result[i][0])
                self.namelst.remove(result[i][1])
            return result
        except TypeError:
            for i in range(len(self.namelst) // 2):
                if len(self.namelst) > 3:
                    result.append(random.sample(self.namelst, 2))
                    self.namelst.remove(result[i][0])
                    self.namelst.remove(result[i][1])
                else:
                    result.append(self.namelst)
            return result


ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())