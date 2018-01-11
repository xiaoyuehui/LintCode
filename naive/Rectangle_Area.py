# -*- coding: utf-8 -*-
class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here
    def __init__(self , _width, _height):
        self.width = _width
        self.height = _height
    
    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    # write your code here
    def getArea(self):
        return self.width * self.height
    

rec = Rectangle(3,4)
print(rec.getArea())
