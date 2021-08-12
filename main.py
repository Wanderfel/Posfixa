from pos_fixa import *

expressao = '(A - B) - C'

pos_fixa = PosFixa(expressao)
print(expressao)
print(pos_fixa.transforma_posfixa())

input()
