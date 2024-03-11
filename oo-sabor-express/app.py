from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Ca', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()