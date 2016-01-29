from Parking import Parking

class Panneau_Affichage:
	def __init__(self):
		pass
						
	def afficherNbPlacesDisponible(self, Parking):
		if(Parking.nbPlacesLibres > 0):
			Rst = "Nombre de place libre : " + str(Parking.nbPlacesLibres) + " "
			for niveau in range(0, Parking.nbNiveaux+1) 
			Rst += "Nombre place niveau " + str(niveau) + " " +str(Parking.nbPlacesParNiveau(niveau)
			Nombre de place par Niveau : " + str(Parking.nbPlacesParNiveau)
		else:
			return "Desole, aucune place disponible"

