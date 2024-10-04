from abc import ABC, abstractmethod

# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 5.0

    def description(self) -> str:
        return "Simple Coffee"

# Decorator (Base Decorator)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._decorated_coffee = coffee
    
    def cost(self) -> float:
        return self._decorated_coffee.cost()

    def description(self) -> str:
        return self._decorated_coffee.description()

# Concrete Decorator 1
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 2.0

    def description(self) -> str:
        return self._decorated_coffee.description() + ", Milk"

# Concrete Decorator 2
class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 1.0

    def description(self) -> str:
        return self._decorated_coffee.description() + ", Sugar"

# Concrete Decorator 3
class WhipCreamDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 3.0

    def description(self) -> str:
        return self._decorated_coffee.description() + ", Whipped Cream"

# Usage
if __name__ == "__main__":
    # Simple coffee
    coffee = SimpleCoffee()
    print(f"{coffee.description()} : ${coffee.cost()}")

    # Coffee with milk
    coffee_with_milk = MilkDecorator(coffee)
    print(f"{coffee_with_milk.description()} : ${coffee_with_milk.cost()}")

    # Coffee with milk and sugar
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"{coffee_with_milk_and_sugar.description()} : ${coffee_with_milk_and_sugar.cost()}")

    # Coffee with milk, sugar, and whipped cream
    coffee_fancy = WhipCreamDecorator(coffee_with_milk_and_sugar)
    print(f"{coffee_fancy.description()} : ${coffee_fancy.cost()}")
