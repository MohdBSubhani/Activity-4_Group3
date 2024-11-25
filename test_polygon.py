'''DOCSTRING
    this file is a test file which contains functions that test the various methods inside of the class Polygon 
    this file calls the class Polygon from the file polygon.py and also calls the function approx from the library pytest'''
from pytest import approx
from polygon import Polygon

QUADRILATERAL = Polygon("Quadrilateral",[7,5,6,7])          # Constant defined as polygon quadrilateral
POLYGON_NO1 = Polygon("Uniform Pentagon",[10,10,10,10,10])  # Constant defined as polygon unifrom pentagon named polgon_no1
POLYGON_NO2 = Polygon("Uniform Pentagon",[10,10,10,10,10])  # Constant defined as polygon unifrom pentagon named polgon_no2

def test_polygon_initialization():
    '''this function tests the initialization method of the class Polygon it creates an object and tchecks wether the correct values have been
        initialized or not'''
    quadrilateral = Polygon("Quadrilateral",[7,5,6,7])  #defining object quadrilateral
    assert quadrilateral.get_name() == "Quadrilateral"  #applying methods on object
    assert quadrilateral.get_sides() == [7,5,6,7]    

test_polygon_initialization()

def testing_get_name(polygon):
    '''this function takes one parameter which is an object of Polygon class and tests the get_name method'''
    assert polygon.get_name() == "Quadrilateral" #returns true if the two operands are equal

testing_get_name(QUADRILATERAL)

def testing_set_name(polygon):
    '''this function takes one parameter which is an object of Polygon class and tests the set_name method'''
    polygon.set_name("Non-Uniform Quadrilateral")#changing the name of the object 
    assert polygon.get_name() == "Non-Uniform Quadrilateral"#returns true if the two operands are equal

testing_set_name(QUADRILATERAL)

def testing_get_sides(polygon):
    '''this function takes one parameter which is an object of Polygon class and tests the get_sides method'''
    assert polygon.get_sides() == [7.0,5.0,6.0,7.0] #returns true if the two operands are equal

testing_get_sides(QUADRILATERAL)

def testing_set_sides(polygon):
    '''this function takes one parameter which is an object of Polygon class and tests the set_sides method'''
    polygon.set_sides([10,10,10,10]) #changes the sides of a polygon
    assert polygon.get_sides() == [10,10,10,10] #returns true if both values are equal

testing_set_sides(QUADRILATERAL)