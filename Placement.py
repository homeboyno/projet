import datetime

class Placement:
	def __init__(self):
		self.dateDebut = datetime.now() #année mois jours heures minutes seconde microsec
		self.estEnCours = True
		
	def partirPlace(self):
		self.dateFin = datetime.now()
		self.estEnCours = False
		
		
		
