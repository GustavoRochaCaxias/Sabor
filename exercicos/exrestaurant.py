class Restaurante :
    nome = ''
    categoria = ''
    ativo = True 

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()   
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food' 

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')    


if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else: 
    print('O restaurante está inativo.')    