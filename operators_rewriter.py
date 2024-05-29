class Building:
    def __init__(self, building_type, number_of_floors):
        self.building_type = building_type
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        return (self.building_type == other.building_type and
                self.number_of_floors == other.number_of_floors)


house = Building('дом', 18)
flat = Building('квартира', 18)
print(house == flat)
