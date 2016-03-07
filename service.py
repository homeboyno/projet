class Service:
    import time
    def __init__(self,dateDemande,dateService,rapport):
        self.dateDemande = dateDemande
        self.dateService = dateDemande
        self.rapport = rapport


class Maintenance(Service):
    def __init__(self,dateDemande,dateService,rapport):
        super().__init__(dateDemande,dateService,rapport)
    def effectuerMaintenance(self,voiture):
        pass

class Entretien(Service):
    def __init__(self,dateDemande,dateService,rapport):
        super().__init__(dateDemande,dateService,rapport)
    def effectuerEntretien(self):
        pass

class Livraison(Service):
    def __init__(self,dateDemande,dateService,rapport):
        super().__init__(dateDemande,dateService,rapport)
    def effectuerLivraison(self):
        pass
    
class Voiturier:
    import time,Voiture
    def __init__(self,numVoiturier):
        self.__numVoiturier = numVoiturier
    def LivrerVoiture(self,voiture,date,heure):
        pass
