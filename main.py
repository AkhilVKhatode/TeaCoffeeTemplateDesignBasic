from abc import ABC, abstractmethod

class Beverage(ABC):
    # Template method to ensure the algorithm steps are followed
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    # Common methods
    def boil_water(self):
        print("Boiling water...")

    def pour_in_cup(self):
        print("Pouring into cup...")

    # Steps to be customized by subclasses
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

# Concrete implementation for Coffee
class CoffeeBeverage(Beverage):
    def brew(self):
        print("Brewing coffee...")

    def add_condiments(self):
        print("Adding sugar and milk...")

# Concrete implementation for Tea
class TeaBeverage(Beverage):
    def brew(self):
        print("Steeping tea bag...")

    def add_condiments(self):
        print("Adding lemon...")

# Main function to test the template method
if __name__ == "__main__":
    coffee = CoffeeBeverage()
    tea = TeaBeverage()
    
    print("Making coffee...")
    coffee.prepare_recipe()
    
    print("\nMaking tea...")
    tea.prepare_recipe()
