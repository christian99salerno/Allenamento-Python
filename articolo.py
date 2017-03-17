class Articolo:
    def __init__(self,titolo,testo):
        self.titolo=titolo
        self.testo=testo
    def setTitolo(self,titolo):
        self.titolo=titolo
    def getTitolo(self):
        return self.titolo
    def setTesto(self,testo):
        self.testo=testo
    def getTesto(self):
        return self.testo
    def __str__(self):
        return self.getTitolo()+"\n"+self.getTesto()
