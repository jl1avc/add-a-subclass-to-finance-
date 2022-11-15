# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 00:49:30 2022

@author: Jon

We want to construct a class called 'loan'

in this class I want 4 functions:

1  given PV, nMonths, intAPR, compute the monthly payment   name this function computePmt(PV, intAPR, nMonths)

2  given PV, nMonths and monthly payment, Pmt, compute intAPR  name this function compute_intAPR(PV, nMonths, Pmt)

3. given PV, Pmt, intAPR compute the number of months, nMonths name this function compute_nMonths(PV, Pmt, intAPR)

4. given Pmt, intApr, nMonths compute PV, name this function computePV(Pmt, intAPR, nMonths)

For example if I wanted to compute Pmt I would use loan.computePmt(PV, intAPR, nMonths)

"""

class loan(object):
    def __init__ (self, name):
        
        self._name = name
        self._Pv = 0
        self._intAPR = 0
        self._Pmt = 0
        self._nMonths=0
        
        
    def getName(self):
        print(f"\nname on this instance: {self._name}")
    
    def getChoice(self):
        print("\nwhat would you like to compute?")
        print("options: Pmt, Pv, intAPR, nMonths")
        
        choice = 0
        
        while choice  not in ("Pmt", "Pv", "intAPR", "nMonths"):
            choice = input("enter choice ")
            
        if choice == "Pmt":
            self.computePmt()
        elif choice == 'Pv':
            self.computePv()
        elif choice == 'intAPR':
            self.compute_intAPR()
        else:
            self.compute_nMonths()


    def compute_intAPR(self):
        ''' Solve for interest rate, APR  '''
        self._Pv = float(input('Enter PV '))
        self._Pmt = float(input('Enter Pmt '))
        self._nMonths = int(input('Enter number of months '))
        
        fIntRate = lambda r: self._Pmt*(1-(1+r)**(-self._nMonths)) - self._Pv*r

        _rlow =0
        _rhigh = 50 
        
        _rl = _rlow/1200
        _rh = _rhigh/1200
        _count = 0
        
        while(_count < 20): # in case there is no solution
            _rTry = (_rl+_rh)/2
            if abs(fIntRate(_rTry)) < 0.001: break
            
            if fIntRate(_rTry) > 0: _rl = _rTry
            else: _rh = _rTry
            
            _count += 1
            
        if(_count >=20):
            print("no solution: try again")
            print(f"interest rate APR is > {_rTry*1200:.2f}%")
        
        print(f"Interest rate = {_rTry*1200}")
        return _rTry*1200

    def computePmt(self):

        self._Pv = float(input('Enter PV '))
        self._intAPR = float(input('Enter intrest rate '))
        self._nMonths = int(input('Enter number of months '))
        
        _r = self._intAPR / 1200
        
        self._Pmt = _r*self._Pv/(1-(1+_r)**(-self._nMonths))
        
        print(f"Monthly Payment = {self._Pmt}")
        return self._Pmt
    
    def compute_nMonths(self):
        import numpy as np

        self._Pv = float(input('Enter PV '))
        self._intAPR = float(input('Enter intrest rate '))
        self._Pmt = float(input('Enter Pmt '))
        
        _r = self._intAPR / 1200
        
        self._nMonths = -np.log(1-_r*self._Pv/self._Pmt)/np.log((1+_r))
        
        print(f"{self._nMonths} months to pay off loan")
        return self._nMonths

    
    def computePv(self):
        #formula for PV:
        # self._Pmt/_r *(1-(1+_r)**(-self._nMonths))
        
        self._intAPR = float(input('Enter intrest rate '))
        self._Pmt = float(input('Enter Pmt '))
        self._nMonths = int(input('Enter number of months '))
        
        _r = self._intAPR / 1200
        
        self._Pv = self._Pmt/_r *(1-(1+_r)**(-self._nMonths))
        
        print(f'Pv = {self._Pv:.2f}')
        return self._Pv


#####################################################################     
  
if __name__ == '__main__':
    
    loan1 = loan('test1')
    loan1.getName()
    
    loan1.getChoice()