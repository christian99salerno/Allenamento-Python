class Giornale:
    def __init__(self,pag):
        self.pag=pag
    def setGiornale(self,pag,index_pag):
        self.pag[index_pag]=pag
    def getGiornale(self,pag):
        return self.pag
    def aggiungi_pagina(self,pag):
        self.pag.append(pag)
    def __str__(self):
        pags=""
        for i in self.pag:
            pags=pags+str(i)
        return pags
        
