'''
Created on 29 janv. 2016

@author: haojizhang
'''
from contrat import contrat

class Abonnement:
    import contrat
    '''
    classdocs
    '''


    def __init__(self, libelle,prix,estpackgar ):
        '''
        Constructor
        '''
        self.libelle = libelle
        self.prix = prix
        self.estpackgar = estpackgar
    def addcontrat(self,contrat):
        self.contrat = contrat
    
    
        
        