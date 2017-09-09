from articolo import *
from pagina import *
from giornale import *

art1=Articolo("Ciao","Come stai?")
art2=Articolo("Hello","How are you?")

pag1=Pagina([art1,art2])

gior1=Giornale([pag1])

print gior1
