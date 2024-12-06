class Vehicle:
    def __init__(self, model, mileage, price):
        self.model = model
        self.mileage = mileage
        self.price = price
        self.vehicles = []  

    def __str__(self):
        return f"Model: {self.model}, Mileage: {self.mileage}, Price: {self.price}"

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)  
    def show_details(self, model):
        for veh in self.vehicles:
            if veh.model == model:
                print(veh)
                return
        print("Model not found.")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles available.")
            return
        for vehicle in self.vehicles:
            print(vehicle)


class Car(Vehicle):
    def __init__(self, model, mileage, price, number_of_doors):
        super().__init__(model, mileage, price)
        self.number_of_doors = number_of_doors

    def add_car(self, car):
        self.add_vehicle(car)  

    def show_details(self, model):
        super().show_details(model)  

class Bike(Vehicle):
    def __init__(self, model, mileage, price, type_of_handlebars):
        super().__init__(model, mileage, price)
        self.type_of_handlebars = type_of_handlebars

    def add_bike(self, bike):
        self.add_vehicle(bike)  

    def show_details(self, model):
        super().show_details(model) 


class ElectricCar(Car, Bike):  
    def __init__(self, model, mileage, price, number_of_doors, type_of_handlebars, battery_capacity):
        Car.__init__(self, model, mileage, price, number_of_doors)  
        Bike.__init__(self, model, mileage, price, type_of_handlebars)  
        self.battery_capacity = battery_capacity

    def add_electric_car(self, electric_car):
        self.add_car(electric_car)  

    def show_details(self, model):
        super().show_details(model)  

def main():
    vehicle_manager = Vehicle('Manager', '0', '0')  

    while True:
        print("\nVehicle Menu")
        print("1. Display All Vehicles")
        print("2. Vehicle Details")
        print("3. Add Vehicle")
        print("4. Car Menu")
        print("5. Bike Menu")
        print("6. Electric Car Menu")
        print("7. Exit")

        choice = input("\nChoose your option: ")

        if choice == '1':
            print("\nAll vehicles: ")
            vehicle_manager.display_vehicles()

        elif choice == '2':
            model = input("Enter Model number: ")
            vehicle_manager.show_details(model)

        elif choice == '3':
            model = input("Enter model of the vehicle: ")
            mileage = input("Enter mileage of the vehicle: ")
            price = input("Enter price of the vehicle: ")
            vehicle_manager.add_vehicle(Vehicle(model, mileage, price))

        elif choice == '4':
            while True:
                print("\nCar Menu")
                print("1. Display Cars")
                print("2. Car Details")
                print("3. Add Cars")
                print("4. Back")

                car_choice = input("\nChoose your option: ")

                if car_choice == '1':
                    for veh in vehicle_manager.vehicles:
                        if isinstance(veh, Car):
                            print(veh)

                elif car_choice == '2':
                    model = input("Enter Model number: ")
                    for veh in vehicle_manager.vehicles:
                        if isinstance(veh, Car):
                            veh.show_details(model)

                elif car_choice == '3':
                    model = input("Enter model of the car: ")
                    mileage = input("Enter mileage of the car: ")
                    price = input("Enter price of the car: ")
                    number_of_doors = input("Enter number of doors: ")
                    vehicle_manager.add_vehicle(Car(model, mileage, price, number_of_doors))

                elif car_choice == '4':
                    break

        elif choice == '5':
            while True:
                print("\nBike Menu")
                print("1. Display Bikes")
                print("2. Bike Details")
                print("3. Add Bikes")
                print("4. Back")

                bike_choice = input("\nChoose your option: ")

                if bike_choice == '1':
                    for veh in vehicle_manager.vehicles:
                        if isinstance(veh, Bike):
                            print(veh)

                elif bike_choice == '2':
                    model = input("Enter Model number: ")
                    for veh in vehicle_manager.vehicles:
                        if isinstance(veh, Bike):
                            veh.show_details(model)

                elif bike_choice == '3':
                    model = input("Enter model of the bike: ")
                    mileage = input("Enter mileage of the bike: ")
                    price = input("Enter price of the bike: ")
                    type_of_handlebar = input("Enter type of handlebar: ")
                    vehicle_manager.add_vehicle(Bike(model, mileage, price, type_of_handlebar))

                elif bike_choice == '4':
                    break

        elif choice == '6':
            while True:
                print("\nElectric Car Menu")
                print("1. Display Electric Cars")
                print("2. Electric Car Details")
                print("3. Add Electric Cars")
                print("4. Back")

                ev_choice = input("\nChoose your option: ")

                if ev_choice == '1':
                    for veh in vehicle_manager.vehicles:
                        if isinstance(veh, ElectricCar):
                            print(veh)

                elif ev_choice == '2':
                    model = input("Enter Model number: ")
                    for veh in vehicle_manager.vehicles:
                        if isinstance(veh, ElectricCar):
                            veh.show_details(model)

                elif ev_choice == '3':
                    model = input("Enter model of the electric car: ")
                    mileage = input("Enter mileage of the electric car: ")
                    price = input("Enter price of the electric car: ")
                    number_of_doors = input("Enter number of doors: ")
                    battery_capacity = input("Enter battery capacity: ")
                    vehicle_manager.add_vehicle(ElectricCar(model, mileage, price, number_of_doors, battery_capacity))

                elif ev_choice == '4':
                    break

        elif choice == '7':
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
