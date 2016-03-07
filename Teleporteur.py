from Placement import Placement 
from datetime import datetime

class Teleporteur:
	def __init__(self, tel):
		self.tel = tel  #telEntree ou telSortie.
		
	def teleporterVoiture(self, voiture, place):
		"""
		Set the car in a placement
		Save this information in TracePassage.txt
		"""
		placement = Placement(voiture, place) #Creer un nouveau placement entre la voiture et la place
		voiture.addPlacementV(placement)
		place.addPlacementP(placement)
		print("Votre voiture est bien prise en charge. Place: "+ str(place.idPlace) +". Bonne journee !")
		with open('TracePassage.txt', 'a') as fichier:
			fichier.write(str(datetime.now()) + ": Entree du vehicule : " + str(voiture.immatriculation) + ". Place occupe : " + str(place.idPlace) +".\n")
		
	def teleporterVoitureSuperAbonne(self, voiture):
		if(Parking.recherchePlace(voiture) == None):
			print("Votre voiture est bien prise en charge. Bonne journee !")
			with open('TracePassage.txt', 'a') as fichier:
				fichier.write(str(datetime.now()) + ": Entree du vehicule super Abonne : " + str(voiture.immatriculation) + "\n")
		else:
			teleporterVoiture(voiture, Parking.recherchePlace(voiture))
		
	def retirerVoiture(self, placeID, parking):
		"""
		Free the car in the placement 
		Save this information in TracePassage.txt
		"""
		for pla in parking.places:
			if pla.idPlace == placeID and pla.estLibre == False:
				pla.placement.partirPlace()
				parking.nbPlacesLibres += 1 
				print("Veuillez patienter le temps que votre vehicule arrive.")
				with open('TracePassage.txt', 'a') as fichier:
					fichier.write(str(datetime.now()) + ": Sortie du vehicule : " + str(pla.placement.voiture.immatriculation) + ". Place occupe : " + str(pla.idPlace) +".\n")
				return
		print("La place demander est incorrect")
		
