class Service:
    def fee(self, rent_time, mile):
        self.rent_price = (rent_time // 10) * 1200
        self.insur_price = round(rent_time // 30) * 525
        if mile > 100:
            self.mile_price = (170 * 100) + (85 * (mile - 100))
        else:
            self.mile_price = mile * 170
        return self.rent_price + self.insur_price + self.mile_price

rent1 = Service()
rent2 = Service()


print(rent1.fee(600, 50)) #=> 91000
print(rent2.fee(600, 110)) #=> 100350
