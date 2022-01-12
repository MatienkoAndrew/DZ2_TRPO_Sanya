from src.RawDataGateway.PlantGateway import PlantGateway


class Plant:
    def __init__(self):
        self.plant = None
        self.length = None
        self.weight = None
        pass

    # записываем растение в БД
    def createPlant(self, plant_name, length, weight):
        plant = PlantGateway()
        plant.plant = plant_name
        plant.length = length
        plant.weight = weight
        plant.Insert()
        pass

    # считываем все растения из БД
    def getAll(self):
        return PlantGateway().getAll()

    # считываем последнее введенное растение
    def getLastRestaurant(self):
        plant = PlantGateway()
        lastId = plant.getLastId()

        plantInfo = plant.getLastPlant(lastId)
        return plantInfo
