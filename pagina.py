from articolo import Articolo

class Pagina:
    def __init__(self,art):
        self.art=art
        
    def setPagina(self,art):
        self.art=art
        art=[+self.art]
    
    def getPagina(self):
        return self.art
    
    def __str__(self):
        for i in self.art:
            return str(self.art) 


art1=Articolo("Hello World!","How are you?")
art2=Articolo("Ciao Mondo!","Come stai?")
pag=Pagina(art=[art1,art2])        
print pag
