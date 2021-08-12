class PilhaSequencial:

    def __init__(self):
        self.__pilha = []
    
    def __str__(self):
        return f'{self.__pilha}'
    
    def empilha(self,dado):
        self.__pilha.append(dado)

    def desempilha(self):
        return self.__pilha.pop()
    
    def get_pilha(self):
        return self.__pilha
    
    def pilha_vazia(self):
        verificador = False
        if len(self.__pilha) == 0:
            verificador = True
        
        return verificador
    
    def get_topo(self):
        return self.__pilha[-1]


