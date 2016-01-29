# Classe faites : Camera ; Panneau_affichage; Acces; Teleporteur; Place; 
# Classe à completer : 
# Classe à faire : 
#
#
#
'''
Procedure pour initialiser le projet (no verif)
	creer panneau affichage
	creer les deux teleporteurs
	creer camera
	creer acces (avec tout les param precedent
	creer borneTicket
	x2
	creer parking
	creer un emseble de place
'''
from Client import Client
#from Parking import Parking
from Camera import Camera
from Borne_Ticket import Borne_Ticket
from Teleporteur import Teleporteur
from Panneau_Affichage import Panneau_Affichage
from Voiture import Voiture
from Panneau_Affichage import Panneau_Affichage


panneau_affi1 = Panneau_Affichage()
tel_entree = Teleporteur(TelEntree)
tel_sortie = Teleporteur(TelSortie)
borne_ticket = Borne_Ticket()
camera1 = Camera()
acces1 = Acces(panneau_affi, tel_entree, tel_sortie, borne_ticket, camera1, parking)
borne_ticket.add(acces1)
camera1.add(acces1)




clt = Client("Robert", "rue de la foret")
#clt.nouvelle_voiture()
vtr = Voiture(150,50,"F4SD5")
print(vtr.hauteur)
print(vtr.longueur)
print(vtr.immatriculation)
#park = Parking()
#pano = Panneau_Affichage(park)
#pano.afficherNbPlacesDisponible()

