class Carro:
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano 
    def __str__(self):
        return f'{self.modelo}, {self.cor}, {self.ano}'
    

carro1 = Carro('Uno','Vermelho','2013')        
print(carro1)