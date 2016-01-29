'''
Created on 29 janv. 2016

@author: haojizhang
'''

class contrat:
    import time
    def __init__(self,dateDebut,dateFin,estEnCours):
        self.dateDebut =dateDebut
        self.dateFin = dateFin
        self.estEnCours = True
    @property
    def getEstEnCours(self):
        return self.estEnCours
    
    def rompreContrat(self):
        self.estEnCours = False
    