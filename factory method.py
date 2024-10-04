from abc import ABC, abstractmethod

# Car (Product Interface)
class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
# Ford (Concrete Product)
class Ford(Car):
    def start(self):
        print("Ford is starting its engine.")

    def stop(self):
        print("Ford is stopping its engine.")

# Ferrari (Concrete Product)
class Ferrari(Car):
    def start(self):
        print("Ferrari is roaring to life!")

    def stop(self):
        print("Ferrari is slowing down.")
# CarFactory (Creator Interface)
class CarFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

    def start_car(self):
        car = self.create_car()
        car.start()

    def stop_car(self):
        car = self.create_car()
        car.stop()
# FordFactory (Concrete Creator)
class FordFactory(CarFactory):
    def create_car(self) -> Car:
        return Ford()

# FerrariFactory (Concrete Creator)
class FerrariFactory(CarFactory):
    def create_car(self) -> Car:
        return Ferrari()
if __name__ == "__main__":
    # Instantiate FordFactory and FerrariFactory
    ford_factory = FordFactory()
    ferrari_factory = FerrariFactory()

    # Start and stop Ford using the factory method
    ford_factory.start_car()    # Output: "Ford is starting its engine."
    ford_factory.stop_car()     # Output: "Ford is stopping its engine."

    # Start and stop Ferrari using the factory method
    ferrari_factory.start_car()  # Output: "Ferrari is roaring to life!"
    ferrari_factory.stop_car()   # Output: "Ferrari is slowing down."
