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


