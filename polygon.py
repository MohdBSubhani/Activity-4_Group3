'''Docstring
    This file contains the main function and defines the class Polygon'''

class Polygon:

    __slots__ = ['__name','__sides'] #encapsulation 

    def __init__(self,name,sides):
        '''__init__ method is used to create an object'''
        self.__name = name   #double underscore for encapsulation
        self.__sides = sides

    def get_name(self):
        '''The getter method for the name of the object'''
        return self.__name #returns the name of object
    
    def set_name(self, new_name):
        '''the setter method it allows for changing of the name'''
        self.__name = new_name #new name is assigned as the name for the object

    def get_sides(self):
        '''the getter method for the sides of the polygon object'''
        return self.__sides # returns a list containing the length of all sides
    
    def set_sides(self, new_no_sides):
        '''the setter method for the sides of object allows for changing sides'''
        self.__sides = new_no_sides

    def __eq__(self,other):
        '''this method returns true if two objects have the same name same sides and are of same class'''
        return isinstance(other, self.__class__) and self.__name == other.__name and self.__sides == other.__sides
    
    def __ne__(self,other):
        '''opposite of equality method returns true if two objects are not equal'''
        return not self.__eq__(other)
    
    def __str__(self):
        '''the str method is used to create a string representation of an object in polygon class'''
        return f"{self.__name} with sides: {self.__sides}"

