#Criando um objeto sem o metodo construtor 
class Musica:
    nome = ''
    artistas = ''
    duracao = int

musica_pagode = Musica()
musica_pagode.nome = "Sinais"
musica_pagode.artistas= 'Luan Santana'
musica_pagode.duracao = 568

print(vars(musica_pagode))

#Criando um objeto com o metodo contrutor 
class Musica:
    def __init__(self,nome='',artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)