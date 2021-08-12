from pilha_sequencial import *
class PosFixa:

    def __init__(self,expressao):
        self.__prioridade = {'+':4,'-':4,'*':3,'/':3,'**':2}
        self.__expressao = self.__substitui_char(expressao)
        self.__expressao_posfixa = []
    
    def __substitui_char(self,expressao):
        var = expressao.replace(' ','')
        var = list(var)
        lista_aux = []
        contador = 0
        descontador = 0
        
        for i in range(len(var)):
            
            if var[i] == '*' and var[i] == var[i + 1]:
                var[i] +='*'
                aux = i + 1
                lista_aux.append(aux)

        while contador != len(lista_aux):
            del var[lista_aux[contador]-descontador]
            contador += 1 
            descontador += 1    
        
        return var
                

    
    def __verificar_operando(self,dado):
        return dado.isalpha()
    
    def __verificar_operador(self,dado):
        verificador = None
        
        if dado in ['/','*','**','+','-','(',')']:
            verificador = True
        
        else:
            verificador = False
        
        return verificador
    
    def get_expressao(self):
        return self.__expressao
    
    def transforma_posfixa(self):
        pilha = PilhaSequencial()
        for i in range(len(self.__expressao)):
            char = self.__expressao[i]
            if self.__verificar_operando(char):
                self.__expressao_posfixa.append(char)
            
            elif self.__verificar_operador(char):
                if pilha.pilha_vazia() or pilha.get_topo() == '(' or char == '(':
                    pilha.empilha(char)
                
                elif char == ')':
                    while pilha.get_topo() != '(':
                        var = pilha.desempilha()
                        self.__expressao_posfixa.append(var)
                    
                    pilha.desempilha()

                elif self.__prioridade[char] >= self.__prioridade[pilha.get_topo()]:
                    var = pilha.desempilha()
                    self.__expressao_posfixa.append(var)
                    pilha.empilha(char)
                
                else:
                    pilha.empilha(char)
        
        for i in range(len(pilha.get_pilha())):
            var = pilha.desempilha()
            self.__expressao_posfixa.append(var)
        
        return ''.join(self.__expressao_posfixa)
    
    

            