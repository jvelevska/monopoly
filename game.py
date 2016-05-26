ALL_SECTIONS = {'yellow' : [], 'pink' : [], 'brown':[], 'red':[], 'orange':[],'green':[], 'light_blue':[], 'dark_blue':[]}
STREETS_AVAILABLE = []
SATATIONS_AVAILABLE  = []

class Station:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = Bank
        self.mortgage = int(price / 2)

    def calculate_rent(self, num):
        return self.rent * num

    def buy_station(self, buyer):
        self.owner = buyer

    def mortgage(self):
        self.mortgaged = True

    def unmortgage(self):
        self.mortgaged = False

    
class Street:
    def __init__(self, name, color, price, rent, renths, rentht, pricehs, priceht):
        self.name = name
        self.color = color
        self.price = price
        self.rent = rent
        self.house_rent = renths
        self.hotel_rent = rentht
        self.houses = 0
        self.hotel = False
        self.mortgage = int(price / 2)
        self.unmortgage = self.mortgage + int((1 / 5) * self.mortgage)
        self.mortgaged = False
        self.owner = Bank
        self.price_house = pricehs
        self.price_hotel = priceht

    def buy_street(self, buyer):
        self.owner = buyer

    def build_house(self):
        self.houses = self.houses + 1

    def destroy_house(self):
        self.houses = self.houses - 1

    def build_hotel(self):
        self.houses = 0
        self.Hotel = True

    def destroy_hotel(self):
        self.hotel = False

    def mortgage(self):
        self.mortgaged = True

    def unmortgage(self):
        self.mortgaged = False

    def calculate_rent(self, bo):
        if self.houses > 0:
            return 2*self.rent + self.house_rent*self.houses
        if self.hotel:
            return 2*self.rent + self.hotel_rent
        if bo:
           return 2*self.rent
        return self.rent


class Player:
    def __init__(self, name):
        self.name = name
        self.streets = []
        self.stations = []
        self.sections = {'yellow' : [], 'pink' : [], 'brown':[], 'red':[], 'orange':[],'green':[], 'light_blue':[], 'dark_blue':[]}
        self.money = 2000

    def buy_station(self, station):
        station.buy(self)
        self.money = self.money - station.price
        self.stations.append(station)
        SATATIONS_AVAILABLE.remove(station)

    def rent_station(self, station):
        return station.calculate_rent(len(self.stations)

    def buy(self, street):
        street.buy_street(self)
        self.streets.append(street)
        self.money = self.money - street.price
        self.sections[street.color].append(street.name)
        STREETS_AVAILABLE.remove(street)
  
    def check_full_section(self, color):
        for a in ALL_SECTIONS[color]:
            if not a in self.sections[color]:
                return False
        return True

    def build_house(self, street):
        if check_full_section(self, street.color):
            self.streets[streets.index(street)].build_house()
            self.money = self.money - street.price_house

    def build_hotel(self, street):
        if check_full_section(self, street.color):
            self.streets[streets.index(street)].build_hotel()
            self.money = self.money - street.price_hotel
    
    def destroy_house(self, street):
        self.streets[streets.index(street)].destroy_house()
        self.money = self.money + street.price_house
    
    def destroy_hotel(self, street):
        self.streets[streets.index(street)].destroy_hotel()
        self.money = self.money + street.price_hotel

    def check_rent(self, street):
        return street.calculate_rent(self.check_full_section(street.color))

    def trading(self, street1, street2, money1, money2):
        street2.owner = self
        self.sections[street2.color].append(street2.name)                   
        self.streets.append(street2)
        self.money = self.money + money2
        self.sections[street1.color].remove(street1)
        self.streets.remove(street1)
        self.money = self.money - money1
