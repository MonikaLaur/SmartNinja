class Vehicle:
    def __init__(self, brand, model, kilometers, gs_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.gs_date = gs_date

    def vehicle_brand_model(self):
        return self.brand + " " + self.model

# see the list of vehicles comp has

def list_all_vehicles(Vehicles): # note its VehicleS not Vehicle
    for index, car in enumerate(Vehicles):
        print "Vehicle ID: " + str(index +1)
        print "Brand: " + car.brand
        print "Model: " + car.model
        print "Kilometers gone so far: " + car.kilometers
        print "General service date (in dd.mm.yyyy): " + car.gs_date
        print " "

    if not Vehicles:
        print "You do not have any Vehicles in your list at the moment."

# edit kilometers and gs date
def edit_vehicles(Vehicles):
    print "Choose the ID of the Vehicle you would like to edit"

    for index, car in enumerate(Vehicles):
        print str(index +1) + ") " + car.vehicle_brand_model()

    print " "
    selected_id = raw_input("What vehicle would you like to edit? Please enter ID number:  ")
    selected_car = Vehicles[int(selected_id)-1]

    new_kilometers = raw_input("Please enter a new value for kilometers driven with the %s so far: " % selected_car.vehicle_brand_model())
    selected_car.kilometers = new_kilometers

    print " "
    print "Kilometers driven so far successfully updated!"

    print " "

    new_gs_date = raw_input("Please enter the latest general service date for %s so far: " % selected_car.vehicle_brand_model())
    selected_car.gs_date = new_gs_date

    print " "
    print "General service date successfully updated!"

# add new vehicle
def add_new_vehicle(Vehicles):
    brand = raw_input("Please enter the brand of the vehicle")
    model = raw_input("Please enter the model of the vehicle")
    kilometers = raw_input("Please enter the kilometers driven with the vehicle so far")
    gs_date = raw_input("Please enter the general service date")

    new = Vehicle(brand=brand, model=model,kilometers=kilometers, gs_date=gs_date)
    Vehicles.append(new)

    print " "
    print new.vehicle_brand_model() + "vehicle has been added to your vehicle list!"


def delete_vehicle(Vehicles):
    print "Select the vehicle ID you would like to delete"

    for index, car in enumerate(Vehicles):
        print str(index+1) + ") " + car.vehicle_brand_model()

    print " "
    selected_id = raw_input("What vehicle would you like to delete? Please enter ID number:  ")
    selected_car = Vehicles[int(selected_id)-1]

    Vehicles.remove(selected_car)
    print " "
    print "Vehicle was successfully removed from the list."

def main():
    print "Welcome to your Vehicle list!"
    print "-"*100
    print " "

    BMW = Vehicle(brand="BMW", model="X5", kilometers="320", gs_date="01.01.2018")
    Mercedez = Vehicle(brand="Mercedez Benz", model= "C-class", kilometers="630", gs_date="23.07.2017")
    Bugatti = Vehicle(brand="Bugatti",model="Veyron",kilometers="500", gs_date="05.08.2017")

    Vehicles= [BMW,Mercedez,Bugatti]

    while True:
        print " "
        print "Please choose one of these options:"
        print "a) See all your vehicles"
        print "b) Add a new vehicle"
        print "c) Edit a vehicle"
        print "d) Delete a vehicle"
        print "e) Quit the program."
        print ""

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print " "

        if selection.lower()== "a":
            list_all_vehicles(Vehicles)
        elif selection.lower()== "b":
            add_new_vehicle(Vehicles)
        elif selection.lower() == "c":
            edit_vehicles(Vehicles)
        elif selection.lower() == "d":
            delete_vehicle(Vehicles)
        elif selection.lower() == "e":
            print "You have chosen to quit the program, goodbye!"
            break
        else:
            print "Invalid selection, please try again."
            continue

if __name__ == '__main__':
    main()


