class InvalidCapacityException(Exception):
    def __init__(self, capacity):
        super().__init__(f"Invalid capacity value: {capacity}. Capacity have to be positive .")


class InvalidFileTypeException(Exception):
    def __init__(self, file_type):
        super().__init__(f"Invalid file type: {file_type}. Allowed types: json, xml.")