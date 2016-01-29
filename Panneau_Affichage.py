from Parking import Parking

class Panneau_Affichage:
	def __init__(self):
		pass
						
	def afficherNbPlacesDisponible(self, Parking):
		if(Parking.nbPlacesLibres > 0):
			Rst = "Nombre de place libre : " + str(Parking.nbPlacesLibres) + " \n"
			for niveau in range(0, Parking.nbNiveaux) :
				Rst += "\tNombre place niveau " + str(niveau) + " : " +str(Parking.nbPlacesParNiveau(niveau)) + "\n"
				#Nombre de place par Niveau : " + str(Parking.nbPlacesParNiveau)
			return Rst
		else:
			return "Desole, aucune place disponible"

