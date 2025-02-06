#**************************************************************************
# * Name: Marco Soto                                                
# * Date: 07/14/2022                                                   
# *************************************************************************
# * Class Statement and Specifications: 
# * Given any of the following: apothem, radius, or side length, the lengths of
# * the other 2 can be found with some trigonometric formulas. Functions for each are shown below:
# * Input:  
# * radius, apothem, or side length. Whichever one is given, the corresponding function is called
# * Number of sides is always there 
# * Output: 
# * The reamaing 2 of the lengths that were not given 
# * Also area of polygon and the perimeter are calculated
# *************************************************************************

import math

class RegPolygon:

    
     
    

    # Used for drawing the polygon
    PIXEL_SIZE = 100

    # object initializer or constructor
    # @param numSides the number of sides of in the regular polygon   
    # Precondition: numSides must be a positive integer greater than 2 
    # Postcondition: sets numSides to the correct value based on the parameter numSides
    # sets remaining object variables to zero
    def __init__(self, numSides):
        self.numSides = numSides
        self.sideLength = 0
        self.apothem = 0
        self.radius = 0

    # object string representation 
    def __str__(self):
        info =  '{0: <18}'.format('Number of sides ') + '= ' + str(self.numSides) +'\n'
        info += '{0: <18}'.format('Side Length ') + '= ' + str(self.sideLength) + '\n'
        info += '{0: <18}'.format('Apothem ') + '= ' + str(self.apothem) + '\n'
        info += '{0: <18}'.format('Radius ') + '= ' + str(self.radius) + '\n'
        info += '{0: <18}'.format('Perimeter ') + '= ' + str(self.perimeter()) + '\n'
        info += '{0: <18}'.format('Area ') + '= ' + str(self.area()) + '\n'

        return info

    # @param sideLength: the length of a side 
    # Precondition: sideLength is a positive real number
    # Postcondition: sets sideLength, apothem, and radius to the correct values based on 
    # the parameter sideLength
    def setSide(self, sideLength): # calculations using side length
        if sideLength <= 0:
            print("Side length must be a positive real number")
        else:
            self.sideLength = float(sideLength)
            self.apothem = (self.sideLength/2) * math.tan(math.pi*(self.numSides-2)/(2*self.numSides))
            self.radius = self.sideLength / (2*math.cos(math.pi*(self.numSides-2)/(2*self.numSides)))
            return self.sideLength, self.apothem, self.radius

    # @param apothem: the length of the apothem 
    # Precondition: apothem is a positive real number
    # Postcondition: sets apothem, sideLength, and radius to the correct values based on 
    # the parameter apothem
    def setApothem(self, apothem): # calculations using apothem
        if apothem <= 0:
            print("Apothem must be a positive real number")
        else:
            self.apothem = float(apothem)
            self.sideLength = (2*self.apothem) / (math.tan(math.pi*(self.numSides-2)/(2*self.numSides)))
            self.radius = self.apothem / (math.sin(math.pi*(self.numSides-2)/(2*self.numSides)))
            return self.apothem, self.sideLength, self.radius

    # @param radius: the length of the radius 
    # Precondition: radius is a positive real number
    # Postcondition: sets radius, apothem, and sideLength to the correct values based on 
    # the parameter radius
    def setRadius(self, radius): # calculations using radius 
        if radius <= 0:
            print("Radius must be a positive real number")
        else:
            self.radius = float(radius)
            self.apothem = self.radius * math.sin(math.pi*(self.numSides-2)/(2*self.numSides))
            self.sideLength = 2 * self.radius * math.cos(math.pi*(self.numSides-2)/(2*self.numSides))
            return self.radius, self.apothem, self.sideLength

    # Postcondition: returns the perimeter 	
    def perimeter(self): # perimeter = ns or number of sides * side length
        return self.numSides * self.sideLength

    # Postcondition: returns the area	
    def area(self): # area = 1/2 * apothem * perimeter 
        perimeter = self.perimeter()
        return (1/2) * self.apothem * perimeter
    


