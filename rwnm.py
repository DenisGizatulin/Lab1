import json
import xml.etree.ElementTree as ET
from exceptions import TransportError, InvalidCapacityException, InvalidFileTypeException
from classes import Vehicle, Car, Truck, Bus, Bicycle, Motorcycle, Scooter, Van, Train, Submarine

class TransportManager:
    def __init__(self):
        self.transport_list = []

    def save_to_json(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump([transport.dict for transport in self.transport_list], f)
        except Exception as e:
            print(f"Error while writing JSON: {e}")

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    transport_type = item.pop('type')  # Удаляем тип из данных
                    transport = self.create_vehicle(transport_type, **item)
                    self.transport_list.append(transport)
        except Exception as e:
            print(f"Error while reading from JSON: {e}")

    def save_to_xml(self, filename):
        try:
            root = ET.Element("Transports")
            for transport in self.transport_list:
                vehicle_element = ET.SubElement(root, 'Vehicle',
                                                 name=transport.name,
                                                 capacity=str(transport.capacity),
                                                 type=transport.__class__.__name__)  # Добавляем тип
                if type == 'Car':
                    fuel_type = transport.fuel_type
            tree = ET.ElementTree(root)
            tree.write(filename)
        except Exception as e:
            print(f"Error while writing в XML: {e}")

    def load_from_xml(self, filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            for vehicle in root.findall('Vehicle'):
                name = vehicle.get('name')
                capacity = int(vehicle.get('capacity'))
                transport_type = vehicle.get('type')  # Получаем тип
                transport = self.create_vehicle(transport_type, name=name, capacity=capacity)
                self.transport_list.append(transport)
        except Exception as e:
            print(f"Error while reading из XML: {e}")

    def create_vehicle(self, transport_type, **kwargs):
        if transport_type == 'Car':
            return Car(**kwargs)  # Замените на ваш класс
        elif transport_type == 'Truck':
            return Truck(**kwargs)  # Замените на ваш класс
        else:
            raise ValueError(f"Unknown transport type: {transport_type}")