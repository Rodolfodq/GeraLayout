import os
import sys
from trata_layout_ent import le_texto, salva_lay_entrada

try:
    arquivo = sys.argv[1]    
except:
    arquivo = input("Informe o nome do arquivo: ")
    arquivo = ".\\" + arquivo

layout_name = input("Informe o código do cliente: ")        
texto_arq = le_texto(arquivo) 
salva_lay_entrada(texto_arq, layout_name)



