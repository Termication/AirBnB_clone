import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, does nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    if cls_name == 'BaseModel':
                        self.__objects[key] = BaseModel(**value)
                    elif cls_name == 'User':
                        self.__objects[key] = User(**value)
                    # Add other classes here as needed
        except FileNotFoundError:
            pass
