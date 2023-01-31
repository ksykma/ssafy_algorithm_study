class PublicTransport:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
        
    def get_in(self, count):
        self.count = count
        
    def get_off(self, count):
        self.count = count
    
    def profit(self):
        return self.fare * self.count

class Bus(PublicTransport):
    def max_count(self, count):
        super().get_in(count)
        if self.count > 100:
            print("더이상 탑승할 수 없습니다.")
            
p1 = PublicTransport("김서영", 50000)
p1.get_in(150)
print(p1.profit())