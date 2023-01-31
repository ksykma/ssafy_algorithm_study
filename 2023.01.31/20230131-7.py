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
    
p1 = PublicTransport("김서영", 50000)
p1.get_in(50)
print(p1.profit())