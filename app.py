from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gustavo',10)
restaurante_praca.receber_avaliacao('Lari',6)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()