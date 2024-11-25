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

def test_polygon_equality(polygon_check1,polygon_check2):
    '''this function takes two parameters both of which are objects of Polygon class and tests the __eq__ method which is used to see if two
        objects are equal or not'''
    assert polygon_check1.__eq__(polygon_check2) #checking if polygon1 equals polygon2

test_polygon_equality(POLYGON_NO1,POLYGON_NO2)

def test_polygon_inequality(polygon_check1,polygon_check2):
    '''this function takes two parameters both of which are objects of Polygon class and tests the __ne__ method which is used to see if two
        objects are inequal or not'''
    assert polygon_check1.__ne__(polygon_check2) #checking if polygon1 does not equals polygon2

test_polygon_inequality(QUADRILATERAL,POLYGON_NO1)

def test_polygon_str():
    '''this function tests the method __str__ it defines an object of class Polygon and checks if its string representation is correctly implemented'''
    test_polygon = Polygon("Triangle", [20,20,20])
    assert str(test_polygon) == "Triangle with sides: [20, 20, 20]" #returns true if the string representation is implemented correct

test_polygon_str()

def test_calculate_circumference():
    '''This function checks if the method calculate_circumference returns the  proper perimeter of the polygon or not and accepst approx values'''
    test_polygon = Polygon("Triangle", [20,20,20])
    assert test_polygon.calculate_circumference() == approx(60.0) #checks if the proper perimeter is returned or not

test_calculate_circumference()
