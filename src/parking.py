'''
Created on 29 janv. 2016

@author: haojizhang
'''
class Parking:
   import Voiture
   from abonnement import Abonnement
    def __init__(self,nbPlaceParNiveau,nbPlacesLibres,prix,nbNiveaux):
        self.__nbPlaceParniveau = nbPlaceParNiveau
        self.__nbPlacesLibres = nbPlacesLibres
        self.__prix = prix
        self.nbNiveaux = nbNiveaux   
    def recherhcerPlace(self,voiture):
        pass
      
    def NbPlacesLibresParNIveau(self,niveau):
       pass
    def addAbonnement(self,ab):
       return ab.getEstpackGar()
   
   
       