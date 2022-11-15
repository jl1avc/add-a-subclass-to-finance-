# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 00:57:33 2022

@author: Jon
"""

from os import chdir
chdir('D:/')

from Loan import loan


class finance(loan):
    def __init__(self, name):
        self.name = name
       
    def Value401K(self, pmt, months, intAPR, currentD):
        # how much money will I have after
        # 'months,' given a current values
        # of currentD by putting 'pmt' into the
        # 401k account, assuming interest
        # intAPR
        
        Value = currentD + pmt*((1+intAPR/1200)**months -1)/(intAPR/1200)
        return Value
    
    def FutVal(self, pmt, intR, nMonths):
        _r = intR/1200 # convert APR into decimal
        _F = (pmt*(1+_r)**nMonths - 1)/_r
        return _F
    
    def payout_annuity(self, ValueAnnuity, intR, nMonths): 
        _r = intR/1200
        _pmtPerMo = (ValueAnnuity * _r * (1 + _r)**nMonths) / ((1 +_r)**nMonths) - 1
       
        return(_pmtPerMo)

if __name__ == '__main__':
    finMgt = finance("myFinance")
    
    value = finMgt.Value401K(50, 60, 2.0, 10000)
    print('value of 401k = {value: .2f}')
    
    nMonths = 36*12
    intRate = [3.5, 5.5, 8.5]
    for r in intRate:
        Fval = finMgt.FutVal(500, r , nMonths)
        print(f'r = {r: 0.2f}, Annuity Value = {Fval: .2f}')
    
    valAnn = 786333.07
    nMonths = 15 * 12
    pmtPerMo = finMgt.payout_annuity(valAnn, 5.5, nMonths)
    print(f'present value of the Annuity: {pmtPerMo: .2f}')
    