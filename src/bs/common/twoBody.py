class twoBody():
    '''
    Define basic parameters of two stars in a binary system
    '''
    def __init__(self):
        pass
        
    def setMassOne(self, mass):
        '''
        Unit: Solar Mass
        '''
        self.massOne = mass
        
    def setMassTwo(self, mass):
        '''
        Unit: Solar Mass
        '''
        self.massTwo = mass
        
    def setDistance(self, distance):
        '''
        Unit: A.U.
        '''
        self.distance = distance