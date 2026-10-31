class Phone:
    def __init__(self,brand,storage):
        self.brand=brand
        self.storage=storage

    def advertise_phone(self):
        print(f"Helloo, here is {self.brand}")
        print(f"It comes with a storage of {self.storage}gb")

    def buy_phone(self):
        print(f"I bought a brand new {self.brand} @15,0000 ")

phone1=Phone("Infinix Hot 60i",128)
phone2=Phone("Sumsung S38",256)

phone1.buy_phone()
phone2.advertise_phone()