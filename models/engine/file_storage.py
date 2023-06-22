#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

classes = {'BaseModel', 'User', 'Place',
           'State', 'City', 'Amenity', 'Review'}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            cls_name = cls.__name__
            if cls_name in classes:
                cls_objects = {}
                for item, value in FileStorage.__objects.items():
                    if value.__class__.__name__ == cls_name:
                        cls_objects[item] = value
                return cls_objects
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=2)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete obj from __objects

        Args:
            obj (dict, optional): _description_. Defaults to None.
        """
        if obj is not None:
            obj_dict = obj.to_dict()
            obj = f"{obj_dict['__class__']}.{obj_dict['id']}"

            if obj in FileStorage.__objects:
                del FileStorage.__objects[obj]
                self.save()
