from articolo import Articolo

class Pagina:
    def __init__(self,art):
        self.art=art
        
    def setPagina(self,art,index_art):
        self.art[index_art]=art
    
    def getPagina(self):
        return self.art

    def aggiungi_articolo(self,art):
        self.art.append(art)
    
    def __str__(self):
        arts=""
        for i in self.art:
            arts=arts+str(i)
        return arts    

