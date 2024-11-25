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

    def calculate_circumference(self):
        '''this function/method returns the sum of sides ie the perimeter of a polygon object'''
        circumference = 0
        sides = self.get_sides()
        for side in sides:
            circumference += side
        return circumference
    

def main():
    '''this is the main function it creates three objects of polygon class and prints their string representation and their circumference'''
    triangle = Polygon("Triangle", [15.0, 15.0, 15.0])
    print(triangle)
    print('Circumference of triangle:',triangle.calculate_circumference(),'\n')
    square = Polygon("Square", [13.0, 13.0, 13.0, 13.0])
    print(square)
    print('Circumference of square:',square.calculate_circumference(),'\n')
    hexagon = Polygon("Hexagon", [16.0, 16.0, 16.0, 16.0, 16.0, 16.0])
    print(hexagon)
    print('Circumference of hexagon:',hexagon.calculate_circumference(),'\n')


if __name__ == "__main__":
    main()
