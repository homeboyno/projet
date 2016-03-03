#from Parking import Parking
import string 

class Panneau_Affichage:
	def __init__(self):
		pass
						
	def afficherNbPlacesDisponible(self, Parking):
		if Parking.nbPlacesLibres > 0:
			Rst = "Nombre de place libre : " + str(Parking.nbPlacesLibres) + " \n"
			for niv in range(0, Parking.nbNiveau) :
				niveau = string.ascii_uppercase[niv]
				Rst += "\tNombre place niveau " + str(niveau) + " : " +str(Parking.NbPlacesLibreAuNiveau(niveau)) + "\n"
				#Nombre de place par Niveau : " + str(Parking.nbPlacesParNiveau)
			return Rst
		else:
			return "Desole, aucune place disponible"

