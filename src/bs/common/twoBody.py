class twoBody(object):
    '''
    Define basic parameters of two stars in a binary system
    '''
    def __init__(self, mass1, mass2, distance):
        '''
        Units: mass (Solar Mass), distance (A.U.)
        '''
        self.MassOne = self.setMass(mass1)
        self.MassTwo = self.setMass(mass2)
        self.TotalMass = self.MassOne + self.MassTwo
        self.Distance = self.setDistance(distance)
        pass
        
    def setMass(self, mass):
        '''
        Unit: Solar Mass
        '''
        return mass
            
    def setDistance(self, distance):
        '''
        Unit: A.U.
        '''
        return distance
    
    def getMassOne(self):
        return self.MassOne
    
    def getMassTwo(self):
        return self.MassTwo
    
    def getDistance(self):
        return self.Distance;
    
    def getDistanceToMassOne(self):
        return (self.MassTwo/self.TotalMass)*self.Distance
        
    def getDistanceToMassTwo(self):
        return (self.MassOne/self.TotalMass)*self.Distance