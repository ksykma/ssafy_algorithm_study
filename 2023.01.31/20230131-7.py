class PublicTransport:
    count = 0
    all_count = 0
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
        
    def get_in(self):
        PublicTransport.count += 1
        PublicTransport.all_count += 1

    def get_off(self):
        PublicTransport.count -= 1
    
    def profit(self):
        return PublicTransport.all_count * self.fare
    
p1 = PublicTransport("김서영", 50000)
p1.get_in()
print(p1.count)
print(p1.profit())