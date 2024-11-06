import json
import xml.etree.ElementTree as ET

from rwnm import TransportManager
from classes import Vehicle, Car, Truck, Bus, Bicycle, Motorcycle, Scooter, Van, Train, Submarine
from exceptions import TransportError

if __name__ == "__main__":
    manager = TransportManager()

    # Adding vehicles
    manager.transport_list.append(Car("Sedan", 5, 'gasoline'))
    manager.transport_list.append(Truck("Pickup", 2, 2000))

    # Saving to XML
    manager.save_to_xml("transports.xml")

    # Resetting the manager and loading from XML
    new_manager = TransportManager()
    new_manager.load_from_xml("transports.xml")

    # Display loaded vehicles
    for vehicle in new_manager.transport_list:
        print(f"Loaded {vehicle.__class__.__name__}: {vehicle.name}, Capacity: {vehicle.capacity}")