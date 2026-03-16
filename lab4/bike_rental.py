class BikeRental:
    def __init__(self):
        self.bikes = []
        self.rented_bikes = {}

    def addBike(self, bike_id):
        """Додає велосипед у систему"""
        self.bikes.append(bike_id)

    def rentBike(self, bike_id, hours):
        """Оренда велосипеда"""
        if bike_id in self.bikes:
            cost = self.calculateRentalCost(hours)
            self.bikes.remove(bike_id)
            self.rented_bikes[bike_id] = hours
            return f"Bike {bike_id} rented for {hours} hours. Cost: {cost}"
        return "Bike not available"

    def calculateRentalCost(self, hours):
        """Обчислює вартість оренди"""
        price_per_hour = 5
        return hours * price_per_hour


def main():
    rental = BikeRental()

    rental.addBike("B1")
    rental.addBike("B2")

    print(rental.rentBike("B1", 3))


if __name__ == "__main__":
    main()
